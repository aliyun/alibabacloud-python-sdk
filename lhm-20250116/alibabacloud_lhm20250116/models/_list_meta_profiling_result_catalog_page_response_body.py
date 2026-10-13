# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListMetaProfilingResultCatalogPageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMetaProfilingResultCatalogPageResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
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
                temp_model = main_models.ListMetaProfilingResultCatalogPageResponseBodyData()
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

class ListMetaProfilingResultCatalogPageResponseBodyData(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        created: str = None,
        job_id: int = None,
        last_modified: str = None,
        meta_datasource_id: int = None,
        meta_datasource_type: str = None,
        migration_progress: float = None,
        migration_status: str = None,
        partition_count: int = None,
        pt_table_count: int = None,
        record_count: int = None,
        schema_count: int = None,
        storage_size: str = None,
        table_count: int = None,
        view_count: int = None,
    ):
        self.catalog_name = catalog_name
        self.created = created
        self.job_id = job_id
        self.last_modified = last_modified
        self.meta_datasource_id = meta_datasource_id
        self.meta_datasource_type = meta_datasource_type
        self.migration_progress = migration_progress
        self.migration_status = migration_status
        self.partition_count = partition_count
        self.pt_table_count = pt_table_count
        self.record_count = record_count
        self.schema_count = schema_count
        self.storage_size = storage_size
        self.table_count = table_count
        self.view_count = view_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name

        if self.created is not None:
            result['created'] = self.created

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.last_modified is not None:
            result['lastModified'] = self.last_modified

        if self.meta_datasource_id is not None:
            result['metaDatasourceId'] = self.meta_datasource_id

        if self.meta_datasource_type is not None:
            result['metaDatasourceType'] = self.meta_datasource_type

        if self.migration_progress is not None:
            result['migrationProgress'] = self.migration_progress

        if self.migration_status is not None:
            result['migrationStatus'] = self.migration_status

        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count

        if self.pt_table_count is not None:
            result['ptTableCount'] = self.pt_table_count

        if self.record_count is not None:
            result['recordCount'] = self.record_count

        if self.schema_count is not None:
            result['schemaCount'] = self.schema_count

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        if self.table_count is not None:
            result['tableCount'] = self.table_count

        if self.view_count is not None:
            result['viewCount'] = self.view_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('lastModified') is not None:
            self.last_modified = m.get('lastModified')

        if m.get('metaDatasourceId') is not None:
            self.meta_datasource_id = m.get('metaDatasourceId')

        if m.get('metaDatasourceType') is not None:
            self.meta_datasource_type = m.get('metaDatasourceType')

        if m.get('migrationProgress') is not None:
            self.migration_progress = m.get('migrationProgress')

        if m.get('migrationStatus') is not None:
            self.migration_status = m.get('migrationStatus')

        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')

        if m.get('ptTableCount') is not None:
            self.pt_table_count = m.get('ptTableCount')

        if m.get('recordCount') is not None:
            self.record_count = m.get('recordCount')

        if m.get('schemaCount') is not None:
            self.schema_count = m.get('schemaCount')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        if m.get('tableCount') is not None:
            self.table_count = m.get('tableCount')

        if m.get('viewCount') is not None:
            self.view_count = m.get('viewCount')

        return self

