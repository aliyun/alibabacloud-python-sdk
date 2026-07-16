# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsSignRequest(DaraModel):
    def __init__(
        self,
        app_url: str = None,
        business_license_cert: str = None,
        cert_type: str = None,
        extend_message: str = None,
        old_sms_sign_name: str = None,
        order_id: str = None,
        organization_code_cert: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sms_sign_name: str = None,
        sms_sign_remark: str = None,
        sms_sign_source: str = None,
        tax_registration_cert: str = None,
    ):
        # This parameter is required.
        self.app_url = app_url
        # This parameter is required.
        self.business_license_cert = business_license_cert
        # This parameter is required.
        self.cert_type = cert_type
        self.extend_message = extend_message
        self.old_sms_sign_name = old_sms_sign_name
        self.order_id = order_id
        self.organization_code_cert = organization_code_cert
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.sms_sign_name = sms_sign_name
        # This parameter is required.
        self.sms_sign_remark = sms_sign_remark
        # This parameter is required.
        self.sms_sign_source = sms_sign_source
        self.tax_registration_cert = tax_registration_cert

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_url is not None:
            result['AppUrl'] = self.app_url

        if self.business_license_cert is not None:
            result['BusinessLicenseCert'] = self.business_license_cert

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.extend_message is not None:
            result['ExtendMessage'] = self.extend_message

        if self.old_sms_sign_name is not None:
            result['OldSmsSignName'] = self.old_sms_sign_name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.organization_code_cert is not None:
            result['OrganizationCodeCert'] = self.organization_code_cert

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name

        if self.sms_sign_remark is not None:
            result['SmsSignRemark'] = self.sms_sign_remark

        if self.sms_sign_source is not None:
            result['SmsSignSource'] = self.sms_sign_source

        if self.tax_registration_cert is not None:
            result['TaxRegistrationCert'] = self.tax_registration_cert

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')

        if m.get('BusinessLicenseCert') is not None:
            self.business_license_cert = m.get('BusinessLicenseCert')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('ExtendMessage') is not None:
            self.extend_message = m.get('ExtendMessage')

        if m.get('OldSmsSignName') is not None:
            self.old_sms_sign_name = m.get('OldSmsSignName')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrganizationCodeCert') is not None:
            self.organization_code_cert = m.get('OrganizationCodeCert')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')

        if m.get('SmsSignRemark') is not None:
            self.sms_sign_remark = m.get('SmsSignRemark')

        if m.get('SmsSignSource') is not None:
            self.sms_sign_source = m.get('SmsSignSource')

        if m.get('TaxRegistrationCert') is not None:
            self.tax_registration_cert = m.get('TaxRegistrationCert')

        return self

