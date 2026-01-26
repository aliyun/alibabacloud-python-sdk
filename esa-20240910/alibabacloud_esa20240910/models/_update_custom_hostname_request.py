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
        # 云盾证书ID，使用云盾证书时必填
        self.cas_id = cas_id
        # 云盾证书所在地域，使用云盾证书时必填
        self.cas_region = cas_region
        # 证书类型，SSL 开启时必填
        self.cert_type = cert_type
        # 证书公钥，使用上传证书时必填
        self.certificate = certificate
        # This parameter is required.
        self.hostname_id = hostname_id
        # 证书私钥，使用上传证书时必填
        self.private_key = private_key
        # 绑定的源站记录ID
        self.record_id = record_id
        # SSL开关
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

