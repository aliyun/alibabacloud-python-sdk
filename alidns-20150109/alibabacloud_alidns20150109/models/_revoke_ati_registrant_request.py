# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeAtiRegistrantRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        registrant_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # If you do not specify this parameter, the system automatically uses the value of RequestId as the value of ClientToken. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The ID of the real-name registrant.
        self.registrant_id = registrant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        return self

