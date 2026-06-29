# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetTokenPlanOrgInviteConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTokenPlanOrgInviteConfigResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The response status code.
        self.code = code
        # The data result of the current category statistics.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the API call is successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTokenPlanOrgInviteConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTokenPlanOrgInviteConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        default_role_id: str = None,
        org_id: str = None,
        seat_assign_strategy: str = None,
    ):
        # The default organization role ID to assign. Valid values:
        # 
        # - SYSTEM_ROLE_ORG_ADMIN
        # - SYSTEM_ROLE_ORG_MEMBER
        self.default_role_id = default_role_id
        # The organization ID.
        self.org_id = org_id
        # The default seat allocation strategy. Valid values:
        # 
        # - HIGH_TO_LOW
        # - LOW_TO_HIGH 
        # - NONE
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

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.seat_assign_strategy is not None:
            result['SeatAssignStrategy'] = self.seat_assign_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRoleId') is not None:
            self.default_role_id = m.get('DefaultRoleId')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('SeatAssignStrategy') is not None:
            self.seat_assign_strategy = m.get('SeatAssignStrategy')

        return self

