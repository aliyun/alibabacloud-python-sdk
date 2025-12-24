# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceForCreateDesktopOversoldGroupRequest(DaraModel):
    def __init__(
        self,
        concurrence_count: int = None,
        data_disk_size: int = None,
        desktop_type: str = None,
        oversold_user_count: int = None,
        period: int = None,
        period_unit: str = None,
        system_disk_size: int = None,
    ):
        self.concurrence_count = concurrence_count
        self.data_disk_size = data_disk_size
        self.desktop_type = desktop_type
        self.oversold_user_count = oversold_user_count
        self.period = period
        self.period_unit = period_unit
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrence_count is not None:
            result['ConcurrenceCount'] = self.concurrence_count

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.oversold_user_count is not None:
            result['OversoldUserCount'] = self.oversold_user_count

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrenceCount') is not None:
            self.concurrence_count = m.get('ConcurrenceCount')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('OversoldUserCount') is not None:
            self.oversold_user_count = m.get('OversoldUserCount')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

