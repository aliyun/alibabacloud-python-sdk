# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateDesktopGroupResponseBody(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_group_ids: List[str] = None,
        order_ids: List[str] = None,
        request_id: str = None,
    ):
        # The ID of the shared group.
        self.desktop_group_id = desktop_group_id
        # The IDs of the shared groups.
        self.desktop_group_ids = desktop_group_ids
        # The IDs of the orders.
        self.order_ids = order_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_ids is not None:
            result['DesktopGroupIds'] = self.desktop_group_ids

        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupIds') is not None:
            self.desktop_group_ids = m.get('DesktopGroupIds')

        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

