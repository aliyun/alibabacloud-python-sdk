# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        project_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.client_token = client_token
        self.project_id = project_id
        # This parameter is required.
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

