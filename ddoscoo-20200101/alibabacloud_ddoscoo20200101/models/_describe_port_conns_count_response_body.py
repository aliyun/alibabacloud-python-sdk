# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePortConnsCountResponseBody(DaraModel):
    def __init__(
        self,
        act_conns: int = None,
        conns: int = None,
        cps: int = None,
        in_act_conns: int = None,
        request_id: str = None,
    ):
        # The number of active connections.
        self.act_conns = act_conns
        # The number of concurrent connections.
        self.conns = conns
        # The number of new connections.
        self.cps = cps
        # The number of inactive connections.
        self.in_act_conns = in_act_conns
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns

        if self.conns is not None:
            result['Conns'] = self.conns

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')

        if m.get('Conns') is not None:
            self.conns = m.get('Conns')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

