# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApplicationRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        name: str = None,
        region_id: str = None,
        retain_resource: bool = None,
    ):
        # Specifies whether to forcibly delete the application. Valid values:
        # 
        # *   true
        # *   false
        self.force = force
        # The application name.
        # 
        # This parameter is required.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # Specifies whether to retain resources created by application manager when deleting the application. Valid values:
        # - true
        # - false
        self.retain_resource = retain_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retain_resource is not None:
            result['RetainResource'] = self.retain_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetainResource') is not None:
            self.retain_resource = m.get('RetainResource')

        return self

