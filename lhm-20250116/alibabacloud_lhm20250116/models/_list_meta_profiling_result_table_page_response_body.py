# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListMetaProfilingResultTablePageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMetaProfilingResultTablePageResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of table profiling results. For the element structure, see the descriptions of the sub-fields.
        self.data = data
        # The error code. This parameter is an empty string if the call is successful.
        self.err_code = err_code
        # The error message. This parameter is an empty string if the call is successful.
        self.err_message = err_message
        # The current page number, starting from 1.
        self.page_index = page_index
        # The number of records to return on each page.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues of this call.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success, and a value of false indicates failure. If the call fails, troubleshoot the issue based on errCode and errMessage.
        self.success = success
        # The total number of records that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListMetaProfilingResultTablePageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMetaProfilingResultTablePageResponseBodyData(DaraModel):
    def __init__(
        self,
        average_file_size: str = None,
        average_partition_size: str = None,
        created: str = None,
        db_name: str = None,
        ds: str = None,
        engine: str = None,
        file_num: int = None,
        is_external: int = None,
        is_pt_table: int = None,
        is_transactional: int = None,
        last_accessed: str = None,
        last_modified: str = None,
        max_pt_crt_time: str = None,
        maximum_partition_list: List[str] = None,
        migration_process: float = None,
        migration_status: str = None,
        min_pt_crt_time: str = None,
        minimum_partition_list: List[str] = None,
        new_added: int = None,
        partition_field_name_list: List[str] = None,
        partition_num: int = None,
        record_count: int = None,
        storage_size: str = None,
        table_comment: str = None,
        table_id: str = None,
        table_mod_time: str = None,
        table_name: str = None,
        table_type: str = None,
    ):
        # The average file size.
        self.average_file_size = average_file_size
        # The average partition size.
        self.average_partition_size = average_partition_size
        # The creation time.
        self.created = created
        # The name of the database, which is used to filter results by database.
        self.db_name = db_name
        # The value of the data partition to which the table belongs, which identifies the partition to which this row of data belongs.
        self.ds = ds
        # The type of storage engine used by the table.
        self.engine = engine
        # The number of files.
        self.file_num = file_num
        # Indicates whether the table is an external table.
        self.is_external = is_external
        # Indicates whether the table is a partitioned table.
        self.is_pt_table = is_pt_table
        # Indicates whether the table is a transactional table.
        self.is_transactional = is_transactional
        # The last access time.
        self.last_accessed = last_accessed
        # The last modification time.
        self.last_modified = last_modified
        # The creation time of the largest partition.
        self.max_pt_crt_time = max_pt_crt_time
        # The list of largest partitions.
        self.maximum_partition_list = maximum_partition_list
        # The migration progress percentage.
        self.migration_process = migration_process
        # The migration status, which is used to filter by migration progress or indicate the migration status of an object.
        self.migration_status = migration_status
        # The creation time of the smallest partition.
        self.min_pt_crt_time = min_pt_crt_time
        # The list of smallest partitions.
        self.minimum_partition_list = minimum_partition_list
        # Indicates whether the object is newly added.
        self.new_added = new_added
        # The list of partition field names.
        self.partition_field_name_list = partition_field_name_list
        # The number of partitions.
        self.partition_num = partition_num
        # The number of data rows.
        self.record_count = record_count
        # The data storage size.
        self.storage_size = storage_size
        # The table comment or remark.
        self.table_comment = table_comment
        # The table ID.
        self.table_id = table_id
        # The last modification time of the table schema.
        self.table_mod_time = table_mod_time
        # The name of the table, which is used to filter results by table name.
        self.table_name = table_name
        # The identifier of the table type, such as managed table (MANAGED_TABLE) or external table (EXTERNAL_TABLE).
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_file_size is not None:
            result['averageFileSize'] = self.average_file_size

        if self.average_partition_size is not None:
            result['averagePartitionSize'] = self.average_partition_size

        if self.created is not None:
            result['created'] = self.created

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.ds is not None:
            result['ds'] = self.ds

        if self.engine is not None:
            result['engine'] = self.engine

        if self.file_num is not None:
            result['fileNum'] = self.file_num

        if self.is_external is not None:
            result['isExternal'] = self.is_external

        if self.is_pt_table is not None:
            result['isPtTable'] = self.is_pt_table

        if self.is_transactional is not None:
            result['isTransactional'] = self.is_transactional

        if self.last_accessed is not None:
            result['lastAccessed'] = self.last_accessed

        if self.last_modified is not None:
            result['lastModified'] = self.last_modified

        if self.max_pt_crt_time is not None:
            result['maxPtCrtTime'] = self.max_pt_crt_time

        if self.maximum_partition_list is not None:
            result['maximumPartitionList'] = self.maximum_partition_list

        if self.migration_process is not None:
            result['migrationProcess'] = self.migration_process

        if self.migration_status is not None:
            result['migrationStatus'] = self.migration_status

        if self.min_pt_crt_time is not None:
            result['minPtCrtTime'] = self.min_pt_crt_time

        if self.minimum_partition_list is not None:
            result['minimumPartitionList'] = self.minimum_partition_list

        if self.new_added is not None:
            result['newAdded'] = self.new_added

        if self.partition_field_name_list is not None:
            result['partitionFieldNameList'] = self.partition_field_name_list

        if self.partition_num is not None:
            result['partitionNum'] = self.partition_num

        if self.record_count is not None:
            result['recordCount'] = self.record_count

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        if self.table_comment is not None:
            result['tableComment'] = self.table_comment

        if self.table_id is not None:
            result['tableId'] = self.table_id

        if self.table_mod_time is not None:
            result['tableModTime'] = self.table_mod_time

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.table_type is not None:
            result['tableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('averageFileSize') is not None:
            self.average_file_size = m.get('averageFileSize')

        if m.get('averagePartitionSize') is not None:
            self.average_partition_size = m.get('averagePartitionSize')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('ds') is not None:
            self.ds = m.get('ds')

        if m.get('engine') is not None:
            self.engine = m.get('engine')

        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')

        if m.get('isExternal') is not None:
            self.is_external = m.get('isExternal')

        if m.get('isPtTable') is not None:
            self.is_pt_table = m.get('isPtTable')

        if m.get('isTransactional') is not None:
            self.is_transactional = m.get('isTransactional')

        if m.get('lastAccessed') is not None:
            self.last_accessed = m.get('lastAccessed')

        if m.get('lastModified') is not None:
            self.last_modified = m.get('lastModified')

        if m.get('maxPtCrtTime') is not None:
            self.max_pt_crt_time = m.get('maxPtCrtTime')

        if m.get('maximumPartitionList') is not None:
            self.maximum_partition_list = m.get('maximumPartitionList')

        if m.get('migrationProcess') is not None:
            self.migration_process = m.get('migrationProcess')

        if m.get('migrationStatus') is not None:
            self.migration_status = m.get('migrationStatus')

        if m.get('minPtCrtTime') is not None:
            self.min_pt_crt_time = m.get('minPtCrtTime')

        if m.get('minimumPartitionList') is not None:
            self.minimum_partition_list = m.get('minimumPartitionList')

        if m.get('newAdded') is not None:
            self.new_added = m.get('newAdded')

        if m.get('partitionFieldNameList') is not None:
            self.partition_field_name_list = m.get('partitionFieldNameList')

        if m.get('partitionNum') is not None:
            self.partition_num = m.get('partitionNum')

        if m.get('recordCount') is not None:
            self.record_count = m.get('recordCount')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        if m.get('tableComment') is not None:
            self.table_comment = m.get('tableComment')

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        if m.get('tableModTime') is not None:
            self.table_mod_time = m.get('tableModTime')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('tableType') is not None:
            self.table_type = m.get('tableType')

        return self

