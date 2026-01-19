# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatasetItemRequest(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_item_id: str = None,
        description: str = None,
        expired_time: str = None,
        security_token: str = None,
    ):
        # The ID of the dataset.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id
        # The ID of the data entry.
        # 
        # This parameter is required.
        self.dataset_item_id = dataset_item_id
        # The description of the data entry. The description cannot exceed 180 characters in length.
        self.description = description
        # The time in UTC when the data entry expires. The time is in the **yyyy-MM-ddTHH:mm:ssZ** format.
        self.expired_time = expired_time
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_item_id is not None:
            result['DatasetItemId'] = self.dataset_item_id

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetItemId') is not None:
            self.dataset_item_id = m.get('DatasetItemId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

