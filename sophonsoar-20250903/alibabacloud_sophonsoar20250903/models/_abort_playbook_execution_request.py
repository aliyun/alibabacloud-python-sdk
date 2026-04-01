# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AbortPlaybookExecutionRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        playbook_execution_uuid: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.playbook_execution_uuid = playbook_execution_uuid
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        self.role_for = role_for
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.playbook_execution_uuid is not None:
            result['PlaybookExecutionUuid'] = self.playbook_execution_uuid

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlaybookExecutionUuid') is not None:
            self.playbook_execution_uuid = m.get('PlaybookExecutionUuid')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

