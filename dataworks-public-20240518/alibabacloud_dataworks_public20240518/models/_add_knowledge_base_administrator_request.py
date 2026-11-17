# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddKnowledgeBaseAdministratorRequest(DaraModel):
    def __init__(
        self,
        administrator_user_id: str = None,
        knowledge_base_id: str = None,
    ):
        # The DataWorks user ID of the administrator to be added. This is not the identity of the caller.
        # 
        # This parameter is required.
        self.administrator_user_id = administrator_user_id
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrator_user_id is not None:
            result['AdministratorUserId'] = self.administrator_user_id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdministratorUserId') is not None:
            self.administrator_user_id = m.get('AdministratorUserId')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        return self

