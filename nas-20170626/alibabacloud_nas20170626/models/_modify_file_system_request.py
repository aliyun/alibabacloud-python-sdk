# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ModifyFileSystemRequest(DaraModel):
    def __init__(
        self,
        auto_upgrade_config: main_models.ModifyFileSystemRequestAutoUpgradeConfig = None,
        description: str = None,
        file_system_id: str = None,
        options: main_models.ModifyFileSystemRequestOptions = None,
    ):
        # The auto-scaling configuration.
        self.auto_upgrade_config = auto_upgrade_config
        # The description of the file system.
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter. It cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), or hyphens (-).
        self.description = description
        # The file system ID.
        # 
        # - General-purpose NAS: `31a8e4****`.
        # 
        # - Extreme NAS: The ID must start with `extreme-`, for example, `extreme-0015****`.
        # - Cloud Parallel File Storage (CPFS): The ID must start with `cpfs-`, for example, `cpfs-125487****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The options.
        self.options = options

    def validate(self):
        if self.auto_upgrade_config:
            self.auto_upgrade_config.validate()
        if self.options:
            self.options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade_config is not None:
            result['AutoUpgradeConfig'] = self.auto_upgrade_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.options is not None:
            result['Options'] = self.options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpgradeConfig') is not None:
            temp_model = main_models.ModifyFileSystemRequestAutoUpgradeConfig()
            self.auto_upgrade_config = temp_model.from_map(m.get('AutoUpgradeConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Options') is not None:
            temp_model = main_models.ModifyFileSystemRequestOptions()
            self.options = temp_model.from_map(m.get('Options'))

        return self

class ModifyFileSystemRequestOptions(DaraModel):
    def __init__(
        self,
        enable_abe: bool = None,
        enable_oplock: bool = None,
        vsc_access_point_access_only: bool = None,
    ):
        # Specifies whether to enable the SMB Access-Based Enumeration (ABE) feature.
        self.enable_abe = enable_abe
        # Specifies whether the OpLock feature is enabled.
        # 
        # Valid values:
        # - true: Enabled.
        # - false: Not enabled.
        # > Only file systems of the SMB Protocol Type are supported.
        self.enable_oplock = enable_oplock
        # Specifies whether the Lingjun VSC mount target supports only access point-based access.
        self.vsc_access_point_access_only = vsc_access_point_access_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_abe is not None:
            result['EnableABE'] = self.enable_abe

        if self.enable_oplock is not None:
            result['EnableOplock'] = self.enable_oplock

        if self.vsc_access_point_access_only is not None:
            result['VscAccessPointAccessOnly'] = self.vsc_access_point_access_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableABE') is not None:
            self.enable_abe = m.get('EnableABE')

        if m.get('EnableOplock') is not None:
            self.enable_oplock = m.get('EnableOplock')

        if m.get('VscAccessPointAccessOnly') is not None:
            self.vsc_access_point_access_only = m.get('VscAccessPointAccessOnly')

        return self

class ModifyFileSystemRequestAutoUpgradeConfig(DaraModel):
    def __init__(
        self,
        capacity_used_ratio: int = None,
        enabled: bool = None,
        step: int = None,
        time: int = None,
    ):
        # The capacity usage threshold.
        self.capacity_used_ratio = capacity_used_ratio
        # Specifies whether to enable auto-scaling.
        self.enabled = enabled
        # The scaling increment.
        self.step = step
        # The duration.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_used_ratio is not None:
            result['capacityUsedRatio'] = self.capacity_used_ratio

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.step is not None:
            result['step'] = self.step

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacityUsedRatio') is not None:
            self.capacity_used_ratio = m.get('capacityUsedRatio')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('step') is not None:
            self.step = m.get('step')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

