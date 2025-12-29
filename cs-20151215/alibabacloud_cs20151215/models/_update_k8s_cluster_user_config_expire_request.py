# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateK8sClusterUserConfigExpireRequest(DaraModel):
    def __init__(
        self,
        expire_hour: int = None,
        user: str = None,
    ):
        # Specifies the expiration time of the kubeconfig file. Unit: hours.
        # 
        # Valid values: [1, 1876000]. The maximum value is 100 years.
        # 
        # This parameter is required.
        self.expire_hour = expire_hour
        # The RAM user ID.
        # 
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_hour is not None:
            result['expire_hour'] = self.expire_hour

        if self.user is not None:
            result['user'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire_hour') is not None:
            self.expire_hour = m.get('expire_hour')

        if m.get('user') is not None:
            self.user = m.get('user')

        return self

