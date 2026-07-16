# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSecretRotationPolicyRequest(DaraModel):
    def __init__(
        self,
        enable_automatic_rotation: bool = None,
        rotation_interval: str = None,
        secret_name: str = None,
    ):
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # *   true: enables automatic rotation.
        # *   false: does not enable automatic rotation. This is the default value.
        # 
        # This parameter is required.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).
        # 
        # The value is in the `integer[unit]` format.````
        # 
        # The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s indicate a seven-day interval.
        # 
        # >  This parameter is required if you set the EnableAutomaticRotation parameter to true. This parameter is ignored if you set the EnableAutomaticRotation parameter to false or does not specify the EnableAutomaticRotation parameter.
        self.rotation_interval = rotation_interval
        # The name of the secret.
        # 
        # This parameter is required.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation

        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')

        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

