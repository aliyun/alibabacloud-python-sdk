# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetRiskNotificationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRiskNotificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The risk detection result.
        self.data = data
        # The response message.
        self.message = message
        # Id of the request
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
            temp_model = main_models.GetRiskNotificationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetRiskNotificationResponseBodyData(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        is_mute: bool = None,
        risk_code: str = None,
    ):
        # The gateway ID.
        self.gateway_id = gateway_id
        # Indicates whether the notification for the risk item is muted.
        self.is_mute = is_mute
        # The code of the risk item.
        self.risk_code = risk_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.is_mute is not None:
            result['isMute'] = self.is_mute

        if self.risk_code is not None:
            result['riskCode'] = self.risk_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('isMute') is not None:
            self.is_mute = m.get('isMute')

        if m.get('riskCode') is not None:
            self.risk_code = m.get('riskCode')

        return self

