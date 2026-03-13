# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyPlaybookRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        lang: str = None,
        release_version: str = None,
        role_for: int = None,
        role_type: str = None,
        source_playbook_uuid: str = None,
    ):
        # The description of the playbook.
        self.description = description
        # The display name of the playbook.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default).
        # *   **en**: English.
        self.lang = lang
        # The release version of the playbook that you want to copy. Default value: 0. Valid values:
        # 
        # *   \\-1: The version that is being edited.
        # *   0: The latest online version of the current playbook.
        self.release_version = release_version
        # The ID of the user who switches from the current view to the destination view by using the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # 
        # *   **0** (default): the view of the current account.
        # *   **1**: the view of the global account.
        self.role_type = role_type
        # The UUID of the playbook that you want to copy.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.source_playbook_uuid = source_playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.source_playbook_uuid is not None:
            result['SourcePlaybookUuid'] = self.source_playbook_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('SourcePlaybookUuid') is not None:
            self.source_playbook_uuid = m.get('SourcePlaybookUuid')

        return self

