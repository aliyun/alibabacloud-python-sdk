# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBgpGroupResponseBody(DaraModel):
    def __init__(
        self,
        bgp_group_id: str = None,
        request_id: str = None,
    ):
        # The ID of the BGP group.
        self.bgp_group_id = bgp_group_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_group_id is not None:
            result['BgpGroupId'] = self.bgp_group_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpGroupId') is not None:
            self.bgp_group_id = m.get('BgpGroupId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

