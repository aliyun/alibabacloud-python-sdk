# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMOQuotaAlertThresholdShrinkRequest(DaraModel):
    def __init__(
        self,
        apikey_shrink: str = None,
        instance_id: str = None,
    ):
        # A list of API keys.
        # 
        # This parameter is required.
        self.apikey_shrink = apikey_shrink
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey_shrink is not None:
            result['Apikey'] = self.apikey_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apikey') is not None:
            self.apikey_shrink = m.get('Apikey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

