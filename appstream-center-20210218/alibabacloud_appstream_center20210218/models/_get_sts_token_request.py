# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStsTokenRequest(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        expiration: int = None,
        external_id: str = None,
    ):
        self.end_user_id = end_user_id
        self.expiration = expiration
        self.external_id = external_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.external_id is not None:
            result['ExternalId'] = self.external_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')

        return self

