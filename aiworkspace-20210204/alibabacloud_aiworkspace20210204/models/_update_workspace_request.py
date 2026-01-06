# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
    ):
        # The workspace description.
        self.description = description
        # The display name of the workspace.
        # 
        # *   The name must be 3 to 23 characters in length, and can contain letters, underscores (_), and digits.
        # *   The name must start with a letter.
        # *   The name must be unique in the current region.
        self.display_name = display_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        return self

