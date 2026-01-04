# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UdpConfig(DaraModel):
    def __init__(
        self,
        hash_key: str = None,
        scheduler: str = None,
    ):
        self.hash_key = hash_key
        self.scheduler = scheduler

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        return self

