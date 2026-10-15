# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportApiKeyInput(DaraModel):
    def __init__(
        self,
        api_key_name: str = None,
        api_key_value: str = None,
        expire_time: str = None,
        team_id: str = None,
    ):
        # The API key name. The name can be up to 128 characters in length and can contain letters, digits, spaces, hyphens (-), underscores (_), and periods (.).
        self.api_key_name = api_key_name
        # The plaintext value of the API key to import. After the import, the source of the key is set to custom.
        self.api_key_value = api_key_value
        # The expiration time of the API key in UTC. The time is in RFC 3339 format. If this parameter is left empty, the API key never expires.
        self.expire_time = expire_time
        # The ID of the team to which the API key belongs, in UUID format. If this parameter is not specified, the default team of the current account is used.
        self.team_id = team_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.api_key_value is not None:
            result['apiKeyValue'] = self.api_key_value

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.team_id is not None:
            result['teamID'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('apiKeyValue') is not None:
            self.api_key_value = m.get('apiKeyValue')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        return self

