# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceSSLResponseBody(DaraModel):
    def __init__(
        self,
        cert_common_name: str = None,
        force_encryption: str = None,
        request_id: str = None,
        sslexpired_time: str = None,
        sslstatus: str = None,
    ):
        # The name of the SSL certificate.
        self.cert_common_name = cert_common_name
        # Specifies whether connections must be encrypted using SSL. Valid values:
        # 
        # - **1**: Connections must be encrypted using SSL.
        # 
        # - **0**: Connections do not need to be encrypted using SSL.
        self.force_encryption = force_encryption
        # The request ID.
        self.request_id = request_id
        # The expiration time of the SSL certificate. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format and is displayed in UTC.
        self.sslexpired_time = sslexpired_time
        # The status of the SSL feature.
        # 
        # - **Open**: The SSL feature is enabled.
        # 
        # - **Closed**: The SSL feature is disabled.
        self.sslstatus = sslstatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name

        if self.force_encryption is not None:
            result['ForceEncryption'] = self.force_encryption

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time

        if self.sslstatus is not None:
            result['SSLStatus'] = self.sslstatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')

        if m.get('ForceEncryption') is not None:
            self.force_encryption = m.get('ForceEncryption')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')

        if m.get('SSLStatus') is not None:
            self.sslstatus = m.get('SSLStatus')

        return self

