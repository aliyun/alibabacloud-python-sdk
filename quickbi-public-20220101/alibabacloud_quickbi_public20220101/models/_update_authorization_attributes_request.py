# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuthorizationAttributesRequest(DaraModel):
    def __init__(
        self,
        edit_permission_type: int = None,
        resource_id: str = None,
        resource_type: str = None,
        use_permission_type: int = None,
    ):
        # The edit permission type. Valid values:
        # 
        # - 0: Private.
        # - 11: All workspace members except guests. For data forms, datasets, and data sources, this value indicates all workspace developers.
        # - 12: Specified members. For data forms, datasets, and data sources, this value indicates specified developers.
        self.edit_permission_type = edit_permission_type
        # The ID of the resource to modify.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - dashboard: dashboard.
        # - screen: data visualization.
        # - report: workbook.
        # - ANALYSIS: ad hoc analysis.
        # - dashboardOfflineQuery: self-service data retrieval.
        # - dataForm: data form.
        # - cube: dataset.
        # - datasource: data source.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The usage permission type for datasets and data sources. Valid values:
        # 
        # - 1: All workspace members except guests.
        # - 2: Specified members.
        self.use_permission_type = use_permission_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edit_permission_type is not None:
            result['EditPermissionType'] = self.edit_permission_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.use_permission_type is not None:
            result['UsePermissionType'] = self.use_permission_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditPermissionType') is not None:
            self.edit_permission_type = m.get('EditPermissionType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UsePermissionType') is not None:
            self.use_permission_type = m.get('UsePermissionType')

        return self

