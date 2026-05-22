# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelServiceRegistrationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        registration_id: str = None,
    ):
        # Client token, used to ensure the idempotence of requests. Generate a unique value for this parameter from your client to ensure it is unique across different requests. ClientToken supports only ASCII characters.
        self.client_token = client_token
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Service registration ID.
        # 
        # This parameter is required.
        self.registration_id = registration_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')

        return self

