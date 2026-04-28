# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIdentityToBenefitPkgMappingRequest(DaraModel):
    def __init__(
        self,
        identity_id: str = None,
        identity_type: str = None,
        include_expired: bool = None,
    ):
        # The unique identifier of the entity.
        # 
        # If you call this operation to manage the benefits of a user, set this parameter to the ID of the user.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The type of the entity. If you call this operation to manage the benefits of a user, set this parameter to user.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # Specifies whether to return the benefit packages that expire. Default value: false.
        self.include_expired = include_expired

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id

        if self.identity_type is not None:
            result['identity_type'] = self.identity_type

        if self.include_expired is not None:
            result['include_expired'] = self.include_expired

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')

        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')

        if m.get('include_expired') is not None:
            self.include_expired = m.get('include_expired')

        return self

