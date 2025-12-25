# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccountRequest(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        user_name: str = None,
    ):
        # The timestamp that indicates when the pair of static username and password that you want to delete was created. Unit: milliseconds.
        # 
        # You can call the [ListAccounts](https://help.aliyun.com/document_detail/472730.html) operation to view the timestamp.
        self.create_timestamp = create_timestamp
        # The pair of username and password that you want to delete.
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
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

