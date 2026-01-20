# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteResourceShareRequest(DaraModel):
    def __init__(
        self,
        resource_share_id: str = None,
    ):
        # The ID of the resource share.
        # 
        # This parameter is required.
        self.resource_share_id = resource_share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        return self

