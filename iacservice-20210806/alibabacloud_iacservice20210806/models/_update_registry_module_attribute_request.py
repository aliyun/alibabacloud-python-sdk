# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRegistryModuleAttributeRequest(DaraModel):
    def __init__(
        self,
        acl: str = None,
        client_token: str = None,
        description: str = None,
    ):
        # The access permission. Valid values:
        # 
        # - private: private.
        self.acl = acl
        # The idempotence token. Format: [0-9a-zA-Z-]{1,64}. Use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the Registry template.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

