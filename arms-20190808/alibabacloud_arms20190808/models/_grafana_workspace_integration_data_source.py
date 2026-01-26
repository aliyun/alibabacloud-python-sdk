# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GrafanaWorkspaceIntegrationDataSource(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        datasource_id: str = None,
        datasource_name: str = None,
        datasource_url: str = None,
        description: str = None,
        explore_url: str = None,
        extra: Dict[str, str] = None,
        folder_url: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.cluster_type = cluster_type
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.datasource_url = datasource_url
        self.description = description
        self.explore_url = explore_url
        self.extra = extra
        self.folder_url = folder_url
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type

        if self.datasource_id is not None:
            result['datasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['datasourceName'] = self.datasource_name

        if self.datasource_url is not None:
            result['datasourceUrl'] = self.datasource_url

        if self.description is not None:
            result['description'] = self.description

        if self.explore_url is not None:
            result['exploreUrl'] = self.explore_url

        if self.extra is not None:
            result['extra'] = self.extra

        if self.folder_url is not None:
            result['folderUrl'] = self.folder_url

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')

        if m.get('datasourceId') is not None:
            self.datasource_id = m.get('datasourceId')

        if m.get('datasourceName') is not None:
            self.datasource_name = m.get('datasourceName')

        if m.get('datasourceUrl') is not None:
            self.datasource_url = m.get('datasourceUrl')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('exploreUrl') is not None:
            self.explore_url = m.get('exploreUrl')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('folderUrl') is not None:
            self.folder_url = m.get('folderUrl')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

