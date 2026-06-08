# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDeletionProtectionRequest(DaraModel):
    def __init__(
        self,
        deletion_protection: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        # Indicates whether stack deletion protection is enabled. Valid values:
        # 
        # *   Enabled: enables the stack deletion protection.
        # *   Disabled (default): Resource stack deletion protection is Disabled. You can use the console or API(DeleteStack) to release the stack resources.
        # 
        # >  The deletion of nested stacks is the same as the root stack.
        # 
        # This parameter is required.
        self.deletion_protection = deletion_protection
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the stack.
        # 
        # The delete protection attribute of a nested stack is determined by the root stack and remains unchanged from the root stack.
        # 
        # This parameter is required.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

