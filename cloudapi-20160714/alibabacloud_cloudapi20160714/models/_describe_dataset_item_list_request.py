# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDatasetItemListRequest(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_item_ids: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        # The ID of the dataset.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id
        # The ID of the data entry. You can enter multiple IDs. Separate them with commas (,).
        self.dataset_item_ids = dataset_item_ids
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
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

        if self.dataset_item_ids is not None:
            result['DatasetItemIds'] = self.dataset_item_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetItemIds') is not None:
            self.dataset_item_ids = m.get('DatasetItemIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

