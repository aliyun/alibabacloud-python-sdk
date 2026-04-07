# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableBasicInfoRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_source_type: str = None,
        database_name: str = None,
        extension: bool = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        # The ID of the EMR cluster. This parameter is required only if you set the DataSourceType parameter to emr.
        # 
        # You can log on to the [EMR console](https://emr.console.aliyun.com/?spm=a2c4g.11186623.0.0.965cc5c2GeiHet#/cn-hangzhou) to query the ID.
        self.cluster_id = cluster_id
        # The type of the data source. Valid values: odps and emr.
        self.data_source_type = data_source_type
        # The name of the metadatabase. This parameter is required only if you set the DataSourceType parameter to emr.
        # 
        # You can call the [ListMetaDB](https://help.aliyun.com/document_detail/2780105.html) operation to query the name.
        self.database_name = database_name
        # Specifies whether to include extended fields in query results. The extended fields include ReadCount, FavoriteCount, and ViewCount. This parameter takes effect only if you set the DataSourceType parameter to odps.
        self.extension = extension
        # The GUID of the MaxCompute table. Specify the GUID in the odps.projectName.tableName format.
        # 
        # > This parameter is optional for E-MapReduce (EMR) tables.
        self.table_guid = table_guid
        # The name of the metatable in the EMR cluster. This parameter is required only if you set the DataSourceType parameter to emr.
        # 
        # You can call the [GetMetaDBTableList](https://help.aliyun.com/document_detail/2780086.html) operation to query the name.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

