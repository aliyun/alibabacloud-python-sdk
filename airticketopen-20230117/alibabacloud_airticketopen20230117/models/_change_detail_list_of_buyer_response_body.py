# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class ChangeDetailListOfBuyerResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.ChangeDetailListOfBuyerResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with the error.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful HTTP requests.
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
            temp_model = main_models.ChangeDetailListOfBuyerResponseBodyData()
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

class ChangeDetailListOfBuyerResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ChangeDetailListOfBuyerResponseBodyDataList] = None,
        pagination: main_models.ChangeDetailListOfBuyerResponseBodyDataPagination = None,
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
                temp_model = main_models.ChangeDetailListOfBuyerResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pagination') is not None:
            temp_model = main_models.ChangeDetailListOfBuyerResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m.get('pagination'))

        return self

class ChangeDetailListOfBuyerResponseBodyDataPagination(DaraModel):
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

class ChangeDetailListOfBuyerResponseBodyDataList(DaraModel):
    def __init__(
        self,
        change_order_num: int = None,
        order_num: int = None,
        order_status: int = None,
        pay_status: int = None,
        transaction_no: str = None,
        utc_create_time: int = None,
    ):
        # The change order number.
        self.change_order_num = change_order_num
        # The order number.
        self.order_num = order_num
        # The application order status. Valid values:
        # - 0: initial state
        # - 1: pending payment
        # - 2: payment successful
        # - 3: change successful
        # - 4: change closed.
        self.order_status = order_status
        # The payment status. Valid values:
        # - 0: initial state
        # - 1: pending payment
        # - 2: payment successful
        # - 3: transaction successful
        # - 4: paid order closed successfully
        # - 5: unpaid order closed successfully.
        self.pay_status = pay_status
        # The transaction number.
        self.transaction_no = transaction_no
        # The order creation time. The value is a UTC timestamp.
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num

        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no

        if self.utc_create_time is not None:
            result['utc_create_time'] = self.utc_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')

        if m.get('utc_create_time') is not None:
            self.utc_create_time = m.get('utc_create_time')

        return self

