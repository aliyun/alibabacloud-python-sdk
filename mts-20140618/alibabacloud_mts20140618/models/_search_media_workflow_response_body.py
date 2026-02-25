# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class SearchMediaWorkflowResponseBody(DaraModel):
    def __init__(
        self,
        media_workflow_list: main_models.SearchMediaWorkflowResponseBodyMediaWorkflowList = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.media_workflow_list = media_workflow_list
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.media_workflow_list:
            self.media_workflow_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_workflow_list is not None:
            result['MediaWorkflowList'] = self.media_workflow_list.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaWorkflowList') is not None:
            temp_model = main_models.SearchMediaWorkflowResponseBodyMediaWorkflowList()
            self.media_workflow_list = temp_model.from_map(m.get('MediaWorkflowList'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchMediaWorkflowResponseBodyMediaWorkflowList(DaraModel):
    def __init__(
        self,
        media_workflow: List[main_models.SearchMediaWorkflowResponseBodyMediaWorkflowListMediaWorkflow] = None,
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
                temp_model = main_models.SearchMediaWorkflowResponseBodyMediaWorkflowListMediaWorkflow()
                self.media_workflow.append(temp_model.from_map(k1))

        return self

class SearchMediaWorkflowResponseBodyMediaWorkflowListMediaWorkflow(DaraModel):
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

