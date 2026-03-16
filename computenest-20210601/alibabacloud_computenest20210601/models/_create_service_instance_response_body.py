# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceInstanceResponseBody(DaraModel):
    def __init__(
        self,
        market_instance_id: str = None,
        order_id: str = None,
        request_id: str = None,
        service_instance_id: str = None,
        status: str = None,
    ):
        # The MartketInstance ID.
        self.market_instance_id = market_instance_id
        # The order ID.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The status of the service instance. Valid values:
        # 
        # *   **Created**
        # *   **Deploying**
        # *   **DeployedFailed**
        # *   **Deployed**
        # *   **Upgrading**
        # *   **Deleting**
        # *   **Deleted**
        # *   **DeletedFailed**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

