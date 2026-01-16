# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListPipelineResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListPipelineResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListPipelineResponseBodyResult] = None,
    ):
        # The ID of the ApsaraVideo Media Processing (MPS) queue that is used to run the job.
        self.headers = headers
        # The response.
        self.request_id = request_id
        # The time when the pipeline was created.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListPipelineResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListPipelineResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListPipelineResponseBodyResult(DaraModel):
    def __init__(
        self,
        gmt_created_time: str = None,
        gmt_update_time: str = None,
        pipeline_id: str = None,
        pipeline_status: str = None,
    ):
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        # The status of the pipeline. Supported:
        # 
        # *   NOT_DEPLOYED: The node is not deployed.
        # *   RUNNING
        # *   DELETED: Deleted. The console does not display this status.
        self.pipeline_id = pipeline_id
        self.pipeline_status = pipeline_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time

        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time

        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id

        if self.pipeline_status is not None:
            result['pipelineStatus'] = self.pipeline_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')

        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')

        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')

        if m.get('pipelineStatus') is not None:
            self.pipeline_status = m.get('pipelineStatus')

        return self

class ListPipelineResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The time when the pipeline was updated.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

