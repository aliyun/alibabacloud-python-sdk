# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSPriceRequest(DaraModel):
    def __init__(
        self,
        ddo_sbilling_mode: str = None,
        ddo_sburstable_domestic_protection: str = None,
        ddo_sburstable_overseas_protection: str = None,
    ):
        # The billing method.
        # 
        # This parameter is required.
        self.ddo_sbilling_mode = ddo_sbilling_mode
        # The instance specifications for the Chinese mainland.
        # 
        # This parameter is required.
        self.ddo_sburstable_domestic_protection = ddo_sburstable_domestic_protection
        # The instance specifications for regions outside the Chinese mainland.
        # 
        # This parameter is required.
        self.ddo_sburstable_overseas_protection = ddo_sburstable_overseas_protection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddo_sbilling_mode is not None:
            result['DDoSBillingMode'] = self.ddo_sbilling_mode

        if self.ddo_sburstable_domestic_protection is not None:
            result['DDoSBurstableDomesticProtection'] = self.ddo_sburstable_domestic_protection

        if self.ddo_sburstable_overseas_protection is not None:
            result['DDoSBurstableOverseasProtection'] = self.ddo_sburstable_overseas_protection

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDoSBillingMode') is not None:
            self.ddo_sbilling_mode = m.get('DDoSBillingMode')

        if m.get('DDoSBurstableDomesticProtection') is not None:
            self.ddo_sburstable_domestic_protection = m.get('DDoSBurstableDomesticProtection')

        if m.get('DDoSBurstableOverseasProtection') is not None:
            self.ddo_sburstable_overseas_protection = m.get('DDoSBurstableOverseasProtection')

        return self

