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
    ):
        # The private or public endpoint for which the server certificate needs to be created or updated.
        self.connection_string = connection_string
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable SSL encryption. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        # 
        # This parameter is required.
        self.enable_ssl = enable_ssl
        # The region ID.
        self.region_id = region_id

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

        return self

