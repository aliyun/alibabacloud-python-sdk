# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProjectRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        recycle_bin_enabled: bool = None,
    ):
        # The description of the project. The default value is an empty string.
        # 
        # This parameter is required.
        self.description = description
        # Specifies whether to enable the recycle bin feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.recycle_bin_enabled = recycle_bin_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.recycle_bin_enabled is not None:
            result['recycleBinEnabled'] = self.recycle_bin_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('recycleBinEnabled') is not None:
            self.recycle_bin_enabled = m.get('recycleBinEnabled')

        return self

