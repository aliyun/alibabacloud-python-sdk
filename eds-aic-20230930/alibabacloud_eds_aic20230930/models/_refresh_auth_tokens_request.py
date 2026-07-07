# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshAuthTokensRequest(DaraModel):
    def __init__(
        self,
        expire_seconds: int = None,
        instance_ids: str = None,
        license_keys: str = None,
    ):
        # The validity period in seconds.
        self.expire_seconds = expire_seconds
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The list of license keys.
        self.license_keys = license_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.license_keys is not None:
            result['LicenseKeys'] = self.license_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LicenseKeys') is not None:
            self.license_keys = m.get('LicenseKeys')

        return self

