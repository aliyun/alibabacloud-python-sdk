# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSkillScopeRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        scope: str = None,
        skill_name: str = None,
    ):
        # This parameter is required.
        self.namespace_id = namespace_id
        # This parameter is required.
        self.scope = scope
        # This parameter is required.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

