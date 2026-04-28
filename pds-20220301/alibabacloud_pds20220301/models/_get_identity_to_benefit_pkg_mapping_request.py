# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIdentityToBenefitPkgMappingRequest(DaraModel):
    def __init__(
        self,
        benefit_pkg_id: str = None,
        identity_id: str = None,
        identity_type: str = None,
    ):
        # The unique identifier of the benefit package.
        # 
        # This parameter is required.
        self.benefit_pkg_id = benefit_pkg_id
        # The unique identifier of the entity.
        # 
        # If you want to manage the benefits of a user, set this parameter to a user ID.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The type of the entity. If you want to manage the benefits of a user, set this parameter to user.
        # 
        # This parameter is required.
        self.identity_type = identity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.benefit_pkg_id is not None:
            result['benefit_pkg_id'] = self.benefit_pkg_id

        if self.identity_id is not None:
            result['identity_id'] = self.identity_id

        if self.identity_type is not None:
            result['identity_type'] = self.identity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('benefit_pkg_id') is not None:
            self.benefit_pkg_id = m.get('benefit_pkg_id')

        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')

        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')

        return self

