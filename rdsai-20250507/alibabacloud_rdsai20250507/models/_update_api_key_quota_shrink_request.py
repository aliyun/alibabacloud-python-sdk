# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApiKeyQuotaShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        keys_shrink: str = None,
    ):
        self.instance_id = instance_id
        self.keys_shrink = keys_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')

        return self

