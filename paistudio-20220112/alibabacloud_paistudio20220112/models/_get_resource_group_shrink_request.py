# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        is_aiworkspace_data_enabled: bool = None,
        tag_shrink: str = None,
    ):
        # Specifies whether to enable AI workspace data. This parameter is optional. Default value: true.
        self.is_aiworkspace_data_enabled = is_aiworkspace_data_enabled
        # The list of tags to be added. A maximum of 20 tags can be added.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_aiworkspace_data_enabled is not None:
            result['IsAIWorkspaceDataEnabled'] = self.is_aiworkspace_data_enabled

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAIWorkspaceDataEnabled') is not None:
            self.is_aiworkspace_data_enabled = m.get('IsAIWorkspaceDataEnabled')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

