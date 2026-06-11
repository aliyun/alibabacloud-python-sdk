# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListPipelinesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        pipelines: List[main_models.ListPipelinesResponseBodyPipelines] = None,
        request_id: str = None,
    ):
        # The number of results returned on the current page.
        self.max_results = max_results
        # A pagination token. If this parameter is not empty, use it in a subsequent request to get the next page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # A list of pipelines.
        self.pipelines = pipelines
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.pipelines:
            for v1 in self.pipelines:
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

        result['pipelines'] = []
        if self.pipelines is not None:
            for k1 in self.pipelines:
                result['pipelines'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.pipelines = []
        if m.get('pipelines') is not None:
            for k1 in m.get('pipelines'):
                temp_model = main_models.ListPipelinesResponseBodyPipelines()
                self.pipelines.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPipelinesResponseBodyPipelines(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        pipeline_name: str = None,
        region_id: str = None,
        update_time: str = None,
        workspace: str = None,
    ):
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The description of the pipeline.
        self.description = description
        # The pipeline name.
        self.pipeline_name = pipeline_name
        # The region ID.
        self.region_id = region_id
        # The update time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        # The workspace ID.
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

        if self.description is not None:
            result['description'] = self.description

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

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

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

