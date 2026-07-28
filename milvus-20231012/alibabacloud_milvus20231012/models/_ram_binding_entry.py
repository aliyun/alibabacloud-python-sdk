# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RamBindingEntry(DaraModel):
    def __init__(
        self,
        bound_uid: str = None,
        bound_user_name: str = None,
        milvus_username: str = None,
    ):
        # The unique identifier (UID) of the bound RAM user.
        self.bound_uid = bound_uid
        # The bound RAM username.
        self.bound_user_name = bound_user_name
        # The Milvus username.
        self.milvus_username = milvus_username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_uid is not None:
            result['boundUid'] = self.bound_uid

        if self.bound_user_name is not None:
            result['boundUserName'] = self.bound_user_name

        if self.milvus_username is not None:
            result['milvusUsername'] = self.milvus_username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boundUid') is not None:
            self.bound_uid = m.get('boundUid')

        if m.get('boundUserName') is not None:
            self.bound_user_name = m.get('boundUserName')

        if m.get('milvusUsername') is not None:
            self.milvus_username = m.get('milvusUsername')

        return self

