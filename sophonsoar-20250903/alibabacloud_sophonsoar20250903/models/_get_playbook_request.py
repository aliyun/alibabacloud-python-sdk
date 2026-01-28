# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPlaybookRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
        playbook_version: str = None,
        playbook_version_type: str = None,
        role_for: int = None,
    ):
        # The language type for requests and received messages.
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The version ID of the playbook, which is only effective when **PlaybookVersionType** is **History**.
        self.playbook_version = playbook_version
        # The version type of the playbook, with the following values:
        # 
        # - **Draft**: Editing state.
        # - **Online**: Online version.
        # - **History**: Historical version.
        self.playbook_version_type = playbook_version_type
        # The user ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.playbook_version is not None:
            result['PlaybookVersion'] = self.playbook_version

        if self.playbook_version_type is not None:
            result['PlaybookVersionType'] = self.playbook_version_type

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('PlaybookVersion') is not None:
            self.playbook_version = m.get('PlaybookVersion')

        if m.get('PlaybookVersionType') is not None:
            self.playbook_version_type = m.get('PlaybookVersionType')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

