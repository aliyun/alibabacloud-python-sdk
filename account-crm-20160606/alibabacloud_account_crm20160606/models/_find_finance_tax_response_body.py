# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class FindFinanceTaxResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        finance_version: main_models.FindFinanceTaxResponseBodyFinanceVersion = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.finance_version = finance_version
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.finance_version:
            self.finance_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.finance_version is not None:
            result['FinanceVersion'] = self.finance_version.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FinanceVersion') is not None:
            temp_model = main_models.FindFinanceTaxResponseBodyFinanceVersion()
            self.finance_version = temp_model.from_map(m.get('FinanceVersion'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FindFinanceTaxResponseBodyFinanceVersion(DaraModel):
    def __init__(
        self,
        finance_tax_certificate_img_name: str = None,
        finance_tax_certificate_img_url: str = None,
        second_finance_tax: str = None,
        second_finance_tax_certificate_img_name: str = None,
        second_finance_tax_certificate_img_url: str = None,
        tax: str = None,
        version: str = None,
    ):
        self.finance_tax_certificate_img_name = finance_tax_certificate_img_name
        self.finance_tax_certificate_img_url = finance_tax_certificate_img_url
        self.second_finance_tax = second_finance_tax
        self.second_finance_tax_certificate_img_name = second_finance_tax_certificate_img_name
        self.second_finance_tax_certificate_img_url = second_finance_tax_certificate_img_url
        self.tax = tax
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finance_tax_certificate_img_name is not None:
            result['FinanceTaxCertificateImgName'] = self.finance_tax_certificate_img_name

        if self.finance_tax_certificate_img_url is not None:
            result['FinanceTaxCertificateImgUrl'] = self.finance_tax_certificate_img_url

        if self.second_finance_tax is not None:
            result['SecondFinanceTax'] = self.second_finance_tax

        if self.second_finance_tax_certificate_img_name is not None:
            result['SecondFinanceTaxCertificateImgName'] = self.second_finance_tax_certificate_img_name

        if self.second_finance_tax_certificate_img_url is not None:
            result['SecondFinanceTaxCertificateImgUrl'] = self.second_finance_tax_certificate_img_url

        if self.tax is not None:
            result['Tax'] = self.tax

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinanceTaxCertificateImgName') is not None:
            self.finance_tax_certificate_img_name = m.get('FinanceTaxCertificateImgName')

        if m.get('FinanceTaxCertificateImgUrl') is not None:
            self.finance_tax_certificate_img_url = m.get('FinanceTaxCertificateImgUrl')

        if m.get('SecondFinanceTax') is not None:
            self.second_finance_tax = m.get('SecondFinanceTax')

        if m.get('SecondFinanceTaxCertificateImgName') is not None:
            self.second_finance_tax_certificate_img_name = m.get('SecondFinanceTaxCertificateImgName')

        if m.get('SecondFinanceTaxCertificateImgUrl') is not None:
            self.second_finance_tax_certificate_img_url = m.get('SecondFinanceTaxCertificateImgUrl')

        if m.get('Tax') is not None:
            self.tax = m.get('Tax')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

