# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableTrustedOriginRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        trusted_origin_id: str = None,
    ):
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the trusted origin.
        # 
        # This parameter is required.
        self.trusted_origin_id = trusted_origin_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.trusted_origin_id is not None:
            result['TrustedOriginId'] = self.trusted_origin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TrustedOriginId') is not None:
            self.trusted_origin_id = m.get('TrustedOriginId')

        return self

