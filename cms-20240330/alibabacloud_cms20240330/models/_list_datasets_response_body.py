# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListDatasetsResponseBody(DaraModel):
    def __init__(
        self,
        datasets: List[main_models.ListDatasetsResponseBodyDatasets] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # A list of dataset objects.
        self.datasets = datasets
        # The maximum number of results returned per page.
        self.max_results = max_results
        # A token to retrieve the next page of results. This element is returned only when the result set is truncated.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of datasets that match the query.
        self.total = total

    def validate(self):
        if self.datasets:
            for v1 in self.datasets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['datasets'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasets = []
        if m.get('datasets') is not None:
            for k1 in m.get('datasets'):
                temp_model = main_models.ListDatasetsResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListDatasetsResponseBodyDatasets(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_name: str = None,
        description: str = None,
        region_id: str = None,
        update_time: str = None,
        workspace: str = None,
    ):
        # The time the dataset was created, as a UNIX timestamp.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The description of the dataset.
        self.description = description
        # The ID of the region where the dataset resides.
        self.region_id = region_id
        # The time the dataset was last updated, as a UNIX timestamp.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        # The ID of the workspace that contains the dataset.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.description is not None:
            result['description'] = self.description

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

