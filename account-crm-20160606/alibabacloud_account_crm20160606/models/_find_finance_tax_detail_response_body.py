# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class FindFinanceTaxDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        finance: main_models.FindFinanceTaxDetailResponseBodyFinance = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.finance = finance
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.finance:
            self.finance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.finance is not None:
            result['Finance'] = self.finance.to_map()

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

        if m.get('Finance') is not None:
            temp_model = main_models.FindFinanceTaxDetailResponseBodyFinance()
            self.finance = temp_model.from_map(m.get('Finance'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FindFinanceTaxDetailResponseBodyFinance(DaraModel):
    def __init__(
        self,
        finance_tax_certificate_img_name: str = None,
        tax: str = None,
        finance_tax_certificate_img_url: str = None,
        second_finance_tax: str = None,
        second_finance_tax_certificate_img_name: str = None,
        second_finance_tax_certificate_img_url: str = None,
    ):
        self.finance_tax_certificate_img_name = finance_tax_certificate_img_name
        self.tax = tax
        self.finance_tax_certificate_img_url = finance_tax_certificate_img_url
        self.second_finance_tax = second_finance_tax
        self.second_finance_tax_certificate_img_name = second_finance_tax_certificate_img_name
        self.second_finance_tax_certificate_img_url = second_finance_tax_certificate_img_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finance_tax_certificate_img_name is not None:
            result['FinanceTaxCertificateImgName'] = self.finance_tax_certificate_img_name

        if self.tax is not None:
            result['Tax'] = self.tax

        if self.finance_tax_certificate_img_url is not None:
            result['financeTaxCertificateImgUrl'] = self.finance_tax_certificate_img_url

        if self.second_finance_tax is not None:
            result['secondFinanceTax'] = self.second_finance_tax

        if self.second_finance_tax_certificate_img_name is not None:
            result['secondFinanceTaxCertificateImgName'] = self.second_finance_tax_certificate_img_name

        if self.second_finance_tax_certificate_img_url is not None:
            result['secondFinanceTaxCertificateImgUrl'] = self.second_finance_tax_certificate_img_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinanceTaxCertificateImgName') is not None:
            self.finance_tax_certificate_img_name = m.get('FinanceTaxCertificateImgName')

        if m.get('Tax') is not None:
            self.tax = m.get('Tax')

        if m.get('financeTaxCertificateImgUrl') is not None:
            self.finance_tax_certificate_img_url = m.get('financeTaxCertificateImgUrl')

        if m.get('secondFinanceTax') is not None:
            self.second_finance_tax = m.get('secondFinanceTax')

        if m.get('secondFinanceTaxCertificateImgName') is not None:
            self.second_finance_tax_certificate_img_name = m.get('secondFinanceTaxCertificateImgName')

        if m.get('secondFinanceTaxCertificateImgUrl') is not None:
            self.second_finance_tax_certificate_img_url = m.get('secondFinanceTaxCertificateImgUrl')

        return self

