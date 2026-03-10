# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHighlightTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        edit_shrink: str = None,
        highlight_shrink: str = None,
        mode: str = None,
        notification_shrink: str = None,
        output_shrink: str = None,
        project_name: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        type: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.edit_shrink = edit_shrink
        self.highlight_shrink = highlight_shrink
        self.mode = mode
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.output_shrink = output_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.type = type
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.edit_shrink is not None:
            result['Edit'] = self.edit_shrink

        if self.highlight_shrink is not None:
            result['Highlight'] = self.highlight_shrink

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.output_shrink is not None:
            result['Output'] = self.output_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.type is not None:
            result['Type'] = self.type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('Edit') is not None:
            self.edit_shrink = m.get('Edit')

        if m.get('Highlight') is not None:
            self.highlight_shrink = m.get('Highlight')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('Output') is not None:
            self.output_shrink = m.get('Output')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

