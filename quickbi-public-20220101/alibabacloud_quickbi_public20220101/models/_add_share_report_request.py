# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddShareReportRequest(DaraModel):
    def __init__(
        self,
        auth_point: int = None,
        expire_date: int = None,
        share_to_id: str = None,
        share_to_type: int = None,
        works_id: str = None,
    ):
        # The scope of authorization. Valid values:
        # 
        # *   1: view only
        # *   3: View and export
        # 
        # This parameter is required.
        self.auth_point = auth_point
        # The validity period of the share. The value is a timestamp in milliseconds.
        # 
        # This parameter is required.
        self.expire_date = expire_date
        # The ID of the person to be shared, which may be the user ID of the Quick BI or the user group ID.
        # 
        # *   If ShareToType is 0 (user), ShareTo is the user ID.
        # *   When ShareToType is set to 1 (user group), ShareTo is the user group ID.
        # *   When ShareToType=2 (organization), ShareTo is the ID of the organization.
        self.share_to_id = share_to_id
        # The share type of the template. Valid values:
        # 
        # *   0: user
        # *   1: user group
        # *   2: organization
        # 
        # This parameter is required.
        self.share_to_type = share_to_type
        # The ID of the shared work. The works here include BI portal, dashboards, spreadsheets, and self-service access.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_point is not None:
            result['AuthPoint'] = self.auth_point

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.share_to_id is not None:
            result['ShareToId'] = self.share_to_id

        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPoint') is not None:
            self.auth_point = m.get('AuthPoint')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('ShareToId') is not None:
            self.share_to_id = m.get('ShareToId')

        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        return self

