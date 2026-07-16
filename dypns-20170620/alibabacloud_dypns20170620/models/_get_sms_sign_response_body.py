# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class GetSmsSignResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetSmsSignResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSmsSignResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSmsSignResponseBodyData(DaraModel):
    def __init__(
        self,
        app_url: str = None,
        audit_result: str = None,
        business_license_cert: str = None,
        business_license_cert_id: str = None,
        cert_type: str = None,
        create_date: int = None,
        default_flag: bool = None,
        order_id: str = None,
        organization_code_cert: str = None,
        organization_code_cert_id: str = None,
        sms_sign_name: str = None,
        sms_sign_remark: str = None,
        sms_sign_source: str = None,
        status: str = None,
        tax_registration_cert: str = None,
        tax_registration_cert_id: str = None,
        test_flag: bool = None,
    ):
        self.app_url = app_url
        self.audit_result = audit_result
        self.business_license_cert = business_license_cert
        self.business_license_cert_id = business_license_cert_id
        self.cert_type = cert_type
        self.create_date = create_date
        self.default_flag = default_flag
        self.order_id = order_id
        self.organization_code_cert = organization_code_cert
        self.organization_code_cert_id = organization_code_cert_id
        self.sms_sign_name = sms_sign_name
        self.sms_sign_remark = sms_sign_remark
        self.sms_sign_source = sms_sign_source
        self.status = status
        self.tax_registration_cert = tax_registration_cert
        self.tax_registration_cert_id = tax_registration_cert_id
        self.test_flag = test_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_url is not None:
            result['AppUrl'] = self.app_url

        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result

        if self.business_license_cert is not None:
            result['BusinessLicenseCert'] = self.business_license_cert

        if self.business_license_cert_id is not None:
            result['BusinessLicenseCertId'] = self.business_license_cert_id

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.default_flag is not None:
            result['DefaultFlag'] = self.default_flag

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.organization_code_cert is not None:
            result['OrganizationCodeCert'] = self.organization_code_cert

        if self.organization_code_cert_id is not None:
            result['OrganizationCodeCertId'] = self.organization_code_cert_id

        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name

        if self.sms_sign_remark is not None:
            result['SmsSignRemark'] = self.sms_sign_remark

        if self.sms_sign_source is not None:
            result['SmsSignSource'] = self.sms_sign_source

        if self.status is not None:
            result['Status'] = self.status

        if self.tax_registration_cert is not None:
            result['TaxRegistrationCert'] = self.tax_registration_cert

        if self.tax_registration_cert_id is not None:
            result['TaxRegistrationCertId'] = self.tax_registration_cert_id

        if self.test_flag is not None:
            result['TestFlag'] = self.test_flag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')

        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')

        if m.get('BusinessLicenseCert') is not None:
            self.business_license_cert = m.get('BusinessLicenseCert')

        if m.get('BusinessLicenseCertId') is not None:
            self.business_license_cert_id = m.get('BusinessLicenseCertId')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DefaultFlag') is not None:
            self.default_flag = m.get('DefaultFlag')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrganizationCodeCert') is not None:
            self.organization_code_cert = m.get('OrganizationCodeCert')

        if m.get('OrganizationCodeCertId') is not None:
            self.organization_code_cert_id = m.get('OrganizationCodeCertId')

        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')

        if m.get('SmsSignRemark') is not None:
            self.sms_sign_remark = m.get('SmsSignRemark')

        if m.get('SmsSignSource') is not None:
            self.sms_sign_source = m.get('SmsSignSource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaxRegistrationCert') is not None:
            self.tax_registration_cert = m.get('TaxRegistrationCert')

        if m.get('TaxRegistrationCertId') is not None:
            self.tax_registration_cert_id = m.get('TaxRegistrationCertId')

        if m.get('TestFlag') is not None:
            self.test_flag = m.get('TestFlag')

        return self

