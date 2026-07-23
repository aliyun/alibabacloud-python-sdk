# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurchaseDDoSInstanceRequest(DaraModel):
    def __init__(
        self,
        ddo_sbilling_mode: str = None,
        ddo_sburstable_domestic_protection: str = None,
        ddo_sburstable_overseas_protection: str = None,
        site_instance_id: str = None,
    ):
        # This parameter is required.
        self.ddo_sbilling_mode = ddo_sbilling_mode
        # This parameter is required.
        self.ddo_sburstable_domestic_protection = ddo_sburstable_domestic_protection
        # This parameter is required.
        self.ddo_sburstable_overseas_protection = ddo_sburstable_overseas_protection
        # This parameter is required.
        self.site_instance_id = site_instance_id

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

        if self.site_instance_id is not None:
            result['SiteInstanceId'] = self.site_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDoSBillingMode') is not None:
            self.ddo_sbilling_mode = m.get('DDoSBillingMode')

        if m.get('DDoSBurstableDomesticProtection') is not None:
            self.ddo_sburstable_domestic_protection = m.get('DDoSBurstableDomesticProtection')

        if m.get('DDoSBurstableOverseasProtection') is not None:
            self.ddo_sburstable_overseas_protection = m.get('DDoSBurstableOverseasProtection')

        if m.get('SiteInstanceId') is not None:
            self.site_instance_id = m.get('SiteInstanceId')

        return self

