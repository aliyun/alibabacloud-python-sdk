# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        user_name: str = None,
    ):
        # The cluster ID.
        # 
        # You can call [ListClusters](https://help.aliyun.com/document_detail/87116.html) to obtain the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The username.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

