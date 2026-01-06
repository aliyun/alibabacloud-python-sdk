# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class GetUserCertificateDetailResponseBody(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        buy_in_aliyun: bool = None,
        cert: str = None,
        cert_chain: List[main_models.GetUserCertificateDetailResponseBodyCertChain] = None,
        cert_identifier: str = None,
        city: str = None,
        common: str = None,
        country: str = None,
        encrypt_cert: str = None,
        encrypt_private_key: str = None,
        end_date: str = None,
        expired: bool = None,
        fingerprint: str = None,
        id: int = None,
        instance_id: str = None,
        issuer: str = None,
        key: str = None,
        name: str = None,
        not_after: int = None,
        not_before: int = None,
        order_id: int = None,
        org_name: str = None,
        province: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_cert: str = None,
        sign_private_key: str = None,
        start_date: str = None,
        tags: List[main_models.GetUserCertificateDetailResponseBodyTags] = None,
    ):
        # The algorithm.
        self.algorithm = algorithm
        # Indicates whether the certificate was purchased from Alibaba Cloud. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.buy_in_aliyun = buy_in_aliyun
        # The content of the certificate if the certificate does not use an SM algorithm. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.cert = cert
        # The certificate chain.
        self.cert_chain = cert_chain
        # The certificate identifier. The value is in the "Certificate ID-cn-hangzhou" format. For example, if the ID of the certificate is 123, the value of CertIdentifier is 123-cn-hangzhou.
        self.cert_identifier = cert_identifier
        # The city of the company or organization to which the certificate purchaser belongs.
        self.city = city
        # The primary domain name that is bound to the certificate.
        self.common = common
        # The country or region of the company or organization to which the certificate purchaser belongs.
        self.country = country
        # The content of the encryption certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.encrypt_cert = encrypt_cert
        # The private key of the encryption certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.encrypt_private_key = encrypt_private_key
        # The expiration date of the certificate.
        self.end_date = end_date
        # Indicates whether the certificate has expired. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.expired = expired
        # The fingerprint of the certificate.
        self.fingerprint = fingerprint
        # The ID of the certificate.
        self.id = id
        # The instance ID of the resource.
        self.instance_id = instance_id
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer
        # The private key of the certificate if the certificate does not use an SM algorithm. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.key = key
        # The name of the certificate.
        self.name = name
        # The end of the validity period of the certificate.
        self.not_after = not_after
        # The beginning of the validity period of the certificate.
        self.not_before = not_before
        # The order ID.
        self.order_id = order_id
        # The name of the company or organization to which the certificate purchaser belongs.
        self.org_name = org_name
        # The province of the company or organization to which the certificate purchaser belongs.
        self.province = province
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # All domain names that are bound to the certificate.
        self.sans = sans
        # The serial number of the certificate.
        self.serial_no = serial_no
        # The SHA-2 value of the certificate.
        self.sha_2 = sha_2
        # The content of the signing certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.sign_cert = sign_cert
        # The private key of the signing certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.sign_private_key = sign_private_key
        # The issuance date of the certificate.
        self.start_date = start_date
        self.tags = tags

    def validate(self):
        if self.cert_chain:
            for v1 in self.cert_chain:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.buy_in_aliyun is not None:
            result['BuyInAliyun'] = self.buy_in_aliyun

        if self.cert is not None:
            result['Cert'] = self.cert

        result['CertChain'] = []
        if self.cert_chain is not None:
            for k1 in self.cert_chain:
                result['CertChain'].append(k1.to_map() if k1 else None)

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.city is not None:
            result['City'] = self.city

        if self.common is not None:
            result['Common'] = self.common

        if self.country is not None:
            result['Country'] = self.country

        if self.encrypt_cert is not None:
            result['EncryptCert'] = self.encrypt_cert

        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        if self.province is not None:
            result['Province'] = self.province

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no

        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2

        if self.sign_cert is not None:
            result['SignCert'] = self.sign_cert

        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('BuyInAliyun') is not None:
            self.buy_in_aliyun = m.get('BuyInAliyun')

        if m.get('Cert') is not None:
            self.cert = m.get('Cert')

        self.cert_chain = []
        if m.get('CertChain') is not None:
            for k1 in m.get('CertChain'):
                temp_model = main_models.GetUserCertificateDetailResponseBodyCertChain()
                self.cert_chain.append(temp_model.from_map(k1))

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Common') is not None:
            self.common = m.get('Common')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('EncryptCert') is not None:
            self.encrypt_cert = m.get('EncryptCert')

        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')

        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')

        if m.get('SignCert') is not None:
            self.sign_cert = m.get('SignCert')

        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetUserCertificateDetailResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetUserCertificateDetailResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class GetUserCertificateDetailResponseBodyCertChain(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        issuer_common_name: str = None,
        not_after: int = None,
        not_before: int = None,
        remain_day: int = None,
    ):
        # The common name of the certificate.
        self.common_name = common_name
        # The common name of the issuer.
        self.issuer_common_name = issuer_common_name
        # The end of the validity period of the certificate.
        self.not_after = not_after
        # The beginning of the validity period of the certificate.
        self.not_before = not_before
        # The remaining days of the certificate validity period.
        self.remain_day = remain_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.issuer_common_name is not None:
            result['IssuerCommonName'] = self.issuer_common_name

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.remain_day is not None:
            result['RemainDay'] = self.remain_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('IssuerCommonName') is not None:
            self.issuer_common_name = m.get('IssuerCommonName')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('RemainDay') is not None:
            self.remain_day = m.get('RemainDay')

        return self

