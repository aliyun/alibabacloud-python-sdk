# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class AccountFlowListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.AccountFlowListResponseBodyData = None,
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
            temp_model = main_models.AccountFlowListResponseBodyData()
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

class AccountFlowListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.AccountFlowListResponseBodyDataList] = None,
        pagination: main_models.AccountFlowListResponseBodyDataPagination = None,
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
                temp_model = main_models.AccountFlowListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pagination') is not None:
            temp_model = main_models.AccountFlowListResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m.get('pagination'))

        return self

class AccountFlowListResponseBodyDataPagination(DaraModel):
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

class AccountFlowListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        after_available_amount: float = None,
        before_available_amount: float = None,
        change_order_num: int = None,
        flow_id: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        op_amount: float = None,
        op_type: int = None,
        order_num: int = None,
        order_type: int = None,
        out_order_num: str = None,
        refund_order_num: int = None,
    ):
        # The available balance after the operation, in CNY.
        self.after_available_amount = after_available_amount
        # The available balance before the operation, in CNY.
        self.before_available_amount = before_available_amount
        # The change order number. This value is not empty if the flow is related to a ticket change.
        self.change_order_num = change_order_num
        # The flow ID.
        self.flow_id = flow_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The operation amount, in CNY.
        self.op_amount = op_amount
        # The operation type. Valid values:
        # - 1: payment
        # - 2: refund
        # - 3: top-up.
        self.op_type = op_type
        # The original order number.
        self.order_num = order_num
        # The order type. Valid values:
        # - 0: original transaction
        # - 1: change order payment
        # - 2: refund.
        self.order_type = order_type
        # The external order number of the original order.
        self.out_order_num = out_order_num
        # The refund order number. This value is not empty if the flow is related to a refund.
        self.refund_order_num = refund_order_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_available_amount is not None:
            result['after_available_amount'] = self.after_available_amount

        if self.before_available_amount is not None:
            result['before_available_amount'] = self.before_available_amount

        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num

        if self.flow_id is not None:
            result['flow_id'] = self.flow_id

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.op_amount is not None:
            result['op_amount'] = self.op_amount

        if self.op_type is not None:
            result['op_type'] = self.op_type

        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.order_type is not None:
            result['order_type'] = self.order_type

        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num

        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('after_available_amount') is not None:
            self.after_available_amount = m.get('after_available_amount')

        if m.get('before_available_amount') is not None:
            self.before_available_amount = m.get('before_available_amount')

        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')

        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('op_amount') is not None:
            self.op_amount = m.get('op_amount')

        if m.get('op_type') is not None:
            self.op_type = m.get('op_type')

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')

        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')

        return self

