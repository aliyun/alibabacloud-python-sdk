# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class ModelRouterUpdateBillingRuleRequest(DaraModel):
    def __init__(
        self,
        billing_type: str = None,
        effective_time: str = None,
        expire_time: str = None,
        pricing_config: Any = None,
        status: int = None,
        version: int = None,
    ):
        self.billing_type = billing_type
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.pricing_config = pricing_config
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_type is not None:
            result['billingType'] = self.billing_type

        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.pricing_config is not None:
            result['pricingConfig'] = self.pricing_config

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')

        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('pricingConfig') is not None:
            self.pricing_config = m.get('pricingConfig')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

