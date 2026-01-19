# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApiMarketAttributesResponseBody(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        market_charging_mode: str = None,
        need_charging: str = None,
        request_id: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The billing method used by the Alibaba Cloud Marketplace.
        self.market_charging_mode = market_charging_mode
        # Indicates whether fees are charged.
        self.need_charging = need_charging
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.market_charging_mode is not None:
            result['MarketChargingMode'] = self.market_charging_mode

        if self.need_charging is not None:
            result['NeedCharging'] = self.need_charging

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('MarketChargingMode') is not None:
            self.market_charging_mode = m.get('MarketChargingMode')

        if m.get('NeedCharging') is not None:
            self.need_charging = m.get('NeedCharging')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

