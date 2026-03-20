# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceInstanceTokenRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        worker_name: str = None,
    ):
        self.action_type = action_type
        self.worker_name = worker_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.worker_name is not None:
            result['WorkerName'] = self.worker_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('WorkerName') is not None:
            self.worker_name = m.get('WorkerName')

        return self

