# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModuleVersionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        # The idempotence token. Format: [0-9a-zA-Z-]{1,64}. Use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The version description. The description can be up to 256 characters in length.
        self.description = description
        # The template version name. The name must meet the following requirements:
        # 
        # - The name must be 2 to 128 characters in length.
        # - The name can contain letters, digits, Chinese characters, hyphens (-), underscores (_), and periods (.). The name cannot start or end with a hyphen, underscore, or period.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

