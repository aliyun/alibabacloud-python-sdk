# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeColdStorageInstanceResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        object_type: str = None,
        oss_cluster_enabled: str = None,
        oss_cluster_info_list: List[main_models.DescribeColdStorageInstanceResponseBodyOssClusterInfoList] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        support_oss_cluster: str = None,
        tables: List[main_models.DescribeColdStorageInstanceResponseBodyTables] = None,
        total_record: int = None,
    ):
        # The maximum number of entries returned. Default value: 10.
        self.max_results = max_results
        # The token to retrieve the next page of results. If this parameter is not returned, all results have been returned.
        self.next_token = next_token
        # The object type.
        self.object_type = object_type
        # Indicates whether the OSS bucket is enabled.
        # 
        # - **true**: enabled
        # 
        # - **false**: disabled
        self.oss_cluster_enabled = oss_cluster_enabled
        # The list of OSS addresses for the cold storage instances.
        self.oss_cluster_info_list = oss_cluster_info_list
        # The page number.
        self.page_number = page_number
        # The number of entries on the current page.
        self.page_record_count = page_record_count
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the cluster supports cold storage. If the cluster does not support cold storage, the switch is not displayed on the console.
        self.support_oss_cluster = support_oss_cluster
        # The list of cold storage instances.
        self.tables = tables
        # The total number of entries.
        self.total_record = total_record

    def validate(self):
        if self.oss_cluster_info_list:
            for v1 in self.oss_cluster_info_list:
                 if v1:
                    v1.validate()
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.oss_cluster_enabled is not None:
            result['OssClusterEnabled'] = self.oss_cluster_enabled

        result['OssClusterInfoList'] = []
        if self.oss_cluster_info_list is not None:
            for k1 in self.oss_cluster_info_list:
                result['OssClusterInfoList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_oss_cluster is not None:
            result['SupportOssCluster'] = self.support_oss_cluster

        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        if self.total_record is not None:
            result['TotalRecord'] = self.total_record

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OssClusterEnabled') is not None:
            self.oss_cluster_enabled = m.get('OssClusterEnabled')

        self.oss_cluster_info_list = []
        if m.get('OssClusterInfoList') is not None:
            for k1 in m.get('OssClusterInfoList'):
                temp_model = main_models.DescribeColdStorageInstanceResponseBodyOssClusterInfoList()
                self.oss_cluster_info_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportOssCluster') is not None:
            self.support_oss_cluster = m.get('SupportOssCluster')

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.DescribeColdStorageInstanceResponseBodyTables()
                self.tables.append(temp_model.from_map(k1))

        if m.get('TotalRecord') is not None:
            self.total_record = m.get('TotalRecord')

        return self

class DescribeColdStorageInstanceResponseBodyTables(DaraModel):
    def __init__(
        self,
        child_objects: List[main_models.DescribeColdStorageInstanceResponseBodyTablesChildObjects] = None,
        db: str = None,
        dbname: str = None,
        field_name: str = None,
        oss_cluster_id: str = None,
        partion: str = None,
        size: str = None,
        status: str = None,
        table: str = None,
        table_name: str = None,
    ):
        # The list of child objects.
        self.child_objects = child_objects
        # The database name.
        self.db = db
        # The database name.
        self.dbname = dbname
        # The name of the large object (LOB) field.
        self.field_name = field_name
        # The ID of the OSS-based cluster.
        self.oss_cluster_id = oss_cluster_id
        # The partition of the cold storage instance.
        self.partion = partion
        # The disk size of the cold storage instance. Unit: GiB.
        self.size = size
        # The status of the task.
        self.status = status
        # The table name.
        self.table = table
        # The table name.
        self.table_name = table_name

    def validate(self):
        if self.child_objects:
            for v1 in self.child_objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChildObjects'] = []
        if self.child_objects is not None:
            for k1 in self.child_objects:
                result['ChildObjects'].append(k1.to_map() if k1 else None)

        if self.db is not None:
            result['DB'] = self.db

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.oss_cluster_id is not None:
            result['OssClusterId'] = self.oss_cluster_id

        if self.partion is not None:
            result['Partion'] = self.partion

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.table is not None:
            result['Table'] = self.table

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_objects = []
        if m.get('ChildObjects') is not None:
            for k1 in m.get('ChildObjects'):
                temp_model = main_models.DescribeColdStorageInstanceResponseBodyTablesChildObjects()
                self.child_objects.append(temp_model.from_map(k1))

        if m.get('DB') is not None:
            self.db = m.get('DB')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('OssClusterId') is not None:
            self.oss_cluster_id = m.get('OssClusterId')

        if m.get('Partion') is not None:
            self.partion = m.get('Partion')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeColdStorageInstanceResponseBodyTablesChildObjects(DaraModel):
    def __init__(
        self,
        object_name: str = None,
        object_type: str = None,
        size: str = None,
        status: str = None,
    ):
        # The object name.
        self.object_name = object_name
        # The object type.
        self.object_type = object_type
        # The disk size. Unit: GiB.
        self.size = size
        # The status of the task. Valid values:
        # 
        # - **Scheduled**: The task is waiting to be executed.
        # 
        # - **Running**: The task is in progress.
        # 
        # - **Succeed**: The task is successful.
        # 
        # - **Cancelling**: The task is being stopped.
        # 
        # - **Canceled**: The task is stopped.
        # 
        # - **Waiting**: The task is waiting for a preset time.
        # 
        # To query multiple statuses, separate them with commas (,). If you do not specify this parameter, all statuses are queried.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeColdStorageInstanceResponseBodyOssClusterInfoList(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        oss_cluster_id: str = None,
        region: str = None,
        size: str = None,
    ):
        # The time when the cluster was created.
        self.created_time = created_time
        # The ID of the cold storage instance.
        self.oss_cluster_id = oss_cluster_id
        # The ID of the region where the task is located.
        self.region = region
        # The size of the cold storage table. Unit: GB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.oss_cluster_id is not None:
            result['OssClusterId'] = self.oss_cluster_id

        if self.region is not None:
            result['Region'] = self.region

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('OssClusterId') is not None:
            self.oss_cluster_id = m.get('OssClusterId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

