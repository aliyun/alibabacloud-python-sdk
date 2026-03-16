# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagerInfoByAuthCodeResponseBody(DaraModel):
    def __init__(
        self,
        org_id: str = None,
        phone: str = None,
        request_id: str = None,
        team_name: str = None,
        user_name: str = None,
        wa_id: int = None,
    ):
        # The organization ID.
        self.org_id = org_id
        # The mobile number.
        self.phone = phone
        # The request ID.
        self.request_id = request_id
        # The team name.
        self.team_name = team_name
        # The tenant name.
        self.user_name = user_name
        # The ID of the Elastic Desktop Service account.
        self.wa_id = wa_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.team_name is not None:
            result['TeamName'] = self.team_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.wa_id is not None:
            result['WaId'] = self.wa_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TeamName') is not None:
            self.team_name = m.get('TeamName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WaId') is not None:
            self.wa_id = m.get('WaId')

        return self

