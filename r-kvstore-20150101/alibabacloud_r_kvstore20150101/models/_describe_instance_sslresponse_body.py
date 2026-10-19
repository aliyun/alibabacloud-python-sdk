# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceSSLResponseBody(DaraModel):
    def __init__(
        self,
        cert_common_name: str = None,
        cert_download_url: str = None,
        instance_id: str = None,
        request_id: str = None,
        sslenabled: str = None,
        sslexpired_time: str = None,
    ):
        # The common name of the CA certificate. The default value is the internal network endpoint of the instance.
        self.cert_common_name = cert_common_name
        # The download URL of the CA certificate.
        self.cert_download_url = cert_download_url
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id
        # The status of the TLS (SSL) encryption feature. Valid values:
        # * **Enable**: Enabled.
        # * **Disable**: Disabled.
        self.sslenabled = sslenabled
        # The expiration time of the CA certificate.
        # 
        # The time is displayed in the YYYY-MM-DDTHH:mm:ssZ format in UTC.
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

        if self.cert_download_url is not None:
            result['CertDownloadURL'] = self.cert_download_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if m.get('CertDownloadURL') is not None:
            self.cert_download_url = m.get('CertDownloadURL')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')

        return self

