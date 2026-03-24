# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCertificateInfoByIDResponseBody(DaraModel):
    def __init__(
        self,
        cert_infos: main_models.DescribeCertificateInfoByIDResponseBodyCertInfos = None,
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
            temp_model = main_models.DescribeCertificateInfoByIDResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m.get('CertInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCertificateInfoByIDResponseBodyCertInfos(DaraModel):
    def __init__(
        self,
        cert_info: List[main_models.DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo] = None,
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
                temp_model = main_models.DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k1))

        return self

class DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo(DaraModel):
    def __init__(
        self,
        cert_expire_time: str = None,
        cert_id: str = None,
        cert_name: str = None,
        cert_type: str = None,
        create_time: str = None,
        domain_list: str = None,
        https_crt: str = None,
    ):
        self.cert_expire_time = cert_expire_time
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.cert_type = cert_type
        self.create_time = create_time
        self.domain_list = domain_list
        self.https_crt = https_crt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.https_crt is not None:
            result['HttpsCrt'] = self.https_crt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('HttpsCrt') is not None:
            self.https_crt = m.get('HttpsCrt')

        return self

