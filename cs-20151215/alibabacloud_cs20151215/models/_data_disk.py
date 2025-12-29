# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataDisk(DaraModel):
    def __init__(
        self,
        auto_format: bool = None,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        file_system: str = None,
        kms_key_id: str = None,
        mount_target: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.auto_format = auto_format
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.device = device
        self.disk_name = disk_name
        self.encrypted = encrypted
        self.file_system = file_system
        self.kms_key_id = kms_key_id
        self.mount_target = mount_target
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_format is not None:
            result['auto_format'] = self.auto_format

        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id

        if self.bursting_enabled is not None:
            result['bursting_enabled'] = self.bursting_enabled

        if self.category is not None:
            result['category'] = self.category

        if self.device is not None:
            result['device'] = self.device

        if self.disk_name is not None:
            result['disk_name'] = self.disk_name

        if self.encrypted is not None:
            result['encrypted'] = self.encrypted

        if self.file_system is not None:
            result['file_system'] = self.file_system

        if self.kms_key_id is not None:
            result['kms_key_id'] = self.kms_key_id

        if self.mount_target is not None:
            result['mount_target'] = self.mount_target

        if self.performance_level is not None:
            result['performance_level'] = self.performance_level

        if self.provisioned_iops is not None:
            result['provisioned_iops'] = self.provisioned_iops

        if self.size is not None:
            result['size'] = self.size

        if self.snapshot_id is not None:
            result['snapshot_id'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_format') is not None:
            self.auto_format = m.get('auto_format')

        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')

        if m.get('bursting_enabled') is not None:
            self.bursting_enabled = m.get('bursting_enabled')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('device') is not None:
            self.device = m.get('device')

        if m.get('disk_name') is not None:
            self.disk_name = m.get('disk_name')

        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')

        if m.get('file_system') is not None:
            self.file_system = m.get('file_system')

        if m.get('kms_key_id') is not None:
            self.kms_key_id = m.get('kms_key_id')

        if m.get('mount_target') is not None:
            self.mount_target = m.get('mount_target')

        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')

        if m.get('provisioned_iops') is not None:
            self.provisioned_iops = m.get('provisioned_iops')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('snapshot_id') is not None:
            self.snapshot_id = m.get('snapshot_id')

        return self

