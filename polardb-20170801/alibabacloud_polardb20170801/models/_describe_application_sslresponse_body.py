# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationSSLResponseBody(DaraModel):
    def __init__(
        self,
        cert_common_name: str = None,
        cert_expired_time: str = None,
        cert_fingerprint_sha_256der: str = None,
        cert_modified_time: str = None,
        cert_source: str = None,
        request_id: str = None,
        sslauto_rotate: bool = None,
        sslenabled: bool = None,
    ):
        # The Common Name of the certificate. This field is empty when SSL is not enabled.
        self.cert_common_name = cert_common_name
        # The certificate expiration time in UTC. This field is empty when SSL is not enabled.
        self.cert_expired_time = cert_expired_time
        # The SHA-256 (DER) fingerprint of the server certificate in lowercase hex. Use this value for client pinning. This is consistent with openssl -fingerprint -sha256. This field is empty when SSL is not enabled.
        self.cert_fingerprint_sha_256der = cert_fingerprint_sha_256der
        # The most recent certificate installation time in UTC. This field is empty when SSL is not enabled.
        self.cert_modified_time = cert_modified_time
        # The certificate source. Valid values:
        # 
        # - ca: issued by the platform.
        # - customer: provided by the user.
        # 
        # This field is empty when SSL is not enabled.
        self.cert_source = cert_source
        # Id of the request
        self.request_id = request_id
        # Indicates whether automatic rotation of platform-issued certificates is enabled.
        self.sslauto_rotate = sslauto_rotate
        # Indicates whether SSL is enabled.
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name

        if self.cert_expired_time is not None:
            result['CertExpiredTime'] = self.cert_expired_time

        if self.cert_fingerprint_sha_256der is not None:
            result['CertFingerprintSha256Der'] = self.cert_fingerprint_sha_256der

        if self.cert_modified_time is not None:
            result['CertModifiedTime'] = self.cert_modified_time

        if self.cert_source is not None:
            result['CertSource'] = self.cert_source

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sslauto_rotate is not None:
            result['SSLAutoRotate'] = self.sslauto_rotate

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')

        if m.get('CertExpiredTime') is not None:
            self.cert_expired_time = m.get('CertExpiredTime')

        if m.get('CertFingerprintSha256Der') is not None:
            self.cert_fingerprint_sha_256der = m.get('CertFingerprintSha256Der')

        if m.get('CertModifiedTime') is not None:
            self.cert_modified_time = m.get('CertModifiedTime')

        if m.get('CertSource') is not None:
            self.cert_source = m.get('CertSource')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLAutoRotate') is not None:
            self.sslauto_rotate = m.get('SSLAutoRotate')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        return self

