# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentConversationShareScopeRequest(DaraModel):
    def __init__(
        self,
        share_scope: str = None,
    ):
        # This parameter is required.
        self.share_scope = share_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.share_scope is not None:
            result['shareScope'] = self.share_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareScope') is not None:
            self.share_scope = m.get('shareScope')

        return self

