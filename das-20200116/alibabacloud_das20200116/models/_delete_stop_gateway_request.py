# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStopGatewayRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
        # The ID that can uniquely identify the DBGateway. You can obtain the DBGateway ID by calling the [DescribeCloudbenchTask](https://help.aliyun.com/document_detail/230669.html) operation. The DBGateway ID is the value of the **ClientGatewayId** field in the response.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        return self

