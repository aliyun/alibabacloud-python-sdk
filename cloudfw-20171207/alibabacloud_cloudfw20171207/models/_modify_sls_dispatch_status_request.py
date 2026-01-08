# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySlsDispatchStatusRequest(DaraModel):
    def __init__(
        self,
        dispatch_value: str = None,
        enable_status: bool = None,
        filter_keys: str = None,
        new_region_id: str = None,
    ):
        self.dispatch_value = dispatch_value
        self.enable_status = enable_status
        self.filter_keys = filter_keys
        self.new_region_id = new_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dispatch_value is not None:
            result['DispatchValue'] = self.dispatch_value

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.filter_keys is not None:
            result['FilterKeys'] = self.filter_keys

        if self.new_region_id is not None:
            result['NewRegionId'] = self.new_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchValue') is not None:
            self.dispatch_value = m.get('DispatchValue')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('FilterKeys') is not None:
            self.filter_keys = m.get('FilterKeys')

        if m.get('NewRegionId') is not None:
            self.new_region_id = m.get('NewRegionId')

        return self

