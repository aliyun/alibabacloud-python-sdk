# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class SearchMetaTablesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SearchMetaTablesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The search results.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SearchMetaTablesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchMetaTablesResponseBodyData(DaraModel):
    def __init__(
        self,
        data_entity_list: List[main_models.SearchMetaTablesResponseBodyDataDataEntityList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of metatables.
        self.data_entity_list = data_entity_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of metatables.
        self.total_count = total_count

    def validate(self):
        if self.data_entity_list:
            for v1 in self.data_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k1 in self.data_entity_list:
                result['DataEntityList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_entity_list = []
        if m.get('DataEntityList') is not None:
            for k1 in m.get('DataEntityList'):
                temp_model = main_models.SearchMetaTablesResponseBodyDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchMetaTablesResponseBodyDataDataEntityList(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        entity_type: int = None,
        env_type: int = None,
        owner_id: str = None,
        project_id: int = None,
        project_name: str = None,
        schema: str = None,
        table_guid: str = None,
        table_name: str = None,
        tenant_id: int = None,
    ):
        # The ID of the EMR cluster.
        self.cluster_id = cluster_id
        # The name of the metadatabase.
        self.database_name = database_name
        # The type of the metatable. Valid values:
        # 
        # *   0: table
        # *   1: view
        self.entity_type = entity_type
        # The type of the environment. Valid values:
        # 
        # *   1: production environment
        # *   0: development environment
        self.env_type = env_type
        # The ID of the Alibaba Cloud account used by the workspace owner.
        self.owner_id = owner_id
        # The ID of the workspace.
        self.project_id = project_id
        # The name of the workspace.
        self.project_name = project_name
        # The schema information of the table. You must configure this parameter if you enable the three-layer model of MaxCompute.
        self.schema = schema
        # The GUID of the metatable.
        self.table_guid = table_guid
        # The name of the metatable.
        self.table_name = table_name
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

