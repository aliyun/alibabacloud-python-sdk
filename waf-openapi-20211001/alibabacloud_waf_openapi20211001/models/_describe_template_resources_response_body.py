# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeTemplateResourcesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[str] = None,
        template_id: int = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # An array of protected objects or protected object groups that are associated to the protection rule template.
        self.resources = resources
        self.template_id = template_id
        self.total_count = total_count

    def validate(self):
        pass

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

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

