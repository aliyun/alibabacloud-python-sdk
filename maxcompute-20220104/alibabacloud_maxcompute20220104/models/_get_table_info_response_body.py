# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetTableInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetTableInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetTableInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetTableInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_refresh_enabled: bool = None,
        cluster_info: main_models.GetTableInfoResponseBodyDataClusterInfo = None,
        comment: str = None,
        create_table_ddl: str = None,
        creation_time: int = None,
        display_name: str = None,
        file_num: int = None,
        is_external_table: bool = None,
        is_outdated: bool = None,
        last_access_time: int = None,
        last_ddltime: int = None,
        last_modified_time: int = None,
        lifecycle: str = None,
        location: str = None,
        materialized_view: bool = None,
        name: str = None,
        native_columns: List[main_models.GetTableInfoResponseBodyDataNativeColumns] = None,
        odps_properties_rolearn: str = None,
        odps_sql_text_option_flush_header: bool = None,
        odps_text_option_header_lines_count: int = None,
        owner: str = None,
        partition_columns: List[main_models.GetTableInfoResponseBodyDataPartitionColumns] = None,
        physical_size: int = None,
        project_name: str = None,
        rewrite_enabled: bool = None,
        schema: str = None,
        size: int = None,
        storage_handler: str = None,
        table_label: str = None,
        tablesotre_table_name: str = None,
        tablestore_columns_mapping: str = None,
        type: str = None,
        view_text: str = None,
    ):
        self.auto_refresh_enabled = auto_refresh_enabled
        self.cluster_info = cluster_info
        self.comment = comment
        self.create_table_ddl = create_table_ddl
        self.creation_time = creation_time
        self.display_name = display_name
        self.file_num = file_num
        self.is_external_table = is_external_table
        self.is_outdated = is_outdated
        self.last_access_time = last_access_time
        self.last_ddltime = last_ddltime
        self.last_modified_time = last_modified_time
        self.lifecycle = lifecycle
        self.location = location
        self.materialized_view = materialized_view
        self.name = name
        self.native_columns = native_columns
        self.odps_properties_rolearn = odps_properties_rolearn
        self.odps_sql_text_option_flush_header = odps_sql_text_option_flush_header
        self.odps_text_option_header_lines_count = odps_text_option_header_lines_count
        self.owner = owner
        self.partition_columns = partition_columns
        self.physical_size = physical_size
        self.project_name = project_name
        self.rewrite_enabled = rewrite_enabled
        self.schema = schema
        self.size = size
        self.storage_handler = storage_handler
        self.table_label = table_label
        self.tablesotre_table_name = tablesotre_table_name
        self.tablestore_columns_mapping = tablestore_columns_mapping
        self.type = type
        self.view_text = view_text

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()
        if self.native_columns:
            for v1 in self.native_columns:
                 if v1:
                    v1.validate()
        if self.partition_columns:
            for v1 in self.partition_columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_refresh_enabled is not None:
            result['autoRefreshEnabled'] = self.auto_refresh_enabled

        if self.cluster_info is not None:
            result['clusterInfo'] = self.cluster_info.to_map()

        if self.comment is not None:
            result['comment'] = self.comment

        if self.create_table_ddl is not None:
            result['createTableDDL'] = self.create_table_ddl

        if self.creation_time is not None:
            result['creationTime'] = self.creation_time

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.file_num is not None:
            result['fileNum'] = self.file_num

        if self.is_external_table is not None:
            result['isExternalTable'] = self.is_external_table

        if self.is_outdated is not None:
            result['isOutdated'] = self.is_outdated

        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time

        if self.last_ddltime is not None:
            result['lastDDLTime'] = self.last_ddltime

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.lifecycle is not None:
            result['lifecycle'] = self.lifecycle

        if self.location is not None:
            result['location'] = self.location

        if self.materialized_view is not None:
            result['materializedView'] = self.materialized_view

        if self.name is not None:
            result['name'] = self.name

        result['nativeColumns'] = []
        if self.native_columns is not None:
            for k1 in self.native_columns:
                result['nativeColumns'].append(k1.to_map() if k1 else None)

        if self.odps_properties_rolearn is not None:
            result['odpsPropertiesRolearn'] = self.odps_properties_rolearn

        if self.odps_sql_text_option_flush_header is not None:
            result['odpsSqlTextOptionFlushHeader'] = self.odps_sql_text_option_flush_header

        if self.odps_text_option_header_lines_count is not None:
            result['odpsTextOptionHeaderLinesCount'] = self.odps_text_option_header_lines_count

        if self.owner is not None:
            result['owner'] = self.owner

        result['partitionColumns'] = []
        if self.partition_columns is not None:
            for k1 in self.partition_columns:
                result['partitionColumns'].append(k1.to_map() if k1 else None)

        if self.physical_size is not None:
            result['physicalSize'] = self.physical_size

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.rewrite_enabled is not None:
            result['rewriteEnabled'] = self.rewrite_enabled

        if self.schema is not None:
            result['schema'] = self.schema

        if self.size is not None:
            result['size'] = self.size

        if self.storage_handler is not None:
            result['storageHandler'] = self.storage_handler

        if self.table_label is not None:
            result['tableLabel'] = self.table_label

        if self.tablesotre_table_name is not None:
            result['tablesotreTableName'] = self.tablesotre_table_name

        if self.tablestore_columns_mapping is not None:
            result['tablestoreColumnsMapping'] = self.tablestore_columns_mapping

        if self.type is not None:
            result['type'] = self.type

        if self.view_text is not None:
            result['viewText'] = self.view_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRefreshEnabled') is not None:
            self.auto_refresh_enabled = m.get('autoRefreshEnabled')

        if m.get('clusterInfo') is not None:
            temp_model = main_models.GetTableInfoResponseBodyDataClusterInfo()
            self.cluster_info = temp_model.from_map(m.get('clusterInfo'))

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('createTableDDL') is not None:
            self.create_table_ddl = m.get('createTableDDL')

        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')

        if m.get('isExternalTable') is not None:
            self.is_external_table = m.get('isExternalTable')

        if m.get('isOutdated') is not None:
            self.is_outdated = m.get('isOutdated')

        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')

        if m.get('lastDDLTime') is not None:
            self.last_ddltime = m.get('lastDDLTime')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('lifecycle') is not None:
            self.lifecycle = m.get('lifecycle')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('materializedView') is not None:
            self.materialized_view = m.get('materializedView')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.native_columns = []
        if m.get('nativeColumns') is not None:
            for k1 in m.get('nativeColumns'):
                temp_model = main_models.GetTableInfoResponseBodyDataNativeColumns()
                self.native_columns.append(temp_model.from_map(k1))

        if m.get('odpsPropertiesRolearn') is not None:
            self.odps_properties_rolearn = m.get('odpsPropertiesRolearn')

        if m.get('odpsSqlTextOptionFlushHeader') is not None:
            self.odps_sql_text_option_flush_header = m.get('odpsSqlTextOptionFlushHeader')

        if m.get('odpsTextOptionHeaderLinesCount') is not None:
            self.odps_text_option_header_lines_count = m.get('odpsTextOptionHeaderLinesCount')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        self.partition_columns = []
        if m.get('partitionColumns') is not None:
            for k1 in m.get('partitionColumns'):
                temp_model = main_models.GetTableInfoResponseBodyDataPartitionColumns()
                self.partition_columns.append(temp_model.from_map(k1))

        if m.get('physicalSize') is not None:
            self.physical_size = m.get('physicalSize')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('rewriteEnabled') is not None:
            self.rewrite_enabled = m.get('rewriteEnabled')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('storageHandler') is not None:
            self.storage_handler = m.get('storageHandler')

        if m.get('tableLabel') is not None:
            self.table_label = m.get('tableLabel')

        if m.get('tablesotreTableName') is not None:
            self.tablesotre_table_name = m.get('tablesotreTableName')

        if m.get('tablestoreColumnsMapping') is not None:
            self.tablestore_columns_mapping = m.get('tablestoreColumnsMapping')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('viewText') is not None:
            self.view_text = m.get('viewText')

        return self

class GetTableInfoResponseBodyDataPartitionColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.label = label
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.label is not None:
            result['label'] = self.label

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetTableInfoResponseBodyDataNativeColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.label = label
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.label is not None:
            result['label'] = self.label

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetTableInfoResponseBodyDataClusterInfo(DaraModel):
    def __init__(
        self,
        bucket_num: int = None,
        cluster_cols: List[str] = None,
        cluster_type: str = None,
        sort_cols: List[main_models.GetTableInfoResponseBodyDataClusterInfoSortCols] = None,
    ):
        self.bucket_num = bucket_num
        self.cluster_cols = cluster_cols
        self.cluster_type = cluster_type
        self.sort_cols = sort_cols

    def validate(self):
        if self.sort_cols:
            for v1 in self.sort_cols:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_num is not None:
            result['bucketNum'] = self.bucket_num

        if self.cluster_cols is not None:
            result['clusterCols'] = self.cluster_cols

        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type

        result['sortCols'] = []
        if self.sort_cols is not None:
            for k1 in self.sort_cols:
                result['sortCols'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketNum') is not None:
            self.bucket_num = m.get('bucketNum')

        if m.get('clusterCols') is not None:
            self.cluster_cols = m.get('clusterCols')

        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')

        self.sort_cols = []
        if m.get('sortCols') is not None:
            for k1 in m.get('sortCols'):
                temp_model = main_models.GetTableInfoResponseBodyDataClusterInfoSortCols()
                self.sort_cols.append(temp_model.from_map(k1))

        return self

class GetTableInfoResponseBodyDataClusterInfoSortCols(DaraModel):
    def __init__(
        self,
        name: str = None,
        order: str = None,
    ):
        self.name = name
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.order is not None:
            result['order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('order') is not None:
            self.order = m.get('order')

        return self

