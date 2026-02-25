# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class AddMediaWorkflowResponseBody(DaraModel):
    def __init__(
        self,
        media_workflow: main_models.AddMediaWorkflowResponseBodyMediaWorkflow = None,
        request_id: str = None,
    ):
        # The information about the media workflow.
        self.media_workflow = media_workflow
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_workflow:
            self.media_workflow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_workflow is not None:
            result['MediaWorkflow'] = self.media_workflow.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaWorkflow') is not None:
            temp_model = main_models.AddMediaWorkflowResponseBodyMediaWorkflow()
            self.media_workflow = temp_model.from_map(m.get('MediaWorkflow'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddMediaWorkflowResponseBodyMediaWorkflow(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        media_workflow_id: str = None,
        name: str = None,
        state: str = None,
        topology: str = None,
        trigger_mode: str = None,
    ):
        # The time when the media workflow was created.
        self.creation_time = creation_time
        # The ID of the media workflow. We recommend that you keep this ID for later operations on this workflow.
        self.media_workflow_id = media_workflow_id
        # The name of the media workflow.
        self.name = name
        # The state of the media workflow. By default, the created workflow is in the **Active** state.
        self.state = state
        # The topology of the media workflow. The value is a JSON object that contains the activities and activity dependencies.
        self.topology = topology
        # The triggering mode of the media workflow. Valid values:
        # 
        # *   **OssAutoTrigger**: The media workflow is automatically triggered.
        # *   **NotInAuto**: The media workflow is not automatically triggered.
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

