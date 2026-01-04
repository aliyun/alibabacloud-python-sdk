# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUdpReflectResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        udp_sports: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array consisting of the source ports of the UDP traffic that are filtered out by the filtering policies for UDP reflection attacks.
        self.udp_sports = udp_sports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.udp_sports is not None:
            result['UdpSports'] = self.udp_sports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UdpSports') is not None:
            self.udp_sports = m.get('UdpSports')

        return self

