# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceInstanceRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        new_disk_size: str = None,
        reason: str = None,
    ):
        # The scheduling behavior to update for the instance in the dedicated resource group. Valid values:
        # 
        # - Uncordon: Allows services to be scheduled to the instance.
        # 
        # - Cordon: Prevents services from being scheduled to the instance.
        # 
        # - Drain: Evicts the service instances that are running on the instance.
        # 
        # This parameter is required.
        self.action = action
        self.new_disk_size = new_disk_size
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.new_disk_size is not None:
            result['NewDiskSize'] = self.new_disk_size

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('NewDiskSize') is not None:
            self.new_disk_size = m.get('NewDiskSize')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

