# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class OrderListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.OrderListResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with the error.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful requests.
        self.status = status
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_data is not None:
            result['error_data'] = self.error_data

        if self.error_msg is not None:
            result['error_msg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.OrderListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')

        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class OrderListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.OrderListResponseBodyDataList] = None,
        pagination: main_models.OrderListResponseBodyDataPagination = None,
    ):
        # The data list.
        self.list = list
        # The pagination information.
        self.pagination = pagination

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.OrderListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pagination') is not None:
            temp_model = main_models.OrderListResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m.get('pagination'))

        return self

class OrderListResponseBodyDataPagination(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of records per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['current_page'] = self.current_page

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        if self.total_page is not None:
            result['total_page'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current_page') is not None:
            self.current_page = m.get('current_page')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')

        return self

class OrderListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        book_time: int = None,
        order_num: int = None,
        order_status: str = None,
        out_order_num: str = None,
        passenger_list: List[main_models.OrderListResponseBodyDataListPassengerList] = None,
        pay_status: str = None,
        pay_time: int = None,
        promotion_price: float = None,
        real_pay_price: float = None,
        session_nick: str = None,
        succeed_time: int = None,
        total_price: float = None,
        transaction_no: str = None,
    ):
        # The booking time (order creation time). The value is a 13-digit UNIX timestamp.
        self.book_time = book_time
        # The order number.
        self.order_num = order_num
        # The order status. Valid values:
        # - 2: order creation succeeded.
        # - 3: order paid.
        # - 4: order succeeded.
        # - 5: order closed.
        self.order_status = order_status
        # The external order number.
        self.out_order_num = out_order_num
        # The passenger list.
        self.passenger_list = passenger_list
        # The payment status. Valid values:
        # - 0: initialized.
        # - 1: creation succeeded.
        # - 2: payment succeeded.
        # - 4: transaction closed.
        self.pay_status = pay_status
        # The payment time. The value is a 13-digit UNIX timestamp.
        self.pay_time = pay_time
        # The discount amount. Unit: yuan.
        self.promotion_price = promotion_price
        # The actual payment amount. Unit: yuan.
        self.real_pay_price = real_pay_price
        # The buyer nickname.
        self.session_nick = session_nick
        # The ticketing time. The value is a 13-digit UNIX timestamp.
        self.succeed_time = succeed_time
        # The total price of the order. Unit: yuan.
        self.total_price = total_price
        # The transaction serial number.
        self.transaction_no = transaction_no

    def validate(self):
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.book_time is not None:
            result['book_time'] = self.book_time

        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.promotion_price is not None:
            result['promotion_price'] = self.promotion_price

        if self.real_pay_price is not None:
            result['real_pay_price'] = self.real_pay_price

        if self.session_nick is not None:
            result['session_nick'] = self.session_nick

        if self.succeed_time is not None:
            result['succeed_time'] = self.succeed_time

        if self.total_price is not None:
            result['total_price'] = self.total_price

        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.OrderListResponseBodyDataListPassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('promotion_price') is not None:
            self.promotion_price = m.get('promotion_price')

        if m.get('real_pay_price') is not None:
            self.real_pay_price = m.get('real_pay_price')

        if m.get('session_nick') is not None:
            self.session_nick = m.get('session_nick')

        if m.get('succeed_time') is not None:
            self.succeed_time = m.get('succeed_time')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')

        return self

class OrderListResponseBodyDataListPassengerList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        credential: main_models.OrderListResponseBodyDataListPassengerListCredential = None,
        first_name: str = None,
        gender: int = None,
        last_name: str = None,
        mobile_country_code: str = None,
        mobile_phone_number: str = None,
        nationality: str = None,
        type: int = None,
    ):
        # The date of birth in the yyyyMMdd format.
        self.birthday = birthday
        # The credential information.
        self.credential = credential
        # The first name.
        self.first_name = first_name
        # The gender. Valid values:
        # - 0: MALE.
        # - 1: FEMALE.
        self.gender = gender
        # The last name.
        self.last_name = last_name
        # The country code of the mobile phone number.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number.
        self.mobile_phone_number = mobile_phone_number
        # The two-letter nationality code.
        self.nationality = nationality
        # The passenger type. Valid values:
        # - 0: adult.
        # - 1: child.
        # - 8: infant.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('credential') is not None:
            temp_model = main_models.OrderListResponseBodyDataListPassengerListCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class OrderListResponseBodyDataListPassengerListCredential(DaraModel):
    def __init__(
        self,
        cert_issue_place: str = None,
        credential_num: str = None,
        credential_type: int = None,
        expire_date: str = None,
    ):
        # The place of issue, represented as a two-letter code.
        self.cert_issue_place = cert_issue_place
        # The credential number.
        self.credential_num = credential_num
        # The credential type. Valid values:
        # - 0: ID card.
        # - 1: passport.
        # - 2: student ID.
        # - 3: military ID.
        # - 4: Home Return Permit.
        # - 5: Taiwan Compatriot Permit.
        # - 6: Hong Kong and Macao Travel Permit.
        # - 7: international seafarer certificate.
        # - 8: Foreigner Permanent Residence Card.
        # - 10: police officer ID.
        # - 11: soldier ID.
        # - 12: Taiwan Travel Permit.
        # - 13: Taiwan Entry Permit.
        # - 14: household register.
        # - 15: birth certificate.
        # - 16: driver license.
        # - 17: Hong Kong and Macao Resident Residence Permit.
        # - 18: Taiwan Resident Residence Permit.
        self.credential_type = credential_type
        # The credential expiration date.
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_num is not None:
            result['credential_num'] = self.credential_num

        if self.credential_type is not None:
            result['credential_type'] = self.credential_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')

        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        return self

