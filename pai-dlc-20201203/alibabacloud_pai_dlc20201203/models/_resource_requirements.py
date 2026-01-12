# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ResourceRequirements(DaraModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        self.limits = limits
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limits is not None:
            result['Limits'] = self.limits

        if self.requests is not None:
            result['Requests'] = self.requests

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limits') is not None:
            self.limits = m.get('Limits')

        if m.get('Requests') is not None:
            self.requests = m.get('Requests')

        return self

