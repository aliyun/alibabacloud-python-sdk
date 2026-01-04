# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnsServiceRequest(DaraModel):
    def __init__(
        self,
        ens_service_id: str = None,
        order_type: str = None,
    ):
        # The ID of the resource that you want to obtain. You can specify only one ID in a request.
        # 
        # This parameter is required.
        self.ens_service_id = ens_service_id
        # The operation to perform after you preview the created edge service. Valid values:
        # 
        # *   **Buy**: create
        # *   **Upgrade**: change
        # 
        # This parameter is required.
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_service_id is not None:
            result['EnsServiceId'] = self.ens_service_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsServiceId') is not None:
            self.ens_service_id = m.get('EnsServiceId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

