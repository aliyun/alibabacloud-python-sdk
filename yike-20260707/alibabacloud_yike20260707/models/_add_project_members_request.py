# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddProjectMembersRequest(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        yike_user_ids: str = None,
    ):
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The Yike user IDs to be added. Separate multiple IDs with commas. The users must belong to the current Alibaba Cloud account. By default, the Edit permission is granted.
        # 
        # This parameter is required.
        self.yike_user_ids = yike_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.yike_user_ids is not None:
            result['YikeUserIds'] = self.yike_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('YikeUserIds') is not None:
            self.yike_user_ids = m.get('YikeUserIds')

        return self

