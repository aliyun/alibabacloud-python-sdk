# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLivePackageOriginEndpointShrinkRequest(DaraModel):
    def __init__(
        self,
        authorization_code: str = None,
        channel_name: str = None,
        client_token: str = None,
        description: str = None,
        endpoint_name: str = None,
        group_name: str = None,
        ip_blacklist: str = None,
        ip_whitelist: str = None,
        live_packaging_config_shrink: str = None,
        manifest_name: str = None,
        protocol: str = None,
        timeshift_vision: int = None,
    ):
        # The authorization code. It can be up to 200 characters in length. You must configure AuthorizationCode, IpWhitelist, or both. Format: [A-Za-z0-9-_.]+
        self.authorization_code = authorization_code
        # The channel name.
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The endpoint description.
        self.description = description
        # The origin endpoint name. It can contain letters, digits, hyphens (-), and underscores (_). The name must be 1 to 200 characters in length. Format: [A-Za-z0-9_-]+
        # 
        # This parameter is required.
        self.endpoint_name = endpoint_name
        # The channel group name.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The IP address blacklist. It supports subnet masks. 0.0.0.0/0 is not allowed. It can be up to 1,000 characters in length. Separate multiple IP addresses with commas (,).
        self.ip_blacklist = ip_blacklist
        # The IP address whitelist. It supports subnet masks. 0.0.0.0/0 is not allowed. It can be up to 1,000 characters in length. Separate multiple IP addresses with commas (,). You must configure AuthorizationCode, IpWhitelist, or both.
        self.ip_whitelist = ip_whitelist
        self.live_packaging_config_shrink = live_packaging_config_shrink
        # The playlist name. Default value: manifest.
        self.manifest_name = manifest_name
        # The distribution protocol.
        # 
        # This parameter is required.
        self.protocol = protocol
        # The number of days that time-shifted content is available. Maximum value: 30. Default value: 0, which indicates that time shifting is not supported.
        self.timeshift_vision = timeshift_vision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ip_blacklist is not None:
            result['IpBlacklist'] = self.ip_blacklist

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        if self.live_packaging_config_shrink is not None:
            result['LivePackagingConfig'] = self.live_packaging_config_shrink

        if self.manifest_name is not None:
            result['ManifestName'] = self.manifest_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.timeshift_vision is not None:
            result['TimeshiftVision'] = self.timeshift_vision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpBlacklist') is not None:
            self.ip_blacklist = m.get('IpBlacklist')

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        if m.get('LivePackagingConfig') is not None:
            self.live_packaging_config_shrink = m.get('LivePackagingConfig')

        if m.get('ManifestName') is not None:
            self.manifest_name = m.get('ManifestName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TimeshiftVision') is not None:
            self.timeshift_vision = m.get('TimeshiftVision')

        return self

