# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantKnowledgeBaseRetrievalRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The DataWorks user ID of the target user. This is not the RAM UID or the caller identity.
        # 
        # This parameter is required.
        self.principal_id = principal_id
        # The type of the principal that receives the share. This parameter is optional and defaults to USER. Currently, only USER is supported.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

