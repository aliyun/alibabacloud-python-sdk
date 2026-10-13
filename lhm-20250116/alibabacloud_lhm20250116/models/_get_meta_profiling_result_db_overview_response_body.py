# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetMetaProfilingResultDbOverviewResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaProfilingResultDbOverviewResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data source-level metadata profiling overview object. For more information about each field, see the descriptions of the sub-fields.
        self.data = data
        # The error code. It is an empty string if the call is successful.
        self.err_code = err_code
        # The error message. It is an empty string if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues related to this call.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed. If the call fails, troubleshoot the issue based on the errCode and errMessage parameters.
        self.success = success

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

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetMetaProfilingResultDbOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetMetaProfilingResultDbOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        catalog_count: int = None,
        component_id: int = None,
        component_type: int = None,
        ds_name: str = None,
        ds_version: str = None,
        et_table_count: int = None,
        func_count: int = None,
        gmt_create: str = None,
        last_modified: str = None,
        no_pt_table_count: int = None,
        partition_count: int = None,
        pt_table_count: int = None,
        record_count: int = None,
        schema_count: int = None,
        storage_size: str = None,
        table_count: int = None,
        transactional_count: int = None,
        view_count: int = None,
    ):
        # The number of catalogs.
        self.catalog_count = catalog_count
        # The component ID, which is the primary key identifier of the data source component.
        self.component_id = component_id
        # The identifier of the data source component type.
        self.component_type = component_type
        # The name of the data source.
        self.ds_name = ds_name
        # The version of the data source.
        self.ds_version = ds_version
        # The number of external tables.
        self.et_table_count = et_table_count
        # The number of functions.
        self.func_count = func_count
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.last_modified = last_modified
        # The number of non-partitioned tables.
        self.no_pt_table_count = no_pt_table_count
        # The number of partitions.
        self.partition_count = partition_count
        # The number of partitioned tables.
        self.pt_table_count = pt_table_count
        # The number of data rows.
        self.record_count = record_count
        # The number of schemas.
        self.schema_count = schema_count
        # The data storage size.
        self.storage_size = storage_size
        # The number of tables.
        self.table_count = table_count
        # The number of transactional tables.
        self.transactional_count = transactional_count
        # The number of views.
        self.view_count = view_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_count is not None:
            result['catalogCount'] = self.catalog_count

        if self.component_id is not None:
            result['componentId'] = self.component_id

        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        if self.ds_version is not None:
            result['dsVersion'] = self.ds_version

        if self.et_table_count is not None:
            result['etTableCount'] = self.et_table_count

        if self.func_count is not None:
            result['funcCount'] = self.func_count

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.last_modified is not None:
            result['lastModified'] = self.last_modified

        if self.no_pt_table_count is not None:
            result['noPtTableCount'] = self.no_pt_table_count

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

        if self.transactional_count is not None:
            result['transactionalCount'] = self.transactional_count

        if self.view_count is not None:
            result['viewCount'] = self.view_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogCount') is not None:
            self.catalog_count = m.get('catalogCount')

        if m.get('componentId') is not None:
            self.component_id = m.get('componentId')

        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        if m.get('dsVersion') is not None:
            self.ds_version = m.get('dsVersion')

        if m.get('etTableCount') is not None:
            self.et_table_count = m.get('etTableCount')

        if m.get('funcCount') is not None:
            self.func_count = m.get('funcCount')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('lastModified') is not None:
            self.last_modified = m.get('lastModified')

        if m.get('noPtTableCount') is not None:
            self.no_pt_table_count = m.get('noPtTableCount')

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

        if m.get('transactionalCount') is not None:
            self.transactional_count = m.get('transactionalCount')

        if m.get('viewCount') is not None:
            self.view_count = m.get('viewCount')

        return self

