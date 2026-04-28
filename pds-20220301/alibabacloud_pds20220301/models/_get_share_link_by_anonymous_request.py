# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetShareLinkByAnonymousRequest(DaraModel):
    def __init__(
        self,
        share_id: str = None,
    ):
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.share_id is not None:
            result['share_id'] = self.share_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        return self

