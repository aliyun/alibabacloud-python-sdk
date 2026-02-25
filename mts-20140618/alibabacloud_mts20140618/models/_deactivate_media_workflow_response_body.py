# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class DeactivateMediaWorkflowResponseBody(DaraModel):
    def __init__(
        self,
        media_workflow: main_models.DeactivateMediaWorkflowResponseBodyMediaWorkflow = None,
        request_id: str = None,
    ):
        # The topology of the media workflow.
        self.media_workflow = media_workflow
        # The name of the media workflow that is deactivated.
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
            temp_model = main_models.DeactivateMediaWorkflowResponseBodyMediaWorkflow()
            self.media_workflow = temp_model.from_map(m.get('MediaWorkflow'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeactivateMediaWorkflowResponseBodyMediaWorkflow(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        media_workflow_id: str = None,
        name: str = None,
        state: str = None,
        topology: str = None,
    ):
        # *   After you deactivate a media workflow, you can modify the workflow information.
        # *   After you delete or deactivate a media workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        # 
        # ## Limits on QPS
        # 
        # You can call this operation up to 100 times per second. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        self.creation_time = creation_time
        # The ID of the media workflow that you want to deactivate. To obtain the ID of the media workflow, you can log on to the **ApsaraVideo Media Processing (MPS) console** and choose **Workflows** > **Workflow Settings** in the left-side navigation pane.
        self.media_workflow_id = media_workflow_id
        # The details of the media workflow.
        self.name = name
        # The topology of the media workflow.The status of the media workflow. The value is **Inactive**.
        self.state = state
        # The status of the media workflow. The value is **Inactive**.
        self.topology = topology

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

        return self

