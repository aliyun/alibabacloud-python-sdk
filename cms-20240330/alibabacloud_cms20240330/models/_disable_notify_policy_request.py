# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableNotifyPolicyRequest(DaraModel):
    def __init__(
        self,
        workspace: str = None,
    ):
        # The workspace ID. Used to isolate notification policy resources across different business spaces.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

