# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryMediaWorkflowListResponseBody(DaraModel):
    def __init__(
        self,
        media_workflow_list: main_models.QueryMediaWorkflowListResponseBodyMediaWorkflowList = None,
        non_exist_media_workflow_ids: main_models.QueryMediaWorkflowListResponseBodyNonExistMediaWorkflowIds = None,
        request_id: str = None,
    ):
        self.media_workflow_list = media_workflow_list
        self.non_exist_media_workflow_ids = non_exist_media_workflow_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media_workflow_list:
            self.media_workflow_list.validate()
        if self.non_exist_media_workflow_ids:
            self.non_exist_media_workflow_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_workflow_list is not None:
            result['MediaWorkflowList'] = self.media_workflow_list.to_map()

        if self.non_exist_media_workflow_ids is not None:
            result['NonExistMediaWorkflowIds'] = self.non_exist_media_workflow_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaWorkflowList') is not None:
            temp_model = main_models.QueryMediaWorkflowListResponseBodyMediaWorkflowList()
            self.media_workflow_list = temp_model.from_map(m.get('MediaWorkflowList'))

        if m.get('NonExistMediaWorkflowIds') is not None:
            temp_model = main_models.QueryMediaWorkflowListResponseBodyNonExistMediaWorkflowIds()
            self.non_exist_media_workflow_ids = temp_model.from_map(m.get('NonExistMediaWorkflowIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryMediaWorkflowListResponseBodyNonExistMediaWorkflowIds(DaraModel):
    def __init__(
        self,
        media_workflow_id: List[str] = None,
    ):
        self.media_workflow_id = media_workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        return self

class QueryMediaWorkflowListResponseBodyMediaWorkflowList(DaraModel):
    def __init__(
        self,
        media_workflow: List[main_models.QueryMediaWorkflowListResponseBodyMediaWorkflowListMediaWorkflow] = None,
    ):
        self.media_workflow = media_workflow

    def validate(self):
        if self.media_workflow:
            for v1 in self.media_workflow:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaWorkflow'] = []
        if self.media_workflow is not None:
            for k1 in self.media_workflow:
                result['MediaWorkflow'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_workflow = []
        if m.get('MediaWorkflow') is not None:
            for k1 in m.get('MediaWorkflow'):
                temp_model = main_models.QueryMediaWorkflowListResponseBodyMediaWorkflowListMediaWorkflow()
                self.media_workflow.append(temp_model.from_map(k1))

        return self

class QueryMediaWorkflowListResponseBodyMediaWorkflowListMediaWorkflow(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        media_workflow_id: str = None,
        name: str = None,
        state: str = None,
        topology: str = None,
        trigger_mode: str = None,
    ):
        self.creation_time = creation_time
        self.media_workflow_id = media_workflow_id
        self.name = name
        self.state = state
        self.topology = topology
        self.trigger_mode = trigger_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        if self.topology is not None:
            result['Topology'] = self.topology

        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Topology') is not None:
            self.topology = m.get('Topology')

        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')

        return self

