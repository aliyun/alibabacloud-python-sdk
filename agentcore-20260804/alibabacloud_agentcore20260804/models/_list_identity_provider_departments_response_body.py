# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProviderDepartmentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListIdentityProviderDepartmentsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code of the API request. SUCCESS indicates that the request is successful, but does not indicate that the asynchronous synchronization task is completed.
        self.code = code
        # The HTTP status code of the API request, which does not indicate the execution result of the asynchronous task.
        self.http_status_code = http_status_code
        # The direct child departments on the current page under the current parent department. You must make another query to obtain the details of the child departments.
        self.items = items
        # The number of items per page used for this query.
        self.max_results = max_results
        # The response message of the API request.
        self.message = message
        # The token for the next page. An empty or missing value indicates that there are no subsequent pages at the current hierarchy level of the parent department, but does not indicate that the entire department tree has been returned.
        self.next_token = next_token
        # The unique identifier of the request. Provide this value when troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the API request is successful. To check whether an asynchronous task is completed, query the task status.
        self.success = success
        # The total number of departments. This operation does not provide this statistic and may not return this field. Do not treat a missing value as 0.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListIdentityProviderDepartmentsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListIdentityProviderDepartmentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        has_children: bool = None,
        id: str = None,
        member_count: int = None,
        name: str = None,
        parent_id: str = None,
    ):
        # Indicates whether the department has child departments. A value of true indicates that the department has child departments and an expansion entry can be displayed accordingly. A value of false indicates a leaf node. If this field is not returned, the status is unknown. You must use the ID of the current node to make another query to obtain the details of the child departments.
        self.has_children = has_children
        # The unique identifier of the department returned by the identity provider. When querying the child departments of this node, use this value as the parentDepartmentId.
        self.id = id
        # The number of members in the department returned by the identity provider. This field is not returned when the number is unknown. Do not treat a missing value as 0.
        self.member_count = member_count
        # The name of the department returned by the identity provider.
        self.name = name
        # The ID of the parent department to which this department belongs. This value describes the parent-child relationship and is not used to expand the current node.
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_children is not None:
            result['hasChildren'] = self.has_children

        if self.id is not None:
            result['id'] = self.id

        if self.member_count is not None:
            result['memberCount'] = self.member_count

        if self.name is not None:
            result['name'] = self.name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasChildren') is not None:
            self.has_children = m.get('hasChildren')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        return self

