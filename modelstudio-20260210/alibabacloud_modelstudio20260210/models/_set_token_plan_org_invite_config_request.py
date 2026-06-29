# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetTokenPlanOrgInviteConfigRequest(DaraModel):
    def __init__(
        self,
        default_role_id: str = None,
        seat_assign_strategy: str = None,
    ):
        # The ID of the organization role assigned by default. Valid values:
        # 
        # - SYSTEM_ROLE_ORG_ADMIN
        # - SYSTEM_ROLE_ORG_MEMBER
        # 
        # This parameter is required.
        self.default_role_id = default_role_id
        # The default seat allocation policy. Valid values:
        # 
        # - HIGH_TO_LOW
        # - LOW_TO_HIGH
        # - NONE
        # 
        # This parameter is required.
        self.seat_assign_strategy = seat_assign_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_role_id is not None:
            result['DefaultRoleId'] = self.default_role_id

        if self.seat_assign_strategy is not None:
            result['SeatAssignStrategy'] = self.seat_assign_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRoleId') is not None:
            self.default_role_id = m.get('DefaultRoleId')

        if m.get('SeatAssignStrategy') is not None:
            self.seat_assign_strategy = m.get('SeatAssignStrategy')

        return self

