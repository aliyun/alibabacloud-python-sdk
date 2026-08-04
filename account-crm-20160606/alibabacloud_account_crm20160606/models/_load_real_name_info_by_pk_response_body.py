# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class LoadRealNameInfoByPkResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.LoadRealNameInfoByPkResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.LoadRealNameInfoByPkResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class LoadRealNameInfoByPkResponseBodyData(DaraModel):
    def __init__(
        self,
        account_certify_type: str = None,
        auth_alipay: str = None,
        auth_alipay_domain: str = None,
        auth_alipay_login_id: str = None,
        auth_bei_an_cid: str = None,
        auth_domain: str = None,
        certified_from: str = None,
        certified_time: str = None,
        certify_status: int = None,
        cic_certify_from: int = None,
        cic_certify_product: int = None,
        is_bank_idauth: bool = None,
        is_certified: bool = None,
        license_number: str = None,
        license_type: str = None,
        name: str = None,
        new_unity_real_name_account: str = None,
        processing_enterprise_certify: bool = None,
    ):
        self.account_certify_type = account_certify_type
        self.auth_alipay = auth_alipay
        self.auth_alipay_domain = auth_alipay_domain
        self.auth_alipay_login_id = auth_alipay_login_id
        self.auth_bei_an_cid = auth_bei_an_cid
        self.auth_domain = auth_domain
        self.certified_from = certified_from
        self.certified_time = certified_time
        self.certify_status = certify_status
        self.cic_certify_from = cic_certify_from
        self.cic_certify_product = cic_certify_product
        self.is_bank_idauth = is_bank_idauth
        self.is_certified = is_certified
        self.license_number = license_number
        self.license_type = license_type
        self.name = name
        self.new_unity_real_name_account = new_unity_real_name_account
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

        if self.auth_alipay_domain is not None:
            result['AuthAlipayDomain'] = self.auth_alipay_domain

        if self.auth_alipay_login_id is not None:
            result['AuthAlipayLoginId'] = self.auth_alipay_login_id

        if self.auth_bei_an_cid is not None:
            result['AuthBeiAnCid'] = self.auth_bei_an_cid

        if self.auth_domain is not None:
            result['AuthDomain'] = self.auth_domain

        if self.certified_from is not None:
            result['CertifiedFrom'] = self.certified_from

        if self.certified_time is not None:
            result['CertifiedTime'] = self.certified_time

        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status

        if self.cic_certify_from is not None:
            result['CicCertifyFrom'] = self.cic_certify_from

        if self.cic_certify_product is not None:
            result['CicCertifyProduct'] = self.cic_certify_product

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

        if self.new_unity_real_name_account is not None:
            result['NewUnityRealNameAccount'] = self.new_unity_real_name_account

        if self.processing_enterprise_certify is not None:
            result['ProcessingEnterpriseCertify'] = self.processing_enterprise_certify

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCertifyType') is not None:
            self.account_certify_type = m.get('AccountCertifyType')

        if m.get('AuthAlipay') is not None:
            self.auth_alipay = m.get('AuthAlipay')

        if m.get('AuthAlipayDomain') is not None:
            self.auth_alipay_domain = m.get('AuthAlipayDomain')

        if m.get('AuthAlipayLoginId') is not None:
            self.auth_alipay_login_id = m.get('AuthAlipayLoginId')

        if m.get('AuthBeiAnCid') is not None:
            self.auth_bei_an_cid = m.get('AuthBeiAnCid')

        if m.get('AuthDomain') is not None:
            self.auth_domain = m.get('AuthDomain')

        if m.get('CertifiedFrom') is not None:
            self.certified_from = m.get('CertifiedFrom')

        if m.get('CertifiedTime') is not None:
            self.certified_time = m.get('CertifiedTime')

        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')

        if m.get('CicCertifyFrom') is not None:
            self.cic_certify_from = m.get('CicCertifyFrom')

        if m.get('CicCertifyProduct') is not None:
            self.cic_certify_product = m.get('CicCertifyProduct')

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

        if m.get('NewUnityRealNameAccount') is not None:
            self.new_unity_real_name_account = m.get('NewUnityRealNameAccount')

        if m.get('ProcessingEnterpriseCertify') is not None:
            self.processing_enterprise_certify = m.get('ProcessingEnterpriseCertify')

        return self

