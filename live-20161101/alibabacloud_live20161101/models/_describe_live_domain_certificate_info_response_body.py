# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainCertificateInfoResponseBody(DaraModel):
    def __init__(
        self,
        cert_infos: main_models.DescribeLiveDomainCertificateInfoResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        # The certificate information.
        self.cert_infos = cert_infos
        # The request ID.
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
            temp_model = main_models.DescribeLiveDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m.get('CertInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDomainCertificateInfoResponseBodyCertInfos(DaraModel):
    def __init__(
        self,
        cert_info: List[main_models.DescribeLiveDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
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
                temp_model = main_models.DescribeLiveDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainCertificateInfoResponseBodyCertInfosCertInfo(DaraModel):
    def __init__(
        self,
        cert_domain_name: str = None,
        cert_expire_time: str = None,
        cert_life: str = None,
        cert_name: str = None,
        cert_org: str = None,
        cert_type: str = None,
        domain_name: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        status: str = None,
    ):
        # The streaming domain or ingest domain that matches the certificate.
        self.cert_domain_name = cert_domain_name
        # The expiration time of the certificate. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.cert_expire_time = cert_expire_time
        # The validity period of the certificate.
        # 
        # *   If the validity period is greater than 12 months, XX years XX months is displayed. For example, 2 years 3 months indicates that the validity period is 2 years and 3 months.
        # *   If the validity period is less than 12 months, XX months is displayed. For example, 3 months indicates that the validity period is 3 months.
        self.cert_life = cert_life
        # The name of the certificate.
        self.cert_name = cert_name
        # The certificate authority (CA) that issued the certificate.
        self.cert_org = cert_org
        # The type of the certificate. Valid values:
        # 
        # *   **free**: a free certificate (for testing)
        # *   **cas**: a certificate that is purchased from Certificate Management Service
        # *   **upload**: a custom certificate that you uploaded
        self.cert_type = cert_type
        # The streaming domain or ingest domain.
        self.domain_name = domain_name
        # The status of HTTPS. Valid values:
        # 
        # *   **on**: HTTPS is enabled.
        # *   **off**: HTTPS is disabled.
        self.sslprotocol = sslprotocol
        # The public key of the certificate.
        self.sslpub = sslpub
        # The status of the free certificate that is used for testing. Valid values:
        # 
        # *   **success**: The certificate is effective.
        # *   **checking**: The system is checking whether the domain name is mapped to the CNAME that is assigned by ApsaraVideo Live.
        # *   **cname_error**: The domain name is not mapped to the CNAME that is assigned by ApsaraVideo Live.
        # *   **domain_invalid**: The domain name contains invalid characters.
        # *   **unsupport_wildcard**: The domain name is a wildcard domain name, which is not supported.
        # *   **applying**: The certificate is in the application progress.
        # *   **failed**: The application for the certificate failed.
        # 
        # >  The **Status** parameter is valid only if the certificate is a free certificate for testing. If the certificate is not a free certificate for testing, an empty value is returned.
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

        if self.cert_life is not None:
            result['CertLife'] = self.cert_life

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org

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

        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')

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

