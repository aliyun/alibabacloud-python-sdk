# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuthorizationTokenRequest(DaraModel):
    def __init__(
        self,
        expires_in_hours: int = None,
        instance_id: str = None,
    ):
        # The validity period of the temporary credential, in hours. Valid values: 1 to 24.
        self.expires_in_hours = expires_in_hours
        # The repository instance ID.
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
        if self.expires_in_hours is not None:
            result['ExpiresInHours'] = self.expires_in_hours

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiresInHours') is not None:
            self.expires_in_hours = m.get('ExpiresInHours')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

