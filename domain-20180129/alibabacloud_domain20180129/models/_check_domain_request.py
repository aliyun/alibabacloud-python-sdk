# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDomainRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        fee_command: str = None,
        fee_currency: str = None,
        fee_period: int = None,
        lang: str = None,
    ):
        # Domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Operation command. Valid values:  
        # - **create**: Purchase.  
        # - **renew**: Renewal.  
        # - **transfer**: Transfer-in.  
        # - **restore**: Redeem.
        self.fee_command = fee_command
        # Currency type. Valid value: **USD** (US Dollar).
        self.fee_currency = fee_currency
        # Registration period in years. Unit: **year**. Valid range: **1** to **10** years.
        self.fee_period = fee_period
        # Language of error messages returned by the API. Valid values:  
        # - **zh**: Chinese.  
        # - **en**: English.  
        # 
        # Default value: **en**.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.fee_command is not None:
            result['FeeCommand'] = self.fee_command

        if self.fee_currency is not None:
            result['FeeCurrency'] = self.fee_currency

        if self.fee_period is not None:
            result['FeePeriod'] = self.fee_period

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FeeCommand') is not None:
            self.fee_command = m.get('FeeCommand')

        if m.get('FeeCurrency') is not None:
            self.fee_currency = m.get('FeeCurrency')

        if m.get('FeePeriod') is not None:
            self.fee_period = m.get('FeePeriod')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

