# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeVersionRequest(DaraModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
        minor: bool = None,
        target_version: str = None,
    ):
        self.fast_mode = fast_mode
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the minor version is upgraded. Default value: true. Valid values:
        # 
        # *   true: The minor version is upgraded.
        # *   false: The major version is upgraded.
        self.minor = minor
        # The version to which you want to upgrade.
        # 
        # This parameter is required.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.minor is not None:
            result['Minor'] = self.minor

        if self.target_version is not None:
            result['TargetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Minor') is not None:
            self.minor = m.get('Minor')

        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')

        return self

