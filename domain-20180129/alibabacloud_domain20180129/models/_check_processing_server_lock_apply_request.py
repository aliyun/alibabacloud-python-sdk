# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckProcessingServerLockApplyRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        fee_period: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.fee_period = fee_period
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.fee_period is not None:
            result['FeePeriod'] = self.fee_period

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FeePeriod') is not None:
            self.fee_period = m.get('FeePeriod')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

