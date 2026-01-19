# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDatasetItemRequest(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_item_id: str = None,
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

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetItemId') is not None:
            self.dataset_item_id = m.get('DatasetItemId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

