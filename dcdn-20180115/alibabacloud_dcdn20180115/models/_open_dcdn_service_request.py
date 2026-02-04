# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenDcdnServiceRequest(DaraModel):
    def __init__(
        self,
        bill_type: str = None,
        owner_id: int = None,
        security_token: str = None,
        websocket_bill_type: str = None,
    ):
        # The metering method of DCDN. Valid values:
        # 
        # *   **PayByTraffic**: pay-by-traffic
        # *   **PayByBandwidth**: pay-by-bandwidth
        # 
        # This parameter is required.
        self.bill_type = bill_type
        self.owner_id = owner_id
        self.security_token = security_token
        # The metering method of WebSocket. Valid values:
        # 
        # *   **websockettraffic**: pay-by-data-transfer
        # *   **websocketbps**: pay-by-bandwidth
        # 
        # This parameter is required.
        self.websocket_bill_type = websocket_bill_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.websocket_bill_type is not None:
            result['WebsocketBillType'] = self.websocket_bill_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('WebsocketBillType') is not None:
            self.websocket_bill_type = m.get('WebsocketBillType')

        return self

