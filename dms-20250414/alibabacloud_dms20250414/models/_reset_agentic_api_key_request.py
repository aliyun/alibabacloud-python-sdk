# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetAgenticApiKeyRequest(DaraModel):
    def __init__(
        self,
        expire_after_seconds: int = None,
        id: int = None,
    ):
        # The validity period of the new Access Token starting from the time of this reset, in seconds. Valid values: 1 to 31536000 (approximately 365 days). If you do not specify this parameter, the original expiration time of the Access Token is retained. This parameter is required when the target Access Token has already expired. Otherwise, the system retains the past expiration time and issues an Access Token that is invalid upon creation, and the request is rejected.
        self.expire_after_seconds = expire_after_seconds
        # The ID of the data gateway Access Token to reset. This value is the same as the Id returned by the create and query operations. Only the creator of the Access Token can reset it, and the target Access Token cannot be in a revoked state.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_after_seconds is not None:
            result['ExpireAfterSeconds'] = self.expire_after_seconds

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireAfterSeconds') is not None:
            self.expire_after_seconds = m.get('ExpireAfterSeconds')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

