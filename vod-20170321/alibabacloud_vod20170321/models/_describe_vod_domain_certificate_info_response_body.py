# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodDomainCertificateInfoResponseBody(DaraModel):
    def __init__(
        self,
        cert_infos: main_models.DescribeVodDomainCertificateInfoResponseBodyCertInfos = None,
        request_id: str = None,
    ):
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
            temp_model = main_models.DescribeVodDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m.get('CertInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodDomainCertificateInfoResponseBodyCertInfos(DaraModel):
    def __init__(
        self,
        cert_info: List[main_models.DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
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
                temp_model = main_models.DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k1))

        return self

class DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo(DaraModel):
    def __init__(
        self,
        cert_domain_name: str = None,
        cert_expire_time: str = None,
        cert_id: str = None,
        cert_life: str = None,
        cert_name: str = None,
        cert_org: str = None,
        cert_region: str = None,
        cert_start_time: str = None,
        cert_type: str = None,
        cert_update_time: str = None,
        domain_cname_status: str = None,
        domain_name: str = None,
        server_certificate: str = None,
        server_certificate_status: str = None,
        status: str = None,
    ):
        self.cert_domain_name = cert_domain_name
        self.cert_expire_time = cert_expire_time
        self.cert_id = cert_id
        self.cert_life = cert_life
        self.cert_name = cert_name
        self.cert_org = cert_org
        self.cert_region = cert_region
        self.cert_start_time = cert_start_time
        self.cert_type = cert_type
        self.cert_update_time = cert_update_time
        self.domain_cname_status = domain_cname_status
        self.domain_name = domain_name
        self.server_certificate = server_certificate
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

        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time

        if self.domain_cname_status is not None:
            result['DomainCnameStatus'] = self.domain_cname_status

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate

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

        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')

        if m.get('DomainCnameStatus') is not None:
            self.domain_cname_status = m.get('DomainCnameStatus')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')

        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

