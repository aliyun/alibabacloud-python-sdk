# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodCertificateListResponseBody(DaraModel):
    def __init__(
        self,
        certificate_list_model: main_models.DescribeVodCertificateListResponseBodyCertificateListModel = None,
        request_id: str = None,
    ):
        # The information about each certificate.
        self.certificate_list_model = certificate_list_model
        # The ID of the request.
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
            temp_model = main_models.DescribeVodCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m.get('CertificateListModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodCertificateListResponseBodyCertificateListModel(DaraModel):
    def __init__(
        self,
        cert_list: main_models.DescribeVodCertificateListResponseBodyCertificateListModelCertList = None,
        count: int = None,
    ):
        self.cert_list = cert_list
        # The number of certificates that are returned.
        self.count = count

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertList') is not None:
            temp_model = main_models.DescribeVodCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m.get('CertList'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

class DescribeVodCertificateListResponseBodyCertificateListModelCertList(DaraModel):
    def __init__(
        self,
        cert: List[main_models.DescribeVodCertificateListResponseBodyCertificateListModelCertListCert] = None,
    ):
        self.cert = cert

    def validate(self):
        if self.cert:
            for v1 in self.cert:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cert'] = []
        if self.cert is not None:
            for k1 in self.cert:
                result['Cert'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert = []
        if m.get('Cert') is not None:
            for k1 in m.get('Cert'):
                temp_model = main_models.DescribeVodCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k1))

        return self

class DescribeVodCertificateListResponseBodyCertificateListModelCertListCert(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_id: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common: str = None,
        create_time: int = None,
        domain_match_cert: bool = None,
        end_time: int = None,
        fingerprint: str = None,
        instance_id: str = None,
        issuer: str = None,
        last_time: int = None,
        sign_algorithm: str = None,
    ):
        self.algorithm = algorithm
        self.cert_id = cert_id
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common = common
        self.create_time = create_time
        self.domain_match_cert = domain_match_cert
        self.end_time = end_time
        self.fingerprint = fingerprint
        self.instance_id = instance_id
        self.issuer = issuer
        self.last_time = last_time
        self.sign_algorithm = sign_algorithm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.common is not None:
            result['Common'] = self.common

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_match_cert is not None:
            result['DomainMatchCert'] = self.domain_match_cert

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('Common') is not None:
            self.common = m.get('Common')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainMatchCert') is not None:
            self.domain_match_cert = m.get('DomainMatchCert')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')

        return self

