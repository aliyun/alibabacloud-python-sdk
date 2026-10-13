# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetProductRefResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetProductRefResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetProductRefResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetProductRefResponseBodyData(DaraModel):
    def __init__(
        self,
        apig_ref_config: main_models.HiMarketProductRefConfig = None,
        gateway_id: str = None,
    ):
        # The API configurations currently associated with the API product. The structure is derived from the common struct HiMarketProductRefConfig. This struct contains the gatewayId and apigRefConfig members. The inner apigRefConfig struct contains the mcpServerId, mcpRouteId, mcpServerName, agentApiId, agentApiName, modelApiId, and modelApiName members.
        self.apig_ref_config = apig_ref_config
        # The gateway ID. The ID of the gateway instance where the association configuration of the API product resides.
        self.gateway_id = gateway_id

    def validate(self):
        if self.apig_ref_config:
            self.apig_ref_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apig_ref_config is not None:
            result['apigRefConfig'] = self.apig_ref_config.to_map()

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apigRefConfig') is not None:
            temp_model = main_models.HiMarketProductRefConfig()
            self.apig_ref_config = temp_model.from_map(m.get('apigRefConfig'))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        return self

