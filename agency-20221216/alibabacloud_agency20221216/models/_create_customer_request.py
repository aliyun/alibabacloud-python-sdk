# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomerRequest(DaraModel):
    def __init__(
        self,
        customer_name: str = None,
        customer_source: str = None,
        customer_sub_trade: str = None,
        customer_trade: str = None,
        nation: str = None,
    ):
        # Customer\\"s name.
        # 
        # This parameter is required.
        self.customer_name = customer_name
        # The source/channel that allow client to connected with us. Please enumerate with Customer Source.
        # 
        # This parameter is required.
        self.customer_source = customer_source
        # The sub-industry that Customer\\"s business belongs to. Please enumerate with Customer Trade.
        self.customer_sub_trade = customer_sub_trade
        # The industry that Customer\\"s business belongs to. Please enumerate with Customer Trade.
        # 
        # This parameter is required.
        self.customer_trade = customer_trade
        # The region that Customer choose to launch the Cloud Service. Please use ListCountries to confirm the valid region list for current UID.
        # 
        # This parameter is required.
        self.nation = nation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.customer_source is not None:
            result['CustomerSource'] = self.customer_source

        if self.customer_sub_trade is not None:
            result['CustomerSubTrade'] = self.customer_sub_trade

        if self.customer_trade is not None:
            result['CustomerTrade'] = self.customer_trade

        if self.nation is not None:
            result['Nation'] = self.nation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('CustomerSource') is not None:
            self.customer_source = m.get('CustomerSource')

        if m.get('CustomerSubTrade') is not None:
            self.customer_sub_trade = m.get('CustomerSubTrade')

        if m.get('CustomerTrade') is not None:
            self.customer_trade = m.get('CustomerTrade')

        if m.get('Nation') is not None:
            self.nation = m.get('Nation')

        return self

