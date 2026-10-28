# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterSSLRequest(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbcluster_id: str = None,
        enable_ssl: bool = None,
        region_id: str = None,
        sslenabled: str = None,
    ):
        # The internal or public endpoint for which to create or update a server certificate.
        self.connection_string = connection_string
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable SSL connection encryption. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable_ssl = enable_ssl
        # The region ID.
        self.region_id = region_id
        # The SSL operation. This parameter and EnableSSL are mutually exclusive. Valid values:
        # 
        # - Enable: Enables SSL.
        # - Disable: Disables SSL.
        # - Update: Updates the validity period of an enabled SSL certificate and retains the current endpoint bound to the certificate. When you set this parameter to Update, do not specify ConnectionString, or specify an endpoint that is the same as the current endpoint bound to the certificate.
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        return self

