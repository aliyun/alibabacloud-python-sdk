# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodSSLCertificateListResponseBody(DaraModel):
    def __init__(
        self,
        certificate_list_model: main_models.DescribeVodSSLCertificateListResponseBodyCertificateListModel = None,
        request_id: str = None,
    ):
        # The information about certificates.
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
            temp_model = main_models.DescribeVodSSLCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m.get('CertificateListModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodSSLCertificateListResponseBodyCertificateListModel(DaraModel):
    def __init__(
        self,
        cert_list: main_models.DescribeVodSSLCertificateListResponseBodyCertificateListModelCertList = None,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cert_list = cert_list
        # The number of certificates that are returned.
        self.count = count
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: integers from 1 to 1000.
        self.page_size = page_size

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertList') is not None:
            temp_model = main_models.DescribeVodSSLCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m.get('CertList'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class DescribeVodSSLCertificateListResponseBodyCertificateListModelCertList(DaraModel):
    def __init__(
        self,
        cert: List[main_models.DescribeVodSSLCertificateListResponseBodyCertificateListModelCertListCert] = None,
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
                temp_model = main_models.DescribeVodSSLCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k1))

        return self

class DescribeVodSSLCertificateListResponseBodyCertificateListModelCertListCert(DaraModel):
    def __init__(
        self,
        cert_id: int = None,
        cert_name: str = None,
        cert_region: str = None,
        common: str = None,
        fingerprint: str = None,
        issuer: str = None,
        last_time: int = None,
    ):
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.cert_region = cert_region
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

        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region

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

        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')

        if m.get('Common') is not None:
            self.common = m.get('Common')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        return self

