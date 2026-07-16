# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListApiTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        api_templates: List[main_models.ApiTemplate] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The array of API templates.
        self.api_templates = api_templates
        # The maximum number of entries returned for the current request.
        self.max_results = max_results
        # The token to use to retrieve the next page of results. This value is empty when there are no more results to return.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries that meet the filter criteria.
        self.total_count = total_count

    def validate(self):
        if self.api_templates:
            for v1 in self.api_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiTemplates'] = []
        if self.api_templates is not None:
            for k1 in self.api_templates:
                result['ApiTemplates'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_templates = []
        if m.get('ApiTemplates') is not None:
            for k1 in m.get('ApiTemplates'):
                temp_model = main_models.ApiTemplate()
                self.api_templates.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

