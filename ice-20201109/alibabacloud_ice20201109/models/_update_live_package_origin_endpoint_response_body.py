# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateLivePackageOriginEndpointResponseBody(DaraModel):
    def __init__(
        self,
        live_package_origin_endpoint: main_models.UpdateLivePackageOriginEndpointResponseBodyLivePackageOriginEndpoint = None,
        request_id: str = None,
    ):
        # The information about the origin endpoint.
        self.live_package_origin_endpoint = live_package_origin_endpoint
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_package_origin_endpoint:
            self.live_package_origin_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_package_origin_endpoint is not None:
            result['LivePackageOriginEndpoint'] = self.live_package_origin_endpoint.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivePackageOriginEndpoint') is not None:
            temp_model = main_models.UpdateLivePackageOriginEndpointResponseBodyLivePackageOriginEndpoint()
            self.live_package_origin_endpoint = temp_model.from_map(m.get('LivePackageOriginEndpoint'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateLivePackageOriginEndpointResponseBodyLivePackageOriginEndpoint(DaraModel):
    def __init__(
        self,
        authorization_code: str = None,
        channel_name: str = None,
        create_time: str = None,
        description: str = None,
        endpoint_name: str = None,
        endpoint_url: str = None,
        group_name: str = None,
        ip_blacklist: str = None,
        ip_whitelist: str = None,
        last_modified: str = None,
        live_packaging_config: main_models.LivePackagingConfig = None,
        manifest_name: str = None,
        protocol: str = None,
        timeshift_vision: int = None,
    ):
        # The authorization code.
        self.authorization_code = authorization_code
        # The channel name.
        self.channel_name = channel_name
        # The time when the endpoint was created.
        self.create_time = create_time
        # The endpoint description.
        self.description = description
        # The endpoint name.
        self.endpoint_name = endpoint_name
        # The endpoint URL.
        self.endpoint_url = endpoint_url
        # The channel group name.
        self.group_name = group_name
        # The IP address blacklist. It supports subnet masks. Multiple IP addresses are separated by commas (,).
        self.ip_blacklist = ip_blacklist
        # The IP address whitelist. It supports subnet masks. Multiple IP addresses are separated by commas (,).
        self.ip_whitelist = ip_whitelist
        # The time when the endpoint was last modified.
        self.last_modified = last_modified
        self.live_packaging_config = live_packaging_config
        # The playlist name. Default value: manifest.
        self.manifest_name = manifest_name
        # The protocol. Only HLS is supported.
        self.protocol = protocol
        # The number of days that time-shifted content is available. Maximum value: 30.
        self.timeshift_vision = timeshift_vision

    def validate(self):
        if self.live_packaging_config:
            self.live_packaging_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.endpoint_url is not None:
            result['EndpointUrl'] = self.endpoint_url

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ip_blacklist is not None:
            result['IpBlacklist'] = self.ip_blacklist

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.live_packaging_config is not None:
            result['LivePackagingConfig'] = self.live_packaging_config.to_map()

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('EndpointUrl') is not None:
            self.endpoint_url = m.get('EndpointUrl')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpBlacklist') is not None:
            self.ip_blacklist = m.get('IpBlacklist')

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('LivePackagingConfig') is not None:
            temp_model = main_models.LivePackagingConfig()
            self.live_packaging_config = temp_model.from_map(m.get('LivePackagingConfig'))

        if m.get('ManifestName') is not None:
            self.manifest_name = m.get('ManifestName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TimeshiftVision') is not None:
            self.timeshift_vision = m.get('TimeshiftVision')

        return self

