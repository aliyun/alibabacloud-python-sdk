# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeInvoiceForIsvResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        result: List[main_models.DescribeInvoiceForIsvResponseBodyResult] = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeInvoiceForIsvResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeInvoiceForIsvResponseBodyResult(DaraModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        check_notice: str = None,
        create_time_str: str = None,
        evaluate_list: List[main_models.DescribeInvoiceForIsvResponseBodyResultEvaluateList] = None,
        id: str = None,
        invoice_id: str = None,
        invoice_list: List[main_models.DescribeInvoiceForIsvResponseBodyResultInvoiceList] = None,
        material_type: str = None,
        modified_time: str = None,
        modified_time_str: str = None,
        price: str = None,
        receipt_user_info_dto: main_models.DescribeInvoiceForIsvResponseBodyResultReceiptUserInfoDto = None,
        status: str = None,
        title: str = None,
        type: str = None,
        user_address_dto: main_models.DescribeInvoiceForIsvResponseBodyResultUserAddressDto = None,
        user_notice: str = None,
    ):
        self.aliyun_pk = aliyun_pk
        self.check_notice = check_notice
        self.create_time_str = create_time_str
        self.evaluate_list = evaluate_list
        self.id = id
        self.invoice_id = invoice_id
        self.invoice_list = invoice_list
        self.material_type = material_type
        self.modified_time = modified_time
        self.modified_time_str = modified_time_str
        self.price = price
        self.receipt_user_info_dto = receipt_user_info_dto
        self.status = status
        self.title = title
        self.type = type
        self.user_address_dto = user_address_dto
        self.user_notice = user_notice

    def validate(self):
        if self.evaluate_list:
            for v1 in self.evaluate_list:
                 if v1:
                    v1.validate()
        if self.invoice_list:
            for v1 in self.invoice_list:
                 if v1:
                    v1.validate()
        if self.receipt_user_info_dto:
            self.receipt_user_info_dto.validate()
        if self.user_address_dto:
            self.user_address_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk

        if self.check_notice is not None:
            result['CheckNotice'] = self.check_notice

        if self.create_time_str is not None:
            result['CreateTimeStr'] = self.create_time_str

        result['EvaluateList'] = []
        if self.evaluate_list is not None:
            for k1 in self.evaluate_list:
                result['EvaluateList'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.invoice_id is not None:
            result['InvoiceId'] = self.invoice_id

        result['InvoiceList'] = []
        if self.invoice_list is not None:
            for k1 in self.invoice_list:
                result['InvoiceList'].append(k1.to_map() if k1 else None)

        if self.material_type is not None:
            result['MaterialType'] = self.material_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modified_time_str is not None:
            result['ModifiedTimeStr'] = self.modified_time_str

        if self.price is not None:
            result['Price'] = self.price

        if self.receipt_user_info_dto is not None:
            result['ReceiptUserInfoDto'] = self.receipt_user_info_dto.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.user_address_dto is not None:
            result['UserAddressDto'] = self.user_address_dto.to_map()

        if self.user_notice is not None:
            result['UserNotice'] = self.user_notice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')

        if m.get('CheckNotice') is not None:
            self.check_notice = m.get('CheckNotice')

        if m.get('CreateTimeStr') is not None:
            self.create_time_str = m.get('CreateTimeStr')

        self.evaluate_list = []
        if m.get('EvaluateList') is not None:
            for k1 in m.get('EvaluateList'):
                temp_model = main_models.DescribeInvoiceForIsvResponseBodyResultEvaluateList()
                self.evaluate_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InvoiceId') is not None:
            self.invoice_id = m.get('InvoiceId')

        self.invoice_list = []
        if m.get('InvoiceList') is not None:
            for k1 in m.get('InvoiceList'):
                temp_model = main_models.DescribeInvoiceForIsvResponseBodyResultInvoiceList()
                self.invoice_list.append(temp_model.from_map(k1))

        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifiedTimeStr') is not None:
            self.modified_time_str = m.get('ModifiedTimeStr')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('ReceiptUserInfoDto') is not None:
            temp_model = main_models.DescribeInvoiceForIsvResponseBodyResultReceiptUserInfoDto()
            self.receipt_user_info_dto = temp_model.from_map(m.get('ReceiptUserInfoDto'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserAddressDto') is not None:
            temp_model = main_models.DescribeInvoiceForIsvResponseBodyResultUserAddressDto()
            self.user_address_dto = temp_model.from_map(m.get('UserAddressDto'))

        if m.get('UserNotice') is not None:
            self.user_notice = m.get('UserNotice')

        return self

class DescribeInvoiceForIsvResponseBodyResultUserAddressDto(DaraModel):
    def __init__(
        self,
        addressee: str = None,
        aliyun_pk: str = None,
        biz_type: str = None,
        delivery_address: str = None,
        emails: str = None,
        phone: str = None,
        postal_code: str = None,
    ):
        self.addressee = addressee
        self.aliyun_pk = aliyun_pk
        self.biz_type = biz_type
        self.delivery_address = delivery_address
        self.emails = emails
        self.phone = phone
        self.postal_code = postal_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addressee is not None:
            result['Addressee'] = self.addressee

        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address

        if self.emails is not None:
            result['Emails'] = self.emails

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addressee') is not None:
            self.addressee = m.get('Addressee')

        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')

        if m.get('Emails') is not None:
            self.emails = m.get('Emails')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        return self

class DescribeInvoiceForIsvResponseBodyResultReceiptUserInfoDto(DaraModel):
    def __init__(
        self,
        tax_number: str = None,
    ):
        self.tax_number = tax_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tax_number is not None:
            result['TaxNumber'] = self.tax_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaxNumber') is not None:
            self.tax_number = m.get('TaxNumber')

        return self

class DescribeInvoiceForIsvResponseBodyResultInvoiceList(DaraModel):
    def __init__(
        self,
        id: str = None,
        invoice_amount: str = None,
    ):
        self.id = id
        self.invoice_amount = invoice_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')

        return self

class DescribeInvoiceForIsvResponseBodyResultEvaluateList(DaraModel):
    def __init__(
        self,
        agent: bool = None,
        amount: str = None,
        biz_time_str: str = None,
        id: str = None,
        order_type: str = None,
        out_biz_id: str = None,
        product_code: str = None,
        product_name: str = None,
        real_aliyun_id: str = None,
        real_aliyun_pk: str = None,
    ):
        self.agent = agent
        self.amount = amount
        self.biz_time_str = biz_time_str
        self.id = id
        self.order_type = order_type
        self.out_biz_id = out_biz_id
        self.product_code = product_code
        self.product_name = product_name
        self.real_aliyun_id = real_aliyun_id
        self.real_aliyun_pk = real_aliyun_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.biz_time_str is not None:
            result['BizTimeStr'] = self.biz_time_str

        if self.id is not None:
            result['Id'] = self.id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.real_aliyun_id is not None:
            result['RealAliyunId'] = self.real_aliyun_id

        if self.real_aliyun_pk is not None:
            result['RealAliyunPk'] = self.real_aliyun_pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('BizTimeStr') is not None:
            self.biz_time_str = m.get('BizTimeStr')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RealAliyunId') is not None:
            self.real_aliyun_id = m.get('RealAliyunId')

        if m.get('RealAliyunPk') is not None:
            self.real_aliyun_pk = m.get('RealAliyunPk')

        return self

