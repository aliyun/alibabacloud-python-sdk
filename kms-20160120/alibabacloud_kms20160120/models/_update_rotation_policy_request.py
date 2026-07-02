# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRotationPolicyRequest(DaraModel):
    def __init__(
        self,
        enable_automatic_rotation: bool = None,
        key_id: str = None,
        rotation_interval: str = None,
    ):
        # Specifies whether to enable automatic key rotation. Valid values:
        # 
        # - true: enables automatic key rotation.
        # 
        # - false: disables automatic key rotation.
        # 
        # This parameter is required.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The period of automatic key rotation. Specify the value in the integer[unit] format. The following units are supported: d (day), h (hour), m (minute), and s (second). For example, you can use either 7d or 604800s to specify a seven-day period. The period can range from 7 days to 730 days.
        # 
        # > If you set the EnableAutomaticRotation parameter to true, you must also specify this parameter. If you set the EnableAutomaticRotation parameter to false, you can leave this parameter unspecified.
        self.rotation_interval = rotation_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')

        return self

