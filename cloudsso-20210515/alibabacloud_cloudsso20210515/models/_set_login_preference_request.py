# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoginPreferenceRequest(DaraModel):
    def __init__(
        self,
        allow_user_to_get_credentials: bool = None,
        directory_id: str = None,
        login_network_masks: str = None,
    ):
        # Specifies whether to allow a user to obtain the application access credential after logon to the portal. Valid values:
        # 
        # *   True
        # *   False (default)
        self.allow_user_to_get_credentials = allow_user_to_get_credentials
        # The ID of the directory.
        self.directory_id = directory_id
        # The IP address whitelist. CloudSSO users can log on to the CloudSSO user portal only by using the IP addresses in the whitelist. Limits:
        # 
        # *   You can enter IP addresses or CIDR blocks. IPv4 addresses are supported.
        # *   You can enter up to 100 IP addresses or CIDR blocks. Separate multiple IP addresses or CIDR blocks with semicolons `(;)`.
        # *   If you do not specify this parameter, the original settings are retained.
        # *   If you set this parameter to a semicolon (`;`), the value of this parameter is cleared.
        # *   The IP address whitelist takes effect only on CloudSSO users who want to log on to the CloudSSO user portal by using the username-password logon or single sign-on (SSO) method. The IP address whitelist does not take effect on CloudSSO users who access accounts in a resource directory from the CloudSSO user portal.
        self.login_network_masks = login_network_masks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_get_credentials is not None:
            result['AllowUserToGetCredentials'] = self.allow_user_to_get_credentials

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToGetCredentials') is not None:
            self.allow_user_to_get_credentials = m.get('AllowUserToGetCredentials')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')

        return self

