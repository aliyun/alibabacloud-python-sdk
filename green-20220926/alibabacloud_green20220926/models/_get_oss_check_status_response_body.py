# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssCheckStatusResponseBody(DaraModel):
    def __init__(
        self,
        bid: str = None,
        buy: bool = None,
        commodity_code: str = None,
        indebt: bool = None,
        ram_status: str = None,
        request_id: str = None,
        sls_status: str = None,
    ):
        # Bid.
        self.bid = bid
        # Whether a product has been activated on Alibaba Cloud.
        self.buy = buy
        # Commodity code.
        self.commodity_code = commodity_code
        # Whether there is an outstanding payment.
        self.indebt = indebt
        # Whether internal security is authorized.
        self.ram_status = ram_status
        # ID assigned by the backend, used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Whether log analysis function is authorized.
        self.sls_status = sls_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.buy is not None:
            result['Buy'] = self.buy

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.indebt is not None:
            result['Indebt'] = self.indebt

        if self.ram_status is not None:
            result['RamStatus'] = self.ram_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Buy') is not None:
            self.buy = m.get('Buy')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Indebt') is not None:
            self.indebt = m.get('Indebt')

        if m.get('RamStatus') is not None:
            self.ram_status = m.get('RamStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')

        return self

