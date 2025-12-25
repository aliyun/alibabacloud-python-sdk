# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEnvironmentRequest(DaraModel):
    def __init__(
        self,
        with_statistics: bool = None,
        with_vpc_info: bool = None,
    ):
        # Indicates whether to return online resource info.
        self.with_statistics = with_statistics
        # Option for vpc info.
        self.with_vpc_info = with_vpc_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.with_statistics is not None:
            result['withStatistics'] = self.with_statistics

        if self.with_vpc_info is not None:
            result['withVpcInfo'] = self.with_vpc_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withStatistics') is not None:
            self.with_statistics = m.get('withStatistics')

        if m.get('withVpcInfo') is not None:
            self.with_vpc_info = m.get('withVpcInfo')

        return self

