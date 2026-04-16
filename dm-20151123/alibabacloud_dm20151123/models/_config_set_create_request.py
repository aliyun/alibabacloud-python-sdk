# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigSetCreateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip_pool_id: str = None,
        is_public_channel_backoff: bool = None,
        name: str = None,
    ):
        self.description = description
        self.ip_pool_id = ip_pool_id
        self.is_public_channel_backoff = is_public_channel_backoff
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.is_public_channel_backoff is not None:
            result['IsPublicChannelBackoff'] = self.is_public_channel_backoff

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('IsPublicChannelBackoff') is not None:
            self.is_public_channel_backoff = m.get('IsPublicChannelBackoff')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

