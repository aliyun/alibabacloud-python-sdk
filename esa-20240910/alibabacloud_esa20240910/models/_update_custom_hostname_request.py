# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomHostnameRequest(DaraModel):
    def __init__(
        self,
        cas_id: int = None,
        cas_region: str = None,
        cert_type: str = None,
        certificate: str = None,
        hostname_id: int = None,
        private_key: str = None,
        record_id: int = None,
        ssl_flag: str = None,
    ):
        # The ID of the Alibaba Cloud Security certificate. This parameter is required when CertType is set to cas.
        self.cas_id = cas_id
        # The region of the Alibaba Cloud Security certificate. This parameter is required when CertType is set to cas.
        # 
        # - cn-hangzhou: The value for accounts on the Alibaba Cloud China Website (www\\.aliyun.com).
        # 
        # - ap-southeast-1: The value for accounts on the Alibaba Cloud International Website (www\\.alibabacloud.com).
        self.cas_region = cas_region
        # The certificate type. This parameter is required when SslFlag is set to on.
        # 
        # - **free**: Free certificate.
        # 
        # - **upload**: Uploaded certificate.
        # 
        # - **cas**: Alibaba Cloud Security certificate.
        self.cert_type = cert_type
        # The content of the certificate. This parameter is required when CertType is set to upload.
        self.certificate = certificate
        # The ID of the SaaS domain name. You can obtain the ID by calling the [ListCustomHostnames](https://help.aliyun.com/document_detail/3018667.html) operation.
        # 
        # This parameter is required.
        self.hostname_id = hostname_id
        # The private key of the certificate. This parameter is required when CertType is set to upload.
        self.private_key = private_key
        # The ID of the record to attach. You can obtain the ID by calling the [ListRecords](https://help.aliyun.com/document_detail/2850265.html) operation.
        self.record_id = record_id
        # The SSL switch.
        # 
        # - **on**: Enables SSL.
        # 
        # - **off**: Disables SSL.
        self.ssl_flag = ssl_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cas_id is not None:
            result['CasId'] = self.cas_id

        if self.cas_region is not None:
            result['CasRegion'] = self.cas_region

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.hostname_id is not None:
            result['HostnameId'] = self.hostname_id

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.ssl_flag is not None:
            result['SslFlag'] = self.ssl_flag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasId') is not None:
            self.cas_id = m.get('CasId')

        if m.get('CasRegion') is not None:
            self.cas_region = m.get('CasRegion')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('HostnameId') is not None:
            self.hostname_id = m.get('HostnameId')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SslFlag') is not None:
            self.ssl_flag = m.get('SslFlag')

        return self

