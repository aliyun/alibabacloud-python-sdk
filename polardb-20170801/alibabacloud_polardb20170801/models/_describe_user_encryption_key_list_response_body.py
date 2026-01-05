# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUserEncryptionKeyListResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        key_list: List[str] = None,
        request_id: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # Cluster key list.
        self.key_list = key_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.key_list is not None:
            result['KeyList'] = self.key_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('KeyList') is not None:
            self.key_list = m.get('KeyList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

