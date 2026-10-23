# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListWorkflowTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListWorkflowTemplatesResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # Indicates whether more data is available.
        self.has_more = has_more
        # The list of template summaries on the current page.
        self.items = items
        # The maximum number of entries returned per page in the current request.
        self.max_results = max_results
        # The error message.
        self.message = message
        # The pagination token for the next page. An empty string indicates that no more data is available.
        self.next_token = next_token
        # The current page number.
        self.page = page
        # The number of entries per page in the current request.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of visible entries that match the filter conditions.
        self.total = total

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

        if self.has_more is not None:
            result['hasMore'] = self.has_more

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

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListWorkflowTemplatesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListWorkflowTemplatesResponseBodyItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        effective_version: str = None,
        gmt_modified: str = None,
        latest_version: str = None,
        latest_version_status: str = None,
        name: str = None,
        owner_count: int = None,
        review_step_count: int = None,
        step_count: int = None,
        template_id: str = None,
    ):
        # The description of the template.
        self.description = description
        # The current effective version number. An empty value indicates that only a draft exists and the template cannot be used for work items.
        self.effective_version = effective_version
        # The time when the template was last modified. The time is in the ISO 8601 standard.
        self.gmt_modified = gmt_modified
        # The latest version number.
        self.latest_version = latest_version
        # The status of the latest version. Valid values:
        # - DRAFT: Draft. The version contains uncommitted edits.
        # - SUBMITTED: Submitted.
        self.latest_version_status = latest_version_status
        # The name of the template.
        self.name = name
        # The number of unique owners.
        self.owner_count = owner_count
        # The number of steps configured with reviewers.
        self.review_step_count = review_step_count
        # The number of steps.
        self.step_count = step_count
        # The ID of the template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.effective_version is not None:
            result['effectiveVersion'] = self.effective_version

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version

        if self.latest_version_status is not None:
            result['latestVersionStatus'] = self.latest_version_status

        if self.name is not None:
            result['name'] = self.name

        if self.owner_count is not None:
            result['ownerCount'] = self.owner_count

        if self.review_step_count is not None:
            result['reviewStepCount'] = self.review_step_count

        if self.step_count is not None:
            result['stepCount'] = self.step_count

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectiveVersion') is not None:
            self.effective_version = m.get('effectiveVersion')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('latestVersionStatus') is not None:
            self.latest_version_status = m.get('latestVersionStatus')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ownerCount') is not None:
            self.owner_count = m.get('ownerCount')

        if m.get('reviewStepCount') is not None:
            self.review_step_count = m.get('reviewStepCount')

        if m.get('stepCount') is not None:
            self.step_count = m.get('stepCount')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

