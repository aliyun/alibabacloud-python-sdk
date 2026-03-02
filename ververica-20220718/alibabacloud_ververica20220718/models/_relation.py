# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Relation(DaraModel):
    def __init__(
        self,
        destination: str = None,
        job_id: str = None,
        source: str = None,
    ):
        self.destination = destination
        self.job_id = job_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination is not None:
            result['destination'] = self.destination

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

