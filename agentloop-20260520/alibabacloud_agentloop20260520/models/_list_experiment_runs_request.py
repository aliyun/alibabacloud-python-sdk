# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExperimentRunsRequest(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        experiment_name: str = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        plan_name: str = None,
        status: str = None,
    ):
        # Filters results by exact dataset ID.
        self.dataset_id = dataset_id
        # Filters results by fuzzy match on the experiment configuration name.
        self.experiment_name = experiment_name
        # Optional. Use `page` and `pageSize` for pagination instead.
        self.max_results = max_results
        # Optional. Use `page` and `pageSize` for pagination instead.
        self.next_token = next_token
        # The page number, starting from 0. Default value: 0.
        self.page = page
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # Filters results by fuzzy match on the experiment plan name.
        self.plan_name = plan_name
        # Filters results by status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.experiment_name is not None:
            result['experimentName'] = self.experiment_name

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('experimentName') is not None:
            self.experiment_name = m.get('experimentName')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

