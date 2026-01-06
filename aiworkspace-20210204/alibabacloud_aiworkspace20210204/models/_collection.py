# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Collection(DaraModel):
    def __init__(
        self,
        collection_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        owner_id: str = None,
        user_id: str = None,
    ):
        self.collection_name = collection_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.owner_id = owner_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

