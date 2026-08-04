# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateFinanceTaxRequest(DaraModel):
    def __init__(
        self,
        finance_tax: str = None,
        finance_tax_certificate_img_name: str = None,
        hid: int = None,
        second_finance_tax: str = None,
        second_finance_tax_certificate_img_name: str = None,
        second_finance_tax_certificate_img_url: str = None,
        finance_tax_certificate_img_url: str = None,
    ):
        # This parameter is required.
        self.finance_tax = finance_tax
        self.finance_tax_certificate_img_name = finance_tax_certificate_img_name
        # This parameter is required.
        self.hid = hid
        self.second_finance_tax = second_finance_tax
        self.second_finance_tax_certificate_img_name = second_finance_tax_certificate_img_name
        self.second_finance_tax_certificate_img_url = second_finance_tax_certificate_img_url
        self.finance_tax_certificate_img_url = finance_tax_certificate_img_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finance_tax is not None:
            result['FinanceTax'] = self.finance_tax

        if self.finance_tax_certificate_img_name is not None:
            result['FinanceTaxCertificateImgName'] = self.finance_tax_certificate_img_name

        if self.hid is not None:
            result['HId'] = self.hid

        if self.second_finance_tax is not None:
            result['SecondFinanceTax'] = self.second_finance_tax

        if self.second_finance_tax_certificate_img_name is not None:
            result['SecondFinanceTaxCertificateImgName'] = self.second_finance_tax_certificate_img_name

        if self.second_finance_tax_certificate_img_url is not None:
            result['SecondFinanceTaxCertificateImgUrl'] = self.second_finance_tax_certificate_img_url

        if self.finance_tax_certificate_img_url is not None:
            result['financeTaxCertificateImgUrl'] = self.finance_tax_certificate_img_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinanceTax') is not None:
            self.finance_tax = m.get('FinanceTax')

        if m.get('FinanceTaxCertificateImgName') is not None:
            self.finance_tax_certificate_img_name = m.get('FinanceTaxCertificateImgName')

        if m.get('HId') is not None:
            self.hid = m.get('HId')

        if m.get('SecondFinanceTax') is not None:
            self.second_finance_tax = m.get('SecondFinanceTax')

        if m.get('SecondFinanceTaxCertificateImgName') is not None:
            self.second_finance_tax_certificate_img_name = m.get('SecondFinanceTaxCertificateImgName')

        if m.get('SecondFinanceTaxCertificateImgUrl') is not None:
            self.second_finance_tax_certificate_img_url = m.get('SecondFinanceTaxCertificateImgUrl')

        if m.get('financeTaxCertificateImgUrl') is not None:
            self.finance_tax_certificate_img_url = m.get('financeTaxCertificateImgUrl')

        return self

