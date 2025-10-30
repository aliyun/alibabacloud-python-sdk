# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceSSLResponseBody(DaraModel):
    def __init__(
        self,
        cert_common_name: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        request_id: str = None,
        sslenabled: bool = None,
        sslexpired_time: str = None,
    ):
        # The name of the SSL certificate.
        self.cert_common_name = cert_common_name
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The name of the instance.
        self.dbinstance_name = dbinstance_name
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether SSL encryption is enabled.
        self.sslenabled = sslenabled
        # The expiration time of the SSL certificate.
        self.sslexpired_time = sslexpired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')

        return self

