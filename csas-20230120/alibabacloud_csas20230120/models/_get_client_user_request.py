# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClientUserRequest(DaraModel):
    def __init__(
        self,
        idp_config_id: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.idp_config_id = idp_config_id
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

