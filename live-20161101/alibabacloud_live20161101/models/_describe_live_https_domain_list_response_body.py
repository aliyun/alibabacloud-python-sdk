# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveHttpsDomainListResponseBody(DaraModel):
    def __init__(
        self,
        cert_infos: main_models.DescribeLiveHttpsDomainListResponseBodyCertInfos = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the certificates.
        self.cert_infos = cert_infos
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = main_models.DescribeLiveHttpsDomainListResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m.get('CertInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLiveHttpsDomainListResponseBodyCertInfos(DaraModel):
    def __init__(
        self,
        cert_info: List[main_models.DescribeLiveHttpsDomainListResponseBodyCertInfosCertInfo] = None,
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
                temp_model = main_models.DescribeLiveHttpsDomainListResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveHttpsDomainListResponseBodyCertInfosCertInfo(DaraModel):
    def __init__(
        self,
        cert_common_name: str = None,
        cert_expire_time: str = None,
        cert_name: str = None,
        cert_start_time: str = None,
        cert_status: str = None,
        cert_type: str = None,
        cert_update_time: str = None,
        domain_name: str = None,
    ):
        # The primary domain name of the certificate.
        self.cert_common_name = cert_common_name
        # The time when the certificate expires.
        self.cert_expire_time = cert_expire_time
        # The name of the certificate.
        self.cert_name = cert_name
        # The time when the certificate became effective.
        self.cert_start_time = cert_start_time
        # The status of the certificate. Valid values:
        # 
        # *   **ok**: The certificate is working as expected.
        # *   **mismatch**: The certificate does not match the specified domain name.
        # *   **expired**: The certificate has expired.
        # *   **expire_soon**: The certificate will expire soon.
        self.cert_status = cert_status
        # The type of the certificate. Valid values:
        # 
        # *   **cas**: a certificate that you purchased from Certificate Management Service
        # *   **upload**: a custom certificate that you uploaded
        self.cert_type = cert_type
        # The time when the certificate was updated.
        self.cert_update_time = cert_update_time
        # The accelerated domain name.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name

        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time

        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')

        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')

        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

