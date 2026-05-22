# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListCertificatesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[main_models.ListCertificatesResponseBodyResult] = None,
        site_id: int = None,
        site_name: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried certificates.
        self.result = result
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name
        # The total number of entries returned.
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListCertificatesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCertificatesResponseBodyResult(DaraModel):
    def __init__(
        self,
        apply_code: int = None,
        apply_message: str = None,
        cas_id: str = None,
        common_name: str = None,
        create_time: str = None,
        dcv: List[main_models.ListCertificatesResponseBodyResultDCV] = None,
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
        # The error code returned for certificate application.
        self.apply_code = apply_code
        # The error message returned for certificate application.
        self.apply_message = apply_message
        # The certificate ID on Certificate Management Service.
        self.cas_id = cas_id
        # The Common Name of the certificate.
        self.common_name = common_name
        # The time when the certificate was created.
        self.create_time = create_time
        # The Domain Control Validation (DCV) information.
        self.dcv = dcv
        # The SHA-256 fingerprint of the certificate.
        self.fingerprint_sha_256 = fingerprint_sha_256
        # The certificate ID on ESA.
        self.id = id
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer
        # The Common Name of the certificate issuer.
        self.issuer_cn = issuer_cn
        self.key_server_id = key_server_id
        # The certificate name.
        self.name = name
        # The time when the certificate expires.
        self.not_after = not_after
        # The time when the certificate takes effect.
        self.not_before = not_before
        # The public key algorithm of the certificate.
        self.pub_alg = pub_alg
        # The region where the certificate is stored.
        self.region = region
        # The Subject Alternative Name (SAN) of the certificate.
        self.san = san
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The signature algorithm of the certificate.
        self.sig_alg = sig_alg
        # The certificate status.
        # 
        # *   OK
        # *   Expired
        # *   Expiring
        # *   Issued
        # *   Applying
        # *   ApplyFailed
        # *   Canceled
        self.status = status
        # The certificate type.
        # 
        # *   cas: certificate that is purchased by using Certificate Management Service
        # *   upload: custom certificate that you upload
        # *   free: free certificate
        self.type = type
        # The time when the certificate was updated.
        self.update_time = update_time

    def validate(self):
        if self.dcv:
            for v1 in self.dcv:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_code is not None:
            result['ApplyCode'] = self.apply_code

        if self.apply_message is not None:
            result['ApplyMessage'] = self.apply_message

        if self.cas_id is not None:
            result['CasId'] = self.cas_id

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DCV'] = []
        if self.dcv is not None:
            for k1 in self.dcv:
                result['DCV'].append(k1.to_map() if k1 else None)

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
        if m.get('ApplyCode') is not None:
            self.apply_code = m.get('ApplyCode')

        if m.get('ApplyMessage') is not None:
            self.apply_message = m.get('ApplyMessage')

        if m.get('CasId') is not None:
            self.cas_id = m.get('CasId')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.dcv = []
        if m.get('DCV') is not None:
            for k1 in m.get('DCV'):
                temp_model = main_models.ListCertificatesResponseBodyResultDCV()
                self.dcv.append(temp_model.from_map(k1))

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

class ListCertificatesResponseBodyResultDCV(DaraModel):
    def __init__(
        self,
        id: str = None,
        key: str = None,
        status: str = None,
        type: str = None,
        value: str = None,
    ):
        # The DCV ID.
        self.id = id
        # The DCV name. It is a TXT record name if Type is DNS or URL if Type is HTTP.
        self.key = key
        # The verification status.
        self.status = status
        # The DCV type. Valid values: DNS and HTTP.
        self.type = type
        # The DCV content.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.key is not None:
            result['Key'] = self.key

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

