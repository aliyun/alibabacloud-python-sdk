# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertSwimmingLaneGroupRequest(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        entry_app: str = None,
        logical_region_id: str = None,
        name: str = None,
    ):
        # IDs of all applications that are related to the lane group. Separate multiple applications with commas (,).
        # 
        # This parameter is required.
        self.app_ids = app_ids
        # The ingress application. The application is in the EDAS:{application ID} format.
        # 
        # This parameter is required.
        self.entry_app = entry_app
        # The ID of the custom namespace. The ID is in the physical region ID:custom namespace identifier format. Example: cn-hangzhou:test.
        # 
        # This parameter is required.
        self.logical_region_id = logical_region_id
        # The name of the lane group.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.entry_app is not None:
            result['EntryApp'] = self.entry_app

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('EntryApp') is not None:
            self.entry_app = m.get('EntryApp')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

