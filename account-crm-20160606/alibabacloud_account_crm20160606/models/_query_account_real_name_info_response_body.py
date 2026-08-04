# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryAccountRealNameInfoResponseBody(DaraModel):
    def __init__(
        self,
        profile_info: main_models.QueryAccountRealNameInfoResponseBodyProfileInfo = None,
        request_id: str = None,
    ):
        self.profile_info = profile_info
        self.request_id = request_id

    def validate(self):
        if self.profile_info:
            self.profile_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.profile_info is not None:
            result['ProfileInfo'] = self.profile_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProfileInfo') is not None:
            temp_model = main_models.QueryAccountRealNameInfoResponseBodyProfileInfo()
            self.profile_info = temp_model.from_map(m.get('ProfileInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAccountRealNameInfoResponseBodyProfileInfo(DaraModel):
    def __init__(
        self,
        account_certify_type: str = None,
        auth_alipay: str = None,
        auth_bei_an_cid: str = None,
        auth_domain: str = None,
        certified_from: str = None,
        certified_time: str = None,
        is_bank_idauth: str = None,
        is_certified: str = None,
        license_number: str = None,
        license_type: str = None,
        name: str = None,
        processing_enterprise_certify: bool = None,
    ):
        self.account_certify_type = account_certify_type
        self.auth_alipay = auth_alipay
        self.auth_bei_an_cid = auth_bei_an_cid
        self.auth_domain = auth_domain
        self.certified_from = certified_from
        self.certified_time = certified_time
        self.is_bank_idauth = is_bank_idauth
        self.is_certified = is_certified
        self.license_number = license_number
        self.license_type = license_type
        self.name = name
        self.processing_enterprise_certify = processing_enterprise_certify

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_certify_type is not None:
            result['AccountCertifyType'] = self.account_certify_type

        if self.auth_alipay is not None:
            result['AuthAlipay'] = self.auth_alipay

        if self.auth_bei_an_cid is not None:
            result['AuthBeiAnCid'] = self.auth_bei_an_cid

        if self.auth_domain is not None:
            result['AuthDomain'] = self.auth_domain

        if self.certified_from is not None:
            result['CertifiedFrom'] = self.certified_from

        if self.certified_time is not None:
            result['CertifiedTime'] = self.certified_time

        if self.is_bank_idauth is not None:
            result['IsBankIDAuth'] = self.is_bank_idauth

        if self.is_certified is not None:
            result['IsCertified'] = self.is_certified

        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.name is not None:
            result['Name'] = self.name

        if self.processing_enterprise_certify is not None:
            result['ProcessingEnterpriseCertify'] = self.processing_enterprise_certify

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCertifyType') is not None:
            self.account_certify_type = m.get('AccountCertifyType')

        if m.get('AuthAlipay') is not None:
            self.auth_alipay = m.get('AuthAlipay')

        if m.get('AuthBeiAnCid') is not None:
            self.auth_bei_an_cid = m.get('AuthBeiAnCid')

        if m.get('AuthDomain') is not None:
            self.auth_domain = m.get('AuthDomain')

        if m.get('CertifiedFrom') is not None:
            self.certified_from = m.get('CertifiedFrom')

        if m.get('CertifiedTime') is not None:
            self.certified_time = m.get('CertifiedTime')

        if m.get('IsBankIDAuth') is not None:
            self.is_bank_idauth = m.get('IsBankIDAuth')

        if m.get('IsCertified') is not None:
            self.is_certified = m.get('IsCertified')

        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProcessingEnterpriseCertify') is not None:
            self.processing_enterprise_certify = m.get('ProcessingEnterpriseCertify')

        return self

