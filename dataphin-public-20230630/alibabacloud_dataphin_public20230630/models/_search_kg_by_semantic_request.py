# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SearchKgBySemanticRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        search_command: main_models.SearchKgBySemanticRequestSearchCommand = None,
        workspace_id: str = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The search command.
        # 
        # This parameter is required.
        self.search_command = search_command
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.search_command:
            self.search_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.search_command is not None:
            result['SearchCommand'] = self.search_command.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SearchCommand') is not None:
            temp_model = main_models.SearchKgBySemanticRequestSearchCommand()
            self.search_command = temp_model.from_map(m.get('SearchCommand'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class SearchKgBySemanticRequestSearchCommand(DaraModel):
    def __init__(
        self,
        entity_type_codes: List[str] = None,
        min_similarity: float = None,
        property_code: str = None,
        query_text: str = None,
        top_k: int = None,
    ):
        # The entity type codes used for filtering. If this parameter is not specified, all entity types are searched.
        self.entity_type_codes = entity_type_codes
        # The minimum similarity threshold. Valid values: 0.0 to 1.0. Default value: 0.0 (no filtering). This parameter takes effect only for the semantic search path.
        self.min_similarity = min_similarity
        # The property code for semantic search. If this parameter is not specified, all properties with semantic search enabled are searched.
        self.property_code = property_code
        # The natural language query text. The value can be 0 to 500 characters in length.
        # 
        # This parameter is required.
        self.query_text = query_text
        # The maximum number of results to return. Default value: 20. Valid values: 1 to 100.
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type_codes is not None:
            result['EntityTypeCodes'] = self.entity_type_codes

        if self.min_similarity is not None:
            result['MinSimilarity'] = self.min_similarity

        if self.property_code is not None:
            result['PropertyCode'] = self.property_code

        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityTypeCodes') is not None:
            self.entity_type_codes = m.get('EntityTypeCodes')

        if m.get('MinSimilarity') is not None:
            self.min_similarity = m.get('MinSimilarity')

        if m.get('PropertyCode') is not None:
            self.property_code = m.get('PropertyCode')

        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

