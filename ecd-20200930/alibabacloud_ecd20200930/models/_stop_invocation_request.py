# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StopInvocationRequest(DaraModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        invoke_id: str = None,
        region_id: str = None,
    ):
        # The ID of cloud desktop N. Valid values of N: 1 to 50.
        self.desktop_id = desktop_id
        # The ID of the execution.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

