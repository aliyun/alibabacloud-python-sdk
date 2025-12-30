# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDomainBackupRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        period_type: str = None,
    ):
        # The domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The backup cycle. Valid values:
        # 
        # *   DAY: backs up data on a daily basis.
        # *   HOUR: backs up data on an hourly basis.
        # 
        # This parameter is required.
        self.period_type = period_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        return self

