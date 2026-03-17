# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmartAccessGatewaySoftwareResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        smart_agid: str = None,
    ):
        # The ID of the order that you placed to purchase the SAG app instance.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the SAG app instance belongs.
        self.resource_group_id = resource_group_id
        # The ID of the SAG app instance.
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

