# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataAgentMemoryRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        dmsunit: str = None,
        from_id: str = None,
        label: str = None,
        mem_from: str = None,
        session_uuid: str = None,
    ):
        # The memory content.
        self.content = content
        # The current DMS unit.
        self.dmsunit = dmsunit
        # The source ID.
        # - If MemFrom is set to session, FromId indicates the session ID.
        # - If MemFrom is set to user, FromId indicates the RAM user ID.
        self.from_id = from_id
        # The memory label. Valid values:
        # - fact_specifications: fact definitions.
        # - task_constraints: node constraints.
        # - execution_config: execution configuration.
        self.label = label
        # The memory source. Valid values:
        # - session: generated from a session.
        # - user: edited by a user.
        self.mem_from = mem_from
        # The session ID.
        # - Note: This parameter is deprecated.
        self.session_uuid = session_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.from_id is not None:
            result['FromId'] = self.from_id

        if self.label is not None:
            result['Label'] = self.label

        if self.mem_from is not None:
            result['MemFrom'] = self.mem_from

        if self.session_uuid is not None:
            result['SessionUuid'] = self.session_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MemFrom') is not None:
            self.mem_from = m.get('MemFrom')

        if m.get('SessionUuid') is not None:
            self.session_uuid = m.get('SessionUuid')

        return self

