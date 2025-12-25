# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSQLReviewOriginSQLShrinkRequest(DaraModel):
    def __init__(
        self,
        order_action_detail_shrink: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        # The parameters that are used to filter SQL statements involved in the ticket.
        self.order_action_detail_shrink = order_action_detail_shrink
        # The ID of the SQL review ticket. You can call the [CreateSQLReviewOrder](https://help.aliyun.com/document_detail/257777.html) operation to query the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_action_detail_shrink is not None:
            result['OrderActionDetail'] = self.order_action_detail_shrink

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderActionDetail') is not None:
            self.order_action_detail_shrink = m.get('OrderActionDetail')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

