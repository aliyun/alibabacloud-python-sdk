# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        kb_uuid: str = None,
        name: str = None,
    ):
        # The new knowledge base description.
        self.description = description
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.kb_uuid = kb_uuid
        # The new knowledge base name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

