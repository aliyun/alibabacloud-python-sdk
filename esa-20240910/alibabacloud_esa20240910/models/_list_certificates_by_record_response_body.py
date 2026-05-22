# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListCertificatesByRecordResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListCertificatesByRecordResponseBodyResult] = None,
        site_id: int = None,
        site_name: str = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.result = result
        self.site_id = site_id
        self.site_name = site_name
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListCertificatesByRecordResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCertificatesByRecordResponseBodyResult(DaraModel):
    def __init__(
        self,
        applyling_count: int = None,
        certificates: List[main_models.ListCertificatesByRecordResponseBodyResultCertificates] = None,
        count: int = None,
        record_name: str = None,
        status: str = None,
    ):
        self.applyling_count = applyling_count
        self.certificates = certificates
        self.count = count
        self.record_name = record_name
        self.status = status

    def validate(self):
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applyling_count is not None:
            result['ApplylingCount'] = self.applyling_count

        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplylingCount') is not None:
            self.applyling_count = m.get('ApplylingCount')

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.ListCertificatesByRecordResponseBodyResultCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListCertificatesByRecordResponseBodyResultCertificates(DaraModel):
    def __init__(
        self,
        cas_id: str = None,
        common_name: str = None,
        create_time: str = None,
        fingerprint_sha_256: str = None,
        id: str = None,
        issuer: str = None,
        issuer_cn: str = None,
        key_server_id: str = None,
        name: str = None,
        not_after: str = None,
        not_before: str = None,
        pub_alg: str = None,
        region: str = None,
        san: str = None,
        serial_number: str = None,
        sig_alg: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.cas_id = cas_id
        self.common_name = common_name
        self.create_time = create_time
        self.fingerprint_sha_256 = fingerprint_sha_256
        self.id = id
        self.issuer = issuer
        self.issuer_cn = issuer_cn
        self.key_server_id = key_server_id
        self.name = name
        self.not_after = not_after
        self.not_before = not_before
        self.pub_alg = pub_alg
        self.region = region
        self.san = san
        self.serial_number = serial_number
        self.sig_alg = sig_alg
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cas_id is not None:
            result['CasId'] = self.cas_id

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.fingerprint_sha_256 is not None:
            result['FingerprintSha256'] = self.fingerprint_sha_256

        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.issuer_cn is not None:
            result['IssuerCN'] = self.issuer_cn

        if self.key_server_id is not None:
            result['KeyServerId'] = self.key_server_id

        if self.name is not None:
            result['Name'] = self.name

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.pub_alg is not None:
            result['PubAlg'] = self.pub_alg

        if self.region is not None:
            result['Region'] = self.region

        if self.san is not None:
            result['SAN'] = self.san

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.sig_alg is not None:
            result['SigAlg'] = self.sig_alg

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasId') is not None:
            self.cas_id = m.get('CasId')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FingerprintSha256') is not None:
            self.fingerprint_sha_256 = m.get('FingerprintSha256')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('IssuerCN') is not None:
            self.issuer_cn = m.get('IssuerCN')

        if m.get('KeyServerId') is not None:
            self.key_server_id = m.get('KeyServerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('PubAlg') is not None:
            self.pub_alg = m.get('PubAlg')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SAN') is not None:
            self.san = m.get('SAN')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SigAlg') is not None:
            self.sig_alg = m.get('SigAlg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

