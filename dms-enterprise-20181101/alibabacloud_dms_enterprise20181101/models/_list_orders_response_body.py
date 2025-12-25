# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListOrdersResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        orders: main_models.ListOrdersResponseBodyOrders = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The details about the tickets.
        self.orders = orders
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.orders:
            self.orders.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.orders is not None:
            result['Orders'] = self.orders.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Orders') is not None:
            temp_model = main_models.ListOrdersResponseBodyOrders()
            self.orders = temp_model.from_map(m.get('Orders'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOrdersResponseBodyOrders(DaraModel):
    def __init__(
        self,
        order: List[main_models.ListOrdersResponseBodyOrdersOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for v1 in self.order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Order'] = []
        if self.order is not None:
            for k1 in self.order:
                result['Order'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k1 in m.get('Order'):
                temp_model = main_models.ListOrdersResponseBodyOrdersOrder()
                self.order.append(temp_model.from_map(k1))

        return self

class ListOrdersResponseBodyOrdersOrder(DaraModel):
    def __init__(
        self,
        comment: str = None,
        committer: str = None,
        committer_id: int = None,
        create_time: str = None,
        last_modify_time: str = None,
        order_id: int = None,
        plugin_type: str = None,
        status_code: str = None,
        status_desc: str = None,
    ):
        # The remarks of the ticket.
        self.comment = comment
        # The user who submitted the ticket.
        self.committer = committer
        # The ID of the user who submitted the ticket.
        self.committer_id = committer_id
        # The time when the ticket was created.
        self.create_time = create_time
        # The time when the ticket was last modified.
        self.last_modify_time = last_modify_time
        # The ID of the ticket.
        self.order_id = order_id
        # The type of the ticket.
        self.plugin_type = plugin_type
        # The status code of the ticket. Valid values:
        # 
        # *   **fail**: The ticket fails to be executed.
        # *   **toaudit**: The ticket is waiting for approval.
        # *   **cancel**: The ticket is cancelled.
        # *   **processing**: The ticket is being executed.
        # *   **approved**: The ticket is approved.
        # *   **reject**: The ticket is rejected.
        # *   **success**: The ticket is executed.
        # *   **closed**: The ticket is closed.
        self.status_code = status_code
        # The status description of the ticket.
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.committer is not None:
            result['Committer'] = self.committer

        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Committer') is not None:
            self.committer = m.get('Committer')

        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        return self

