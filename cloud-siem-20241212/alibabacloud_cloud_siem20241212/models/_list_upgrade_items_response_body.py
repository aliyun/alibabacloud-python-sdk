# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListUpgradeItemsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        upgrade_items: List[main_models.ListUpgradeItemsResponseBodyUpgradeItems] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.upgrade_items = upgrade_items

    def validate(self):
        if self.upgrade_items:
            for v1 in self.upgrade_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UpgradeItems'] = []
        if self.upgrade_items is not None:
            for k1 in self.upgrade_items:
                result['UpgradeItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.upgrade_items = []
        if m.get('UpgradeItems') is not None:
            for k1 in m.get('UpgradeItems'):
                temp_model = main_models.ListUpgradeItemsResponseBodyUpgradeItems()
                self.upgrade_items.append(temp_model.from_map(k1))

        return self

class ListUpgradeItemsResponseBodyUpgradeItems(DaraModel):
    def __init__(
        self,
        upgrade_item_id: str = None,
    ):
        self.upgrade_item_id = upgrade_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.upgrade_item_id is not None:
            result['UpgradeItemId'] = self.upgrade_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpgradeItemId') is not None:
            self.upgrade_item_id = m.get('UpgradeItemId')

        return self

