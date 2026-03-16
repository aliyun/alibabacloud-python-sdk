# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveMfaDeviceRequest(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        business_channel: str = None,
        serial_number: str = None,
    ):
        # The address of the AD office network.
        self.ad_domain = ad_domain
        self.business_channel = business_channel
        # The serial number of the virtual MFA device. You can call the [DescribeMfaDevices](~~DescribeMfaDevices~~) operation to get this information.
        # 
        # This parameter is required.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

