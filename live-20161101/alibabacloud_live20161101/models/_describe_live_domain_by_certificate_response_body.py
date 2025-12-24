# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainByCertificateResponseBody(DaraModel):
    def __init__(
        self,
        cert_infos: main_models.DescribeLiveDomainByCertificateResponseBodyCertInfos = None,
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
            temp_model = main_models.DescribeLiveDomainByCertificateResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m.get('CertInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDomainByCertificateResponseBodyCertInfos(DaraModel):
    def __init__(
        self,
        cert_info: List[main_models.DescribeLiveDomainByCertificateResponseBodyCertInfosCertInfo] = None,
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
                temp_model = main_models.DescribeLiveDomainByCertificateResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainByCertificateResponseBodyCertInfosCertInfo(DaraModel):
    def __init__(
        self,
        cert_ca_is_legacy: str = None,
        cert_expire_time: str = None,
        cert_expired: str = None,
        cert_start_time: str = None,
        cert_subject_common_name: str = None,
        cert_type: str = None,
        domain_list: str = None,
        domain_names: str = None,
        issuer: str = None,
    ):
        # Indicates whether the SSL certificate is obsolete. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.cert_ca_is_legacy = cert_ca_is_legacy
        # The time at which the certificate expires.
        self.cert_expire_time = cert_expire_time
        # Indicates whether the SSL certificate is expired. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.cert_expired = cert_expired
        # The effective time of the certificate.
        self.cert_start_time = cert_start_time
        # The name of the SSL certificate owner.
        self.cert_subject_common_name = cert_subject_common_name
        # The type of the certificate. Valid values: **RSA**, **DSA**, and **ECDSA**.
        self.cert_type = cert_type
        # The list of domain names. If a value is returned, the value matches the SSL certificate. Multiple domain names are separated by commas (,).
        self.domain_list = domain_list
        # The domain names (DNS fields) that match the SSL certificate. Multiple domain names are separated by commas (,).
        self.domain_names = domain_names
        # The certificate authority (CA) that issued the SSL certificate.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_ca_is_legacy is not None:
            result['CertCaIsLegacy'] = self.cert_ca_is_legacy

        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time

        if self.cert_expired is not None:
            result['CertExpired'] = self.cert_expired

        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time

        if self.cert_subject_common_name is not None:
            result['CertSubjectCommonName'] = self.cert_subject_common_name

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCaIsLegacy') is not None:
            self.cert_ca_is_legacy = m.get('CertCaIsLegacy')

        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')

        if m.get('CertExpired') is not None:
            self.cert_expired = m.get('CertExpired')

        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')

        if m.get('CertSubjectCommonName') is not None:
            self.cert_subject_common_name = m.get('CertSubjectCommonName')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        return self

