# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddWorksAuthorizationRequest(DaraModel):
    def __init__(
        self,
        auth_points: int = None,
        authorize_scope: int = None,
        authorized_id: str = None,
        expire_day: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The permissions to grant. Valid values:
        # 
        # `1`: View
        # 
        # `3`: View and Export
        # 
        # `11`: Edit, View, and Export
        # 
        # **Note**: If AuthPoints is set to 11, the authorization is permanent and the ExpireDay parameter is ignored.
        # 
        # This parameter is required.
        self.auth_points = auth_points
        # The type of the principal. Valid values:
        # 
        # - `0`: User. Set AuthorizedId to the user ID.
        # 
        # - `1`: User group. Set AuthorizedId to the user group ID.
        # 
        # - `2`: All members of an organization. Set AuthorizedId to the organization ID.
        # 
        # - `3`: All members of a workspace. Set AuthorizedId to the workspace ID.
        # 
        # This parameter is required.
        self.authorize_scope = authorize_scope
        # The ID of the principal to be authorized. The AuthorizeScope parameter specifies the type of principal.
        # 
        # This parameter is required.
        self.authorized_id = authorized_id
        # The expiration date for the permissions.
        # 
        # Format: `YYYY-MM-DD`.
        # 
        # **Note**: This parameter is required if AuthPoints is not 11. The authorization must be valid for at least one day after the authorization date.
        self.expire_day = expire_day
        # The ID of the work.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the work. Valid values:
        # 
        # - `dashboard`: A dashboard.
        # 
        # - `report`: A report.
        # 
        # - `dashboardOfflineQuery`: An ad-hoc query.
        # 
        # - `cube`: A dataset.
        # 
        # - `datasource`: A data source.
        # 
        # - `screen`: A data screen.
        # 
        # - `ANALYSIS`: An ad-hoc analysis.
        # 
        # - `dataForm`: A data form.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_points is not None:
            result['AuthPoints'] = self.auth_points

        if self.authorize_scope is not None:
            result['AuthorizeScope'] = self.authorize_scope

        if self.authorized_id is not None:
            result['AuthorizedId'] = self.authorized_id

        if self.expire_day is not None:
            result['ExpireDay'] = self.expire_day

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPoints') is not None:
            self.auth_points = m.get('AuthPoints')

        if m.get('AuthorizeScope') is not None:
            self.authorize_scope = m.get('AuthorizeScope')

        if m.get('AuthorizedId') is not None:
            self.authorized_id = m.get('AuthorizedId')

        if m.get('ExpireDay') is not None:
            self.expire_day = m.get('ExpireDay')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

