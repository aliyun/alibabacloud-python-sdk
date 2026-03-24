# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenCdnServiceRequest(DaraModel):
    def __init__(
        self,
        internet_charge_type: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The metering method of Alibaba Cloud CDN. A value of **PayByTraffic** indicates that the metering method is pay-by-data-transfer.
        # 
        # This parameter is required.
        self.internet_charge_type = internet_charge_type
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

