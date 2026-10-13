# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListMetaProfilingResultUdfPageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMetaProfilingResultUdfPageResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.page_index = page_index
        self.page_size = page_size
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
                temp_model = main_models.ListMetaProfilingResultUdfPageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMetaProfilingResultUdfPageResponseBodyData(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        class_name: str = None,
        db_name: str = None,
        ds_type: str = None,
        func_comment: str = None,
        func_crt_time: str = None,
        func_id: str = None,
        func_mod_time: str = None,
        func_name: str = None,
        func_type: str = None,
        id: int = None,
        migration_status: str = None,
        owner: str = None,
        resource_location: str = None,
        resource_type: str = None,
        tenant_id: str = None,
    ):
        self.catalog_name = catalog_name
        self.class_name = class_name
        self.db_name = db_name
        self.ds_type = ds_type
        self.func_comment = func_comment
        self.func_crt_time = func_crt_time
        self.func_id = func_id
        self.func_mod_time = func_mod_time
        self.func_name = func_name
        self.func_type = func_type
        self.id = id
        self.migration_status = migration_status
        self.owner = owner
        self.resource_location = resource_location
        self.resource_type = resource_type
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name

        if self.class_name is not None:
            result['className'] = self.class_name

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.func_comment is not None:
            result['funcComment'] = self.func_comment

        if self.func_crt_time is not None:
            result['funcCrtTime'] = self.func_crt_time

        if self.func_id is not None:
            result['funcId'] = self.func_id

        if self.func_mod_time is not None:
            result['funcModTime'] = self.func_mod_time

        if self.func_name is not None:
            result['funcName'] = self.func_name

        if self.func_type is not None:
            result['funcType'] = self.func_type

        if self.id is not None:
            result['id'] = self.id

        if self.migration_status is not None:
            result['migrationStatus'] = self.migration_status

        if self.owner is not None:
            result['owner'] = self.owner

        if self.resource_location is not None:
            result['resourceLocation'] = self.resource_location

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')

        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('funcComment') is not None:
            self.func_comment = m.get('funcComment')

        if m.get('funcCrtTime') is not None:
            self.func_crt_time = m.get('funcCrtTime')

        if m.get('funcId') is not None:
            self.func_id = m.get('funcId')

        if m.get('funcModTime') is not None:
            self.func_mod_time = m.get('funcModTime')

        if m.get('funcName') is not None:
            self.func_name = m.get('funcName')

        if m.get('funcType') is not None:
            self.func_type = m.get('funcType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('migrationStatus') is not None:
            self.migration_status = m.get('migrationStatus')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('resourceLocation') is not None:
            self.resource_location = m.get('resourceLocation')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

