# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainCertificateInfoResponseBody(DaraModel):
    def __init__(
        self,
        cert_infos: main_models.DescribeVsDomainCertificateInfoResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        self.cert_infos = cert_infos
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
            temp_model = main_models.DescribeVsDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m.get('CertInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsDomainCertificateInfoResponseBodyCertInfos(DaraModel):
    def __init__(
        self,
        cert_info: List[main_models.DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
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
                temp_model = main_models.DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k1))

        return self

class DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo(DaraModel):
    def __init__(
        self,
        cert_domain_name: str = None,
        cert_expire_time: str = None,
        cert_life: str = None,
        cert_name: str = None,
        cert_org: str = None,
        cert_type: str = None,
        domain_name: str = None,
        sslpub: str = None,
        server_certificate_status: str = None,
        status: str = None,
    ):
        self.cert_domain_name = cert_domain_name
        self.cert_expire_time = cert_expire_time
        self.cert_life = cert_life
        self.cert_name = cert_name
        self.cert_org = cert_org
        self.cert_type = cert_type
        self.domain_name = domain_name
        self.sslpub = sslpub
        self.server_certificate_status = server_certificate_status
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

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status

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

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

