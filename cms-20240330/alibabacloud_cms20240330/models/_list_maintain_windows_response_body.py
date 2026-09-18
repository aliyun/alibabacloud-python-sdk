# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListMaintainWindowsResponseBody(DaraModel):
    def __init__(
        self,
        maintain_window_list: List[main_models.MaintainWindowForView] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of silence policies. An empty list is returned when no items match. The list items do not include workspaceFilterSetting.
        self.maintain_window_list = maintain_window_list
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # The pagination token for the next page. A non-empty value indicates that more results may be available, but the next page may still be empty. An empty value indicates the end of pagination.
        self.next_token = next_token
        # The unique ID of this request, used for troubleshooting and ticket tracking.
        self.request_id = request_id

    def validate(self):
        if self.maintain_window_list:
            for v1 in self.maintain_window_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['maintainWindowList'] = []
        if self.maintain_window_list is not None:
            for k1 in self.maintain_window_list:
                result['maintainWindowList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.maintain_window_list = []
        if m.get('maintainWindowList') is not None:
            for k1 in m.get('maintainWindowList'):
                temp_model = main_models.MaintainWindowForView()
                self.maintain_window_list.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

