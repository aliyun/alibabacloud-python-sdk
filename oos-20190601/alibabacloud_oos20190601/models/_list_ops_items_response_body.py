# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListOpsItemsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        ops_items: List[main_models.ListOpsItemsResponseBodyOpsItems] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The pagination token that can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The list of O\\&M items.
        self.ops_items = ops_items
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ops_items:
            for v1 in self.ops_items:
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

        result['OpsItems'] = []
        if self.ops_items is not None:
            for k1 in self.ops_items:
                result['OpsItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.ops_items = []
        if m.get('OpsItems') is not None:
            for k1 in m.get('OpsItems'):
                temp_model = main_models.ListOpsItemsResponseBodyOpsItems()
                self.ops_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOpsItemsResponseBodyOpsItems(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_date: str = None,
        ops_item_id: str = None,
        priority: int = None,
        resources: List[str] = None,
        severity: str = None,
        source: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
        update_date: str = None,
    ):
        # The category.
        self.category = category
        # The time when the O\\&M item was created.
        self.create_date = create_date
        # The ID of the O\\&M item.
        self.ops_item_id = ops_item_id
        # The priority.
        self.priority = priority
        # The Alibaba Resource Names (ARNs) of the associated resources.
        self.resources = resources
        # The severity level.
        self.severity = severity
        # The source business.
        self.source = source
        # The status of the O\\&M item.
        self.status = status
        # The tags.
        self.tags = tags
        # The title of the O\\&M item.
        self.title = title
        # The time when the O\\&M item was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

