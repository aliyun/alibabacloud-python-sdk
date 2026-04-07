# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApprovePermissionApplyOrderRequest(DaraModel):
    def __init__(
        self,
        approve_action: int = None,
        approve_comment: str = None,
        flow_id: str = None,
    ):
        # The action for the permission request order. Valid values:
        # 
        # *   1: approve
        # *   2: reject
        # 
        # <!---->
        # 
        # *   0
        # *   1
        # *   2\\.
        # *   3\\.
        # *   4
        # *   5
        # 
        # This parameter is required.
        self.approve_action = approve_action
        # The comment on the order.
        # 
        # This parameter is required.
        self.approve_comment = approve_comment
        # The ID of the permission request order. You can call the ListPermissionApplyOrders operation to obtain the order ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve_action is not None:
            result['ApproveAction'] = self.approve_action

        if self.approve_comment is not None:
            result['ApproveComment'] = self.approve_comment

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveAction') is not None:
            self.approve_action = m.get('ApproveAction')

        if m.get('ApproveComment') is not None:
            self.approve_comment = m.get('ApproveComment')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        return self

