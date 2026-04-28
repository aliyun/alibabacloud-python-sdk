# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIdentityToBenefitPkgMappingRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        benefit_pkg_id: str = None,
        expire_time: int = None,
        identity_id: str = None,
        identity_type: str = None,
    ):
        # The number of benefit packages.
        # 
        # This parameter takes effect only for the benefit packages of the resource type. Default value: 1.
        self.amount = amount
        # The unique identifier of the benefit package.
        # 
        # This parameter is required.
        self.benefit_pkg_id = benefit_pkg_id
        # The time when the benefit package expires. Set the value to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # By default, the benefit package never expires.
        self.expire_time = expire_time
        # The unique identifier of the entity.
        # 
        # If you want to manage the benefits of a user, set this parameter to a user ID.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The type of the entity.
        # 
        # If you want to manage the benefits of a user, set this parameter to user.
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
        if self.amount is not None:
            result['amount'] = self.amount

        if self.benefit_pkg_id is not None:
            result['benefit_pkg_id'] = self.benefit_pkg_id

        if self.expire_time is not None:
            result['expire_time'] = self.expire_time

        if self.identity_id is not None:
            result['identity_id'] = self.identity_id

        if self.identity_type is not None:
            result['identity_type'] = self.identity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('benefit_pkg_id') is not None:
            self.benefit_pkg_id = m.get('benefit_pkg_id')

        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')

        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')

        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')

        return self

