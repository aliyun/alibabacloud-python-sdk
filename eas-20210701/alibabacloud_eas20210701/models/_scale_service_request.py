# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ScaleServiceRequest(DaraModel):
    def __init__(
        self,
        instance: int = None,
        instances_to_delete: List[str] = None,
    ):
        # This parameter is required.
        self.instance = instance
        self.instances_to_delete = instances_to_delete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance

        if self.instances_to_delete is not None:
            result['InstancesToDelete'] = self.instances_to_delete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

        if m.get('InstancesToDelete') is not None:
            self.instances_to_delete = m.get('InstancesToDelete')

        return self

