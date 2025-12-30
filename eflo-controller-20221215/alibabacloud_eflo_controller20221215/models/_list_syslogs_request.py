# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSyslogsRequest(DaraModel):
    def __init__(
        self,
        from_time: str = None,
        next_token: str = None,
        node_id: str = None,
        query: str = None,
        reverse: bool = None,
        to_time: str = None,
    ):
        # This parameter is required.
        self.from_time = from_time
        self.next_token = next_token
        # This parameter is required.
        self.node_id = node_id
        self.query = query
        self.reverse = reverse
        # This parameter is required.
        self.to_time = to_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['FromTime'] = self.from_time

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.query is not None:
            result['Query'] = self.query

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.to_time is not None:
            result['ToTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromTime') is not None:
            self.from_time = m.get('FromTime')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('ToTime') is not None:
            self.to_time = m.get('ToTime')

        return self

