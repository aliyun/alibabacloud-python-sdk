# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateManagedTransformRequest(DaraModel):
    def __init__(
        self,
        add_client_geolocation_header: str = None,
        add_real_client_ip_header: str = None,
        real_client_ip_header_name: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # Specifies whether to include the header that indicates the geographical location of a client in an origin request. Valid values:
        # 
        # *   on
        # *   off
        self.add_client_geolocation_header = add_client_geolocation_header
        # Specifies whether to include the "ali-real-client-ip" header that indicates the client\\"s real IP address in an origin request. Valid values:
        # 
        # *   on
        # *   off
        self.add_real_client_ip_header = add_real_client_ip_header
        self.real_client_ip_header_name = real_client_ip_header_name
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the website. You can use this parameter to specify a version of your website to apply the feature settings. By default, version 0 is used.
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

        if self.site_id is not None:
            result['SiteId'] = self.site_id

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

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

