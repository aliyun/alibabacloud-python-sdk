# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListNotifyPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        notify_policy_list: List[main_models.NotifyPolicySummary] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned in this request.
        self.max_results = max_results
        # The pagination token for the next page. This parameter is empty if no more data is available.
        self.next_token = next_token
        # The list of notify policies. Each entry is of the NotifyPolicySummary type (lightweight view).
        self.notify_policy_list = notify_policy_list
        # The request ID. You can use this ID for troubleshooting and ticket submission.
        self.request_id = request_id
        # The total number of entries. The actual total is returned on the first page. A fixed value of -1 is returned on subsequent pages.
        self.total_count = total_count

    def validate(self):
        if self.notify_policy_list:
            for v1 in self.notify_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['notifyPolicyList'] = []
        if self.notify_policy_list is not None:
            for k1 in self.notify_policy_list:
                result['notifyPolicyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.notify_policy_list = []
        if m.get('notifyPolicyList') is not None:
            for k1 in m.get('notifyPolicyList'):
                temp_model = main_models.NotifyPolicySummary()
                self.notify_policy_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

