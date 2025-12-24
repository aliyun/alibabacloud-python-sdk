# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePortRangeListResponseBody(DaraModel):
    def __init__(
        self,
        port_range_list_id: str = None,
        request_id: str = None,
    ):
        # The ID of the port list.
        self.port_range_list_id = port_range_list_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port_range_list_id is not None:
            result['PortRangeListId'] = self.port_range_list_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortRangeListId') is not None:
            self.port_range_list_id = m.get('PortRangeListId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

