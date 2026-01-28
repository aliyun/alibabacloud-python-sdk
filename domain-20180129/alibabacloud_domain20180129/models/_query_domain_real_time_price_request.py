# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainRealTimePriceRequest(DaraModel):
    def __init__(
        self,
        currency: str = None,
        domain_item: List[main_models.QueryDomainRealTimePriceRequestDomainItem] = None,
    ):
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.domain_item = domain_item

    def validate(self):
        if self.domain_item:
            for v1 in self.domain_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        result['DomainItem'] = []
        if self.domain_item is not None:
            for k1 in self.domain_item:
                result['DomainItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        self.domain_item = []
        if m.get('DomainItem') is not None:
            for k1 in m.get('DomainItem'):
                temp_model = main_models.QueryDomainRealTimePriceRequestDomainItem()
                self.domain_item.append(temp_model.from_map(k1))

        return self

class QueryDomainRealTimePriceRequestDomainItem(DaraModel):
    def __init__(
        self,
        action: str = None,
        domain_name: str = None,
        period: int = None,
        suffix: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.domain_name = domain_name
        self.period = period
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.period is not None:
            result['Period'] = self.period

        if self.suffix is not None:
            result['Suffix'] = self.suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        return self

