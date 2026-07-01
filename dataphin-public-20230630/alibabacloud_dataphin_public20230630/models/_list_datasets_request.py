# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDatasetsRequest(DaraModel):
    def __init__(
        self,
        dataset_query: main_models.ListDatasetsRequestDatasetQuery = None,
        op_tenant_id: int = None,
    ):
        # The request body.
        self.dataset_query = dataset_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.dataset_query:
            self.dataset_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_query is not None:
            result['DatasetQuery'] = self.dataset_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetQuery') is not None:
            temp_model = main_models.ListDatasetsRequestDatasetQuery()
            self.dataset_query = temp_model.from_map(m.get('DatasetQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListDatasetsRequestDatasetQuery(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        data_unit: str = None,
        include_version_list: bool = None,
        keyword: str = None,
        owner: str = None,
        page: int = None,
        page_size: int = None,
        project_id: int = None,
        scenario: str = None,
        storage_type: str = None,
        tenant_id: int = None,
        type_list: List[str] = None,
    ):
        # The content type.
        self.content_type = content_type
        # The data domain ID.
        self.data_unit = data_unit
        # Specifies whether to include version details. Default value: FALSE.
        self.include_version_list = include_version_list
        # The keyword.
        self.keyword = keyword
        # The owner ID.
        self.owner = owner
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The dataset scenario. Valid values:
        # - OFFLINE: offline.
        # - REALTIME: real-time.
        self.scenario = scenario
        # The storage type.
        self.storage_type = storage_type
        # The tenant ID.
        self.tenant_id = tenant_id
        # The dataset type. If left empty, all types are queried.
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.data_unit is not None:
            result['DataUnit'] = self.data_unit

        if self.include_version_list is not None:
            result['IncludeVersionList'] = self.include_version_list

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type_list is not None:
            result['TypeList'] = self.type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DataUnit') is not None:
            self.data_unit = m.get('DataUnit')

        if m.get('IncludeVersionList') is not None:
            self.include_version_list = m.get('IncludeVersionList')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')

        return self

