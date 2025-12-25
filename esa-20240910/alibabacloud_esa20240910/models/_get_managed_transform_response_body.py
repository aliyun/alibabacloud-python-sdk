# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagedTransformResponseBody(DaraModel):
    def __init__(
        self,
        add_client_geolocation_header: str = None,
        add_real_client_ip_header: str = None,
        real_client_ip_header_name: str = None,
        request_id: str = None,
        site_version: int = None,
    ):
        # Add visitor geolocation header. Value range:
        # - on: Enable.
        # - off: Disable.
        self.add_client_geolocation_header = add_client_geolocation_header
        # Add the "ali-real-client-ip" header containing the real client IP. Value range:
        # - on: Enable.
        # - off: Disable.
        self.add_real_client_ip_header = add_real_client_ip_header
        self.real_client_ip_header_name = real_client_ip_header_name
        # Request ID.
        self.request_id = request_id
        # The version number of the site. For sites with version management enabled, this parameter can be used to specify the site version for which the configuration takes effect, defaulting to version 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_client_geolocation_header is not None:
            result['AddClientGeolocationHeader'] = self.add_client_geolocation_header

        if self.add_real_client_ip_header is not None:
            result['AddRealClientIpHeader'] = self.add_real_client_ip_header

        if self.real_client_ip_header_name is not None:
            result['RealClientIpHeaderName'] = self.real_client_ip_header_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddClientGeolocationHeader') is not None:
            self.add_client_geolocation_header = m.get('AddClientGeolocationHeader')

        if m.get('AddRealClientIpHeader') is not None:
            self.add_real_client_ip_header = m.get('AddRealClientIpHeader')

        if m.get('RealClientIpHeaderName') is not None:
            self.real_client_ip_header_name = m.get('RealClientIpHeaderName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

