# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDBInstanceSSLRequest(DaraModel):
    def __init__(
        self,
        cert_common_name: str = None,
        dbinstance_name: str = None,
        enable_ssl: bool = None,
        region_id: str = None,
    ):
        self.cert_common_name = cert_common_name
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.enable_ssl = enable_ssl
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

