# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthConfigByResourceRequest(DaraModel):
    def __init__(
        self,
        has_auth: bool = None,
        keyword: str = None,
        resource_id: str = None,
        share_to_type: int = None,
        works_type: str = None,
    ):
        # Specifies whether to query only records that have permissions.
        # 
        # This parameter is required.
        self.has_auth = has_auth
        # The search keyword for the authorized object.
        self.keyword = keyword
        # The ID of the resource to authorize.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The query granularity. Valid values:
        # 
        # - 0: user
        # - 1: user group
        # 
        # >Notice: Authorization records for organizations and workspaces are returned at the user granularity. Datasets and data sources can only be authorized to users.
        # 
        # This parameter is required.
        self.share_to_type = share_to_type
        # The type of the authorization resource. Valid values:
        # 
        # - dashboard: dashboard
        # - screen: data screen
        # - report: electron
        # - ANALYSIS: ad hoc analysis
        # - dashboardOfflineQuery: self-service data retrieval
        # - dataForm: data form
        # - cube: dataset
        # - datasource: data source
        # 
        # This parameter is required.
        self.works_type = works_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_auth is not None:
            result['HasAuth'] = self.has_auth

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasAuth') is not None:
            self.has_auth = m.get('HasAuth')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        return self

