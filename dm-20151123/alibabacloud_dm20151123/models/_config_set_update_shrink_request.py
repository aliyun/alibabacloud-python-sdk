# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigSetUpdateShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        ip_pool_id: str = None,
        is_public_channel_backoff: bool = None,
        name: str = None,
        validation_option_shrink: str = None,
    ):
        # The description. Maximum length: 50 characters.
        self.description = description
        # The configuration set ID. This parameter is required.
        self.id = id
        # The associated IP pool ID. This parameter is optional.
        self.ip_pool_id = ip_pool_id
        self.is_public_channel_backoff = is_public_channel_backoff
        # The configuration name. This parameter is required. Maximum length: 50 characters. The name must be unique.
        self.name = name
        self.validation_option_shrink = validation_option_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.is_public_channel_backoff is not None:
            result['IsPublicChannelBackoff'] = self.is_public_channel_backoff

        if self.name is not None:
            result['Name'] = self.name

        if self.validation_option_shrink is not None:
            result['ValidationOption'] = self.validation_option_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('IsPublicChannelBackoff') is not None:
            self.is_public_channel_backoff = m.get('IsPublicChannelBackoff')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ValidationOption') is not None:
            self.validation_option_shrink = m.get('ValidationOption')

        return self

