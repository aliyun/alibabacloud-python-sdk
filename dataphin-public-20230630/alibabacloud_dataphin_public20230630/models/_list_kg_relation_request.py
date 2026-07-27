# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListKgRelationRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListKgRelationRequestListQuery = None,
        op_tenant_id: int = None,
        relation_type: str = None,
        workspace_id: str = None,
    ):
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.relation_type = relation_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListKgRelationRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ListKgRelationRequestListQuery(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        source_entity_id: str = None,
        target_entity_id: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.source_entity_id = source_entity_id
        self.target_entity_id = target_entity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_entity_id is not None:
            result['SourceEntityId'] = self.source_entity_id

        if self.target_entity_id is not None:
            result['TargetEntityId'] = self.target_entity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceEntityId') is not None:
            self.source_entity_id = m.get('SourceEntityId')

        if m.get('TargetEntityId') is not None:
            self.target_entity_id = m.get('TargetEntityId')

        return self

