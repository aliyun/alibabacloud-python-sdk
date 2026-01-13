# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSubCrowdResponseBody(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        quantity: str = None,
        request_id: str = None,
        source: str = None,
        users: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.quantity = quantity
        # Id of the request
        self.request_id = request_id
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source is not None:
            result['Source'] = self.source

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

