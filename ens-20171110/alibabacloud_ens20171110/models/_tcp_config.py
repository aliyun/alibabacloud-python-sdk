# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TcpConfig(DaraModel):
    def __init__(
        self,
        established_timeout: int = None,
        persistence_timeout: int = None,
        scheduler: str = None,
    ):
        self.established_timeout = established_timeout
        self.persistence_timeout = persistence_timeout
        self.scheduler = scheduler

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        return self

