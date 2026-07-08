# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListCertificatesResponseBody(DaraModel):
    def __init__(
        self,
        certificate_list: List[main_models.ListCertificatesResponseBodyCertificateList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The list of certificates.
        self.certificate_list = certificate_list
        # The current page number. Default value: 1.
        self.current_page = current_page
        # The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The number of entries returned on each page.
        self.show_size = show_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.certificate_list:
            for v1 in self.certificate_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k1 in self.certificate_list:
                result['CertificateList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k1 in m.get('CertificateList'):
                temp_model = main_models.ListCertificatesResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCertificatesResponseBodyCertificateList(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_identifier: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        certificate_source: str = None,
        certificate_status: str = None,
        common_name: str = None,
        domain: str = None,
        exist_private_key: bool = None,
        finger_print: str = None,
        instance_id: str = None,
        issuer: str = None,
        key_size: int = None,
        not_after: int = None,
        not_before: int = None,
        serial: str = None,
        subject_alternative_names: List[str] = None,
        using_product_list: List[str] = None,
    ):
        # The encryption algorithm of the certificate. Valid values:
        # 
        # - **RSA**
        # 
        # - **ECC**
        # 
        # - **SM2**
        self.algorithm = algorithm
        # The global ID of the certificate. This ID is used across Alibaba Cloud services and is in the `Certificate ID-Region ID` format. For example, if a certificate ID is `123`, the `CertIdentifier` is `123-cn-hangzhou` for the Alibaba Cloud China site and `123-ap-southeast-1` for the Alibaba Cloud International site (www\\.alibabacloud.com).
        # 
        # - For the Alibaba Cloud China website, the format is certificate ID + "-cn-hangzhou".
        # 
        # - For the Alibaba Cloud International website (www\\.alibabacloud.com), the format is certificate ID + "-ap-southeast-1".
        # 
        # For example, if the certificate ID is 123, the CertIdentifier is "123-cn-hangzhou" for the China site and "123-ap-southeast-1" for the International site.
        self.cert_identifier = cert_identifier
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The name of the certificate.
        self.certificate_name = certificate_name
        # The source of the certificate.
        # 
        # - BUY: A purchased certificate.
        # 
        # - TEST: A test certificate.
        # 
        # - UPLOAD: An uploaded certificate.
        self.certificate_source = certificate_source
        # The status of the certificate.
        # 
        # - **issued**: The certificate is issued.
        # 
        # - **revoked**: The certificate is revoked.
        # 
        # - **willExpire**: The certificate is about to expire.
        # 
        # - **expired**: The certificate has expired.
        self.certificate_status = certificate_status
        # The common name of the certificate.
        self.common_name = common_name
        # The domain names that are bound to the certificate. Multiple domain names are separated by commas.
        self.domain = domain
        # Indicates whether a private key is available. Valid values:
        # 
        # - **true**: A private key is available.
        # 
        # - **false**: A private key is not available.
        self.exist_private_key = exist_private_key
        # The fingerprint of the public key.
        self.finger_print = finger_print
        # The ID of the certificate instance.
        self.instance_id = instance_id
        # The certification authority.
        self.issuer = issuer
        # The key size, in bits.
        # 
        # - For RSA keys, typical sizes are 2048, 3072, or 4096.
        # 
        # - For ECC or SM2 keys, the typical size is 256.
        self.key_size = key_size
        # The end of the certificate validity period.
        self.not_after = not_after
        # The beginning of the certificate validity period.
        self.not_before = not_before
        # The serial number of the certificate.
        self.serial = serial
        # An array that contains the alternative domain names of the certificate. This parameter corresponds to the `Subject Alternative Name` field of the certificate.
        self.subject_alternative_names = subject_alternative_names
        # The list of Alibaba Cloud products in which the certificate is deployed.
        self.using_product_list = using_product_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.certificate_source is not None:
            result['CertificateSource'] = self.certificate_source

        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.exist_private_key is not None:
            result['ExistPrivateKey'] = self.exist_private_key

        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.key_size is not None:
            result['KeySize'] = self.key_size

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.serial is not None:
            result['Serial'] = self.serial

        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names

        if self.using_product_list is not None:
            result['UsingProductList'] = self.using_product_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('CertificateSource') is not None:
            self.certificate_source = m.get('CertificateSource')

        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExistPrivateKey') is not None:
            self.exist_private_key = m.get('ExistPrivateKey')

        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('Serial') is not None:
            self.serial = m.get('Serial')

        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('SubjectAlternativeNames')

        if m.get('UsingProductList') is not None:
            self.using_product_list = m.get('UsingProductList')

        return self

