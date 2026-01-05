# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConversionDataIntlRequest(DaraModel):
    def __init__(
        self,
        conversion_rate: str = None,
        owner_id: int = None,
        report_time: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The conversion rate.
        # 
        # > The value of this parameter is a double, and ranges from 0 to 1.
        # 
        # This parameter is required.
        self.conversion_rate = conversion_rate
        self.owner_id = owner_id
        # The time point at which the conversion rate is monitored. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > If you do not specify this parameter, the current timestamp is used by default.
        self.report_time = report_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversion_rate is not None:
            result['ConversionRate'] = self.conversion_rate

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.report_time is not None:
            result['ReportTime'] = self.report_time

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversionRate') is not None:
            self.conversion_rate = m.get('ConversionRate')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

