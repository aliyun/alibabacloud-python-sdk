# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryInvoicingCustomerListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryInvoicingCustomerListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if m.get('Data') is not None:
            temp_model = main_models.QueryInvoicingCustomerListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryInvoicingCustomerListResponseBodyData(DaraModel):
    def __init__(
        self,
        customer_invoice_list: main_models.QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList = None,
    ):
        # The information about the invoice.
        self.customer_invoice_list = customer_invoice_list

    def validate(self):
        if self.customer_invoice_list:
            self.customer_invoice_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_invoice_list is not None:
            result['CustomerInvoiceList'] = self.customer_invoice_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerInvoiceList') is not None:
            temp_model = main_models.QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList()
            self.customer_invoice_list = temp_model.from_map(m.get('CustomerInvoiceList'))

        return self

class QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList(DaraModel):
    def __init__(
        self,
        customer_invoice: List[main_models.QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice] = None,
    ):
        self.customer_invoice = customer_invoice

    def validate(self):
        if self.customer_invoice:
            for v1 in self.customer_invoice:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomerInvoice'] = []
        if self.customer_invoice is not None:
            for k1 in self.customer_invoice:
                result['CustomerInvoice'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_invoice = []
        if m.get('CustomerInvoice') is not None:
            for k1 in m.get('CustomerInvoice'):
                temp_model = main_models.QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice()
                self.customer_invoice.append(temp_model.from_map(k1))

        return self

class QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice(DaraModel):
    def __init__(
        self,
        adjust_type: int = None,
        bank: str = None,
        bank_no: str = None,
        customer_type: int = None,
        default_remark: str = None,
        end_cycle: int = None,
        gmt_create: str = None,
        id: int = None,
        invoice_title: str = None,
        issue_type: int = None,
        operating_license_address: str = None,
        operating_license_phone: str = None,
        register_no: str = None,
        start_cycle: int = None,
        status: int = None,
        taxation_license: str = None,
        taxpayer_type: int = None,
        title_change_instructions: str = None,
        type: int = None,
        user_id: int = None,
        user_nick: str = None,
    ):
        # The type of invoice that was changed to.
        self.adjust_type = adjust_type
        # The bank that issues the invoice.
        self.bank = bank
        # The bank account number.
        self.bank_no = bank_no
        # The authentication type of Alipay. Valid values:
        # 
        # *   1: individual
        # *   2: company
        self.customer_type = customer_type
        # The default note that is attached when the title is specified.
        self.default_remark = default_remark
        # The time when the payment ended.
        self.end_cycle = end_cycle
        # The time when the invoice was created. The time was in the yyyy-mm-dd hh:mm:ss format.
        self.gmt_create = gmt_create
        # The ID of the invoice.
        self.id = id
        # The company name in the invoice title.
        self.invoice_title = invoice_title
        # The type of issue.
        self.issue_type = issue_type
        # The address of the business license.
        self.operating_license_address = operating_license_address
        # The phone number of the business license.
        self.operating_license_phone = operating_license_phone
        # The tax registration number.
        self.register_no = register_no
        # The time when the payment started.
        self.start_cycle = start_cycle
        # The status of the invoice title.
        self.status = status
        # The path and file name of the scanned copy of the tax registration certificate.
        self.taxation_license = taxation_license
        # The type of the taxpayer. Valid values:
        # 
        # *   1: general taxpayer
        # *   2: special taxpayer
        self.taxpayer_type = taxpayer_type
        # The instruction document of the invoice title change.
        self.title_change_instructions = title_change_instructions
        # The type of the invoice. Valid values:
        # 
        # *   0: plain value-added tax (VAT) invoice
        # *   1: special VAT invoice
        self.type = type
        # The ID of the user.
        self.user_id = user_id
        # The nickname of the user.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust_type is not None:
            result['AdjustType'] = self.adjust_type

        if self.bank is not None:
            result['Bank'] = self.bank

        if self.bank_no is not None:
            result['BankNo'] = self.bank_no

        if self.customer_type is not None:
            result['CustomerType'] = self.customer_type

        if self.default_remark is not None:
            result['DefaultRemark'] = self.default_remark

        if self.end_cycle is not None:
            result['EndCycle'] = self.end_cycle

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title

        if self.issue_type is not None:
            result['IssueType'] = self.issue_type

        if self.operating_license_address is not None:
            result['OperatingLicenseAddress'] = self.operating_license_address

        if self.operating_license_phone is not None:
            result['OperatingLicensePhone'] = self.operating_license_phone

        if self.register_no is not None:
            result['RegisterNo'] = self.register_no

        if self.start_cycle is not None:
            result['StartCycle'] = self.start_cycle

        if self.status is not None:
            result['Status'] = self.status

        if self.taxation_license is not None:
            result['TaxationLicense'] = self.taxation_license

        if self.taxpayer_type is not None:
            result['TaxpayerType'] = self.taxpayer_type

        if self.title_change_instructions is not None:
            result['TitleChangeInstructions'] = self.title_change_instructions

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustType') is not None:
            self.adjust_type = m.get('AdjustType')

        if m.get('Bank') is not None:
            self.bank = m.get('Bank')

        if m.get('BankNo') is not None:
            self.bank_no = m.get('BankNo')

        if m.get('CustomerType') is not None:
            self.customer_type = m.get('CustomerType')

        if m.get('DefaultRemark') is not None:
            self.default_remark = m.get('DefaultRemark')

        if m.get('EndCycle') is not None:
            self.end_cycle = m.get('EndCycle')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')

        if m.get('IssueType') is not None:
            self.issue_type = m.get('IssueType')

        if m.get('OperatingLicenseAddress') is not None:
            self.operating_license_address = m.get('OperatingLicenseAddress')

        if m.get('OperatingLicensePhone') is not None:
            self.operating_license_phone = m.get('OperatingLicensePhone')

        if m.get('RegisterNo') is not None:
            self.register_no = m.get('RegisterNo')

        if m.get('StartCycle') is not None:
            self.start_cycle = m.get('StartCycle')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaxationLicense') is not None:
            self.taxation_license = m.get('TaxationLicense')

        if m.get('TaxpayerType') is not None:
            self.taxpayer_type = m.get('TaxpayerType')

        if m.get('TitleChangeInstructions') is not None:
            self.title_change_instructions = m.get('TitleChangeInstructions')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

