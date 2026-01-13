# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListCatalogsResponseBody(DaraModel):
    def __init__(
        self,
        catalogs: List[main_models.ListCatalogsResponseBodyCatalogs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.catalogs = catalogs
        # 一次获取的最大记录数。
        self.max_results = max_results
        # 下一页TOKEN。
        self.next_token = next_token
        # 请求ID。
        self.request_id = request_id
        # 记录总数。
        self.total_count = total_count

    def validate(self):
        if self.catalogs:
            for v1 in self.catalogs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['catalogs'] = []
        if self.catalogs is not None:
            for k1 in self.catalogs:
                result['catalogs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.catalogs = []
        if m.get('catalogs') is not None:
            for k1 in m.get('catalogs'):
                temp_model = main_models.ListCatalogsResponseBodyCatalogs()
                self.catalogs.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListCatalogsResponseBodyCatalogs(DaraModel):
    def __init__(
        self,
        alias: str = None,
        catalog_id: str = None,
        catalog_provider: str = None,
        catalog_type: str = None,
        environments: List[str] = None,
        extras: Dict[str, str] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        resource_owner_id: str = None,
        workspace_id: str = None,
    ):
        self.alias = alias
        # regionId。
        self.catalog_id = catalog_id
        self.catalog_provider = catalog_provider
        self.catalog_type = catalog_type
        self.environments = environments
        self.extras = extras
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.resource_owner_id = resource_owner_id
        # 工作空间id。
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        if self.catalog_provider is not None:
            result['catalogProvider'] = self.catalog_provider

        if self.catalog_type is not None:
            result['catalogType'] = self.catalog_type

        if self.environments is not None:
            result['environments'] = self.environments

        if self.extras is not None:
            result['extras'] = self.extras

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.resource_owner_id is not None:
            result['resourceOwnerId'] = self.resource_owner_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        if m.get('catalogProvider') is not None:
            self.catalog_provider = m.get('catalogProvider')

        if m.get('catalogType') is not None:
            self.catalog_type = m.get('catalogType')

        if m.get('environments') is not None:
            self.environments = m.get('environments')

        if m.get('extras') is not None:
            self.extras = m.get('extras')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('resourceOwnerId') is not None:
            self.resource_owner_id = m.get('resourceOwnerId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

