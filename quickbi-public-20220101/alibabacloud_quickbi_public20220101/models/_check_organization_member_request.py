# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckOrganizationMemberRequest(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The ID of the Quick BI user. This is not your Alibaba Cloud account ID. Call the [QueryUserInfoByAccount](https://next.api.aliyun.com/api/quickbi-public/2022-01-01/QueryUserInfoByAccount?spm=api-workbench.api_explorer.0.0.672f50daGq9ooV\\&params=%7B%7D\\&tab=DOC\\&sdkStyle=old\\&RegionId=cn-hangzhou) operation to obtain the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

