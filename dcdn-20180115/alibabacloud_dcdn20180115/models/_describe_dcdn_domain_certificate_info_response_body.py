# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainCertificateInfoResponseBody(DaraModel):
    def __init__(
        self,
        cert_infos: main_models.DescribeDcdnDomainCertificateInfoResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        # The information about the certificate.
        self.cert_infos = cert_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = main_models.DescribeDcdnDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m.get('CertInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnDomainCertificateInfoResponseBodyCertInfos(DaraModel):
    def __init__(
        self,
        cert_info: List[main_models.DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for v1 in self.cert_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k1 in self.cert_info:
                result['CertInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k1 in m.get('CertInfo'):
                temp_model = main_models.DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo(DaraModel):
    def __init__(
        self,
        cert_domain_name: str = None,
        cert_expire_time: str = None,
        cert_id: str = None,
        cert_life: str = None,
        cert_name: str = None,
        cert_org: str = None,
        cert_region: str = None,
        cert_type: str = None,
        domain_name: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        status: str = None,
    ):
        # The domain name that matches the certificate.
        self.cert_domain_name = cert_domain_name
        # The time at which the certificate expires.
        self.cert_expire_time = cert_expire_time
        # The ID of the certificate.
        self.cert_id = cert_id
        # The validity period of the certificate. Unit: **months** or **years**.
        self.cert_life = cert_life
        # The name of the certificate.
        self.cert_name = cert_name
        # The certificate authority (CA) that issued the certificate.
        self.cert_org = cert_org
        # The region where the certificate is used.
        self.cert_region = cert_region
        # The type of the certificate.
        # 
        # *   **cas**: a certificate that is purchased by using Certificates Management Service
        # *   **upload**: a custom certificate that you upload
        self.cert_type = cert_type
        # The accelerated domain name.
        self.domain_name = domain_name
        # The status of HTTPS. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.sslprotocol = sslprotocol
        # The public key of the certificate.
        self.sslpub = sslpub
        # The status of the certificate. Valid values:
        # 
        # *   **success**: The certificate has taken effect.
        # *   **checking**: The system is checking whether the domain name is using Dynamic Route for CDN (DCDN).
        # *   **cname_error**: The domain name is not using DCDN.
        # *   **domain_invalid**: The domain name contains invalid characters.
        # *   **unsupport_wildcard**: The wildcard domain name is not supported.
        # *   **applying**: Certificate application is in progress.
        # *   **get_token_timeout**: The certificate application request has timed out.
        # *   **check_token_timeout**: The verification has timed out.
        # *   **get_cert_timeout**: The request to obtain the certificate has timed out.
        # *   **failed**: The certificate application request failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name

        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_life is not None:
            result['CertLife'] = self.cert_life

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org

        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')

        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')

        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

