# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryFaceUserBatchRequest(DaraModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id_list: List[str] = None,
    ):
        # The business isolation ID, which is used to isolate data between different business applications under the same Alibaba Cloud account. Keep this value consistent with the **IsolationId** set when calling the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) operation to add users.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The list of user IDs. Pass the user IDs that were obtained and saved locally after calling the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) operation to add users.
        # 
        # This parameter is required.
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

