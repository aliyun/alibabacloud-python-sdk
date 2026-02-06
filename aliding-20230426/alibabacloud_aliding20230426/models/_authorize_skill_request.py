# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeSkillRequest(DaraModel):
    def __init__(
        self,
        permission_codes: List[str] = None,
        source_id_of_assistant_id: str = None,
    ):
        self.permission_codes = permission_codes
        self.source_id_of_assistant_id = source_id_of_assistant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission_codes is not None:
            result['PermissionCodes'] = self.permission_codes

        if self.source_id_of_assistant_id is not None:
            result['SourceIdOfAssistantId'] = self.source_id_of_assistant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionCodes') is not None:
            self.permission_codes = m.get('PermissionCodes')

        if m.get('SourceIdOfAssistantId') is not None:
            self.source_id_of_assistant_id = m.get('SourceIdOfAssistantId')

        return self

