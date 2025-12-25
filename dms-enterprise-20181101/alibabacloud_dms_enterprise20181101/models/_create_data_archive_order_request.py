# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateDataArchiveOrderRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        param: main_models.CreateDataArchiveOrderRequestParam = None,
        parent_id: int = None,
        plugin_type: str = None,
        related_user_list: List[str] = None,
        tid: int = None,
    ):
        # The description of the task.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters for archiving data.
        # 
        # This parameter is required.
        self.param = param
        # The ID of the parent ticket. A parent ticket is generated only when a child ticket is created.
        self.parent_id = parent_id
        # The type of the plug-in. Default value: DATA_ARCHIVE.
        self.plugin_type = plugin_type
        # The list of the related users.
        self.related_user_list = related_user_list
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Param') is not None:
            temp_model = main_models.CreateDataArchiveOrderRequestParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateDataArchiveOrderRequestParam(DaraModel):
    def __init__(
        self,
        archive_method: str = None,
        cron_str: str = None,
        database_id: str = None,
        logic: bool = None,
        order_after: List[str] = None,
        run_method: str = None,
        source_catalog_name: str = None,
        source_instance_name: str = None,
        source_schema_name: str = None,
        table_includes: List[main_models.CreateDataArchiveOrderRequestParamTableIncludes] = None,
        table_mapping: List[str] = None,
        target_instance_host: str = None,
        variables: List[main_models.CreateDataArchiveOrderRequestParamVariables] = None,
    ):
        # The archiving destination to which you want to archive data. Valid values:
        # 
        # >  If you set ArchiveMethod to a value other than inner_oss, you must register the corresponding destination database with Data Management (DMS) before you create the data archiving ticket. After the database is registered with DMS, the database is displayed in the Instances Connected section of the DMS console.
        # 
        # *   **inner_oss**: dedicated storage, which is a built-in Object Storage Service (OSS) bucket.
        # *   **oss_userself**: OSS bucket of the user.
        # *   **mysql**: ApsaraDB RDS for MySQL instance.
        # *   **polardb**: PolarDB for MySQL cluster.
        # *   **adb_mysql**: AnalyticDB for MySQL V3.0 cluster.
        # *   **lindorm**: Lindorm instance.
        # 
        # This parameter is required.
        self.archive_method = archive_method
        # A crontab expression that specifies the scheduling cycle of the data archiving task. For more information, see the [Crontab expressions](https://help.aliyun.com/document_detail/206581.html) section of the "Create shadow tables for synchronization" topic. You must specify this parameter if you set RunMethod to schedule.
        self.cron_str = cron_str
        # The database ID. If the database is a self-managed database or a third-party cloud database, you can call the [GetDatabase](https://help.aliyun.com/document_detail/465856.html) operation to query the database ID. If the database is an Alibaba Cloud database, ignore this parameter.
        self.database_id = database_id
        # Specifies whether the database is a logical database.
        self.logic = logic
        # The post behaviors.
        self.order_after = order_after
        # The method that is used to run the data archiving task. Valid values:
        # 
        # *   **schedule**: The data archiving task is periodically scheduled.
        # *   **now**: The data archiving task is immediately run.
        # 
        # This parameter is required.
        self.run_method = run_method
        # The catalog of the source database. Valid values:
        # 
        # *   **def**: Set this parameter to def if the source database is of the two-layer logical schema, such as a MySQL database, a PolarDB for MySQL cluster, or an AnalyticDB for MySQL instance.
        # *   **Empty string**: Set this parameter to an empty string if the source database is a Lindorm or ApsaraDB for MongoDB instance.
        # *   **Catalog name**: Set this parameter to the catalog name of the source database if the source database is of the three-layer logical schema, such as a PostgreSQL database.
        # 
        # This parameter is required.
        self.source_catalog_name = source_catalog_name
        # The name of the source instance. If the database instance is a self-managed database or a third-party cloud database, you can call the [GetInstance](https://help.aliyun.com/document_detail/465826.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.source_instance_name = source_instance_name
        # The schema name of the source database. The schema name of the source database is the same as that of the destination database. If the source database is a MySQL database, this parameter specifies the name of the source database. If the source database is a PostgreSQL database, this parameter specifies the schema name of the source database.
        # 
        # This parameter is required.
        self.source_schema_name = source_schema_name
        # The collection of tables to be archived.
        # 
        # This parameter is required.
        self.table_includes = table_includes
        # The table names mapped to the destination database. This parameter is not required and the default value is used.
        self.table_mapping = table_mapping
        # The host of the destination instance. If the destination instance can be accessed over an internal network or the Internet, preferentially set the value to the internal endpoint of the destination instance.
        # 
        # *   If data is archived in an OSS bucket, set the value to the name of the bucket.
        # *   If data is archived in dedicated storage space, set the value to inner_oss.
        # 
        # This parameter is required.
        self.target_instance_host = target_instance_host
        # The configuration of archiving variables. You can use a time variable as a filter condition for archiving data. Each variable has two attributes: name and pattern.
        self.variables = variables

    def validate(self):
        if self.table_includes:
            for v1 in self.table_includes:
                 if v1:
                    v1.validate()
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_method is not None:
            result['ArchiveMethod'] = self.archive_method

        if self.cron_str is not None:
            result['CronStr'] = self.cron_str

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.order_after is not None:
            result['OrderAfter'] = self.order_after

        if self.run_method is not None:
            result['RunMethod'] = self.run_method

        if self.source_catalog_name is not None:
            result['SourceCatalogName'] = self.source_catalog_name

        if self.source_instance_name is not None:
            result['SourceInstanceName'] = self.source_instance_name

        if self.source_schema_name is not None:
            result['SourceSchemaName'] = self.source_schema_name

        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k1 in self.table_includes:
                result['TableIncludes'].append(k1.to_map() if k1 else None)

        if self.table_mapping is not None:
            result['TableMapping'] = self.table_mapping

        if self.target_instance_host is not None:
            result['TargetInstanceHost'] = self.target_instance_host

        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveMethod') is not None:
            self.archive_method = m.get('ArchiveMethod')

        if m.get('CronStr') is not None:
            self.cron_str = m.get('CronStr')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OrderAfter') is not None:
            self.order_after = m.get('OrderAfter')

        if m.get('RunMethod') is not None:
            self.run_method = m.get('RunMethod')

        if m.get('SourceCatalogName') is not None:
            self.source_catalog_name = m.get('SourceCatalogName')

        if m.get('SourceInstanceName') is not None:
            self.source_instance_name = m.get('SourceInstanceName')

        if m.get('SourceSchemaName') is not None:
            self.source_schema_name = m.get('SourceSchemaName')

        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k1 in m.get('TableIncludes'):
                temp_model = main_models.CreateDataArchiveOrderRequestParamTableIncludes()
                self.table_includes.append(temp_model.from_map(k1))

        if m.get('TableMapping') is not None:
            self.table_mapping = m.get('TableMapping')

        if m.get('TargetInstanceHost') is not None:
            self.target_instance_host = m.get('TargetInstanceHost')

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.CreateDataArchiveOrderRequestParamVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class CreateDataArchiveOrderRequestParamVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        pattern: str = None,
    ):
        self.name = name
        self.pattern = pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        return self

class CreateDataArchiveOrderRequestParamTableIncludes(DaraModel):
    def __init__(
        self,
        table_name: str = None,
        table_where: str = None,
    ):
        # The table name.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The filter condition that is specified by the WHERE clause of the archiving configuration. If a time variable is used in the filter condition, the filter condition is specified in the following format: field name <=\\"${variable name}\\". The variable name in the filter condition must be the same as the time variable name that is specified in the Variables parameter.
        self.table_where = table_where

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_where is not None:
            result['TableWhere'] = self.table_where

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableWhere') is not None:
            self.table_where = m.get('TableWhere')

        return self

