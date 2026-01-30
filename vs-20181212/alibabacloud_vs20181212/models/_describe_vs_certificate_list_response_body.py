# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsCertificateListResponseBody(DaraModel):
    def __init__(
        self,
        certificate_list_model: main_models.DescribeVsCertificateListResponseBodyCertificateListModel = None,
        request_id: str = None,
    ):
        self.certificate_list_model = certificate_list_model
        self.request_id = request_id

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = main_models.DescribeVsCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m.get('CertificateListModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsCertificateListResponseBodyCertificateListModel(DaraModel):
    def __init__(
        self,
        cert_list: List[main_models.DescribeVsCertificateListResponseBodyCertificateListModelCertList] = None,
        count: int = None,
    ):
        self.cert_list = cert_list
        self.count = count

    def validate(self):
        if self.cert_list:
            for v1 in self.cert_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertList'] = []
        if self.cert_list is not None:
            for k1 in self.cert_list:
                result['CertList'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k1 in m.get('CertList'):
                temp_model = main_models.DescribeVsCertificateListResponseBodyCertificateListModelCertList()
                self.cert_list.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

class DescribeVsCertificateListResponseBodyCertificateListModelCertList(DaraModel):
    def __init__(
        self,
        cert_id: int = None,
        cert_name: str = None,
        common: str = None,
        fingerprint: str = None,
        issuer: str = None,
        last_time: int = None,
    ):
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.common = common
        self.fingerprint = fingerprint
        self.issuer = issuer
        self.last_time = last_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.common is not None:
            result['Common'] = self.common

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('Common') is not None:
            self.common = m.get('Common')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        return self

