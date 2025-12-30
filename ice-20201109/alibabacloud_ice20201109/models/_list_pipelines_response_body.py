# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListPipelinesResponseBody(DaraModel):
    def __init__(
        self,
        pipeline_list: List[main_models.ListPipelinesResponseBodyPipelineList] = None,
        request_id: str = None,
    ):
        # The queried MPS queues.
        self.pipeline_list = pipeline_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.pipeline_list:
            for v1 in self.pipeline_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PipelineList'] = []
        if self.pipeline_list is not None:
            for k1 in self.pipeline_list:
                result['PipelineList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pipeline_list = []
        if m.get('PipelineList') is not None:
            for k1 in m.get('PipelineList'):
                temp_model = main_models.ListPipelinesResponseBodyPipelineList()
                self.pipeline_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPipelinesResponseBodyPipelineList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modified_time: str = None,
        name: str = None,
        pipeline_id: str = None,
        priority: int = None,
        speed: str = None,
        status: str = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        # The time when the template was last modified.
        self.modified_time = modified_time
        # The name of the MPS queue.
        self.name = name
        # The ID of the MPS queue.
        self.pipeline_id = pipeline_id
        # The priority of the MPS queue.
        self.priority = priority
        # The type of the MPS queue.
        self.speed = speed
        # The state of the MPS queue.
        # 
        # Valid values:
        # 
        # *   Active
        # *   Paused
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

