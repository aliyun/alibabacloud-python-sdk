# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeUserSessionRequest(DaraModel):
    def __init__(
        self,
        external_ids: str = None,
        idp_id: str = None,
    ):
        # This parameter is required.
        self.external_ids = external_ids
        # This parameter is required.
        self.idp_id = idp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_ids is not None:
            result['ExternalIds'] = self.external_ids

        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIds') is not None:
            self.external_ids = m.get('ExternalIds')

        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        return self

