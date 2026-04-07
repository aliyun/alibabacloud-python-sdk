# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataServiceApiAuthorityRequest(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        authorized_project_id: int = None,
        end_time: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The ID of the API.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The ID of the workspace to which the access permissions on the API are granted.
        # 
        # This parameter is required.
        self.authorized_project_id = authorized_project_id
        # The end time of the validity period of the access permissions. The time must be a UNIX timestamp. Unit: seconds. Example: 1600531564, which indicates 2020-09-20 00:06:04 (UTC+8).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.authorized_project_id is not None:
            result['AuthorizedProjectId'] = self.authorized_project_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('AuthorizedProjectId') is not None:
            self.authorized_project_id = m.get('AuthorizedProjectId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

