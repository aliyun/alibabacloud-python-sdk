# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListRecentChangeOrderResponseBody(DaraModel):
    def __init__(
        self,
        change_order_list: main_models.ListRecentChangeOrderResponseBodyChangeOrderList = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.change_order_list = change_order_list
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.change_order_list:
            self.change_order_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_list is not None:
            result['ChangeOrderList'] = self.change_order_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderList') is not None:
            temp_model = main_models.ListRecentChangeOrderResponseBodyChangeOrderList()
            self.change_order_list = temp_model.from_map(m.get('ChangeOrderList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRecentChangeOrderResponseBodyChangeOrderList(DaraModel):
    def __init__(
        self,
        change_order: List[main_models.ListRecentChangeOrderResponseBodyChangeOrderListChangeOrder] = None,
    ):
        self.change_order = change_order

    def validate(self):
        if self.change_order:
            for v1 in self.change_order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChangeOrder'] = []
        if self.change_order is not None:
            for k1 in self.change_order:
                result['ChangeOrder'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_order = []
        if m.get('ChangeOrder') is not None:
            for k1 in m.get('ChangeOrder'):
                temp_model = main_models.ListRecentChangeOrderResponseBodyChangeOrderListChangeOrder()
                self.change_order.append(temp_model.from_map(k1))

        return self

class ListRecentChangeOrderResponseBodyChangeOrderListChangeOrder(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        batch_count: int = None,
        batch_type: str = None,
        change_order_description: str = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        create_user_id: str = None,
        finish_time: str = None,
        group_id: str = None,
        source: str = None,
        status: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.batch_count = batch_count
        self.batch_type = batch_type
        self.change_order_description = change_order_description
        self.change_order_id = change_order_id
        self.co_type = co_type
        self.co_type_code = co_type_code
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.finish_time = finish_time
        self.group_id = group_id
        self.source = source
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count

        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.change_order_description is not None:
            result['ChangeOrderDescription'] = self.change_order_description

        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.co_type is not None:
            result['CoType'] = self.co_type

        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')

        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('ChangeOrderDescription') is not None:
            self.change_order_description = m.get('ChangeOrderDescription')

        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')

        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

