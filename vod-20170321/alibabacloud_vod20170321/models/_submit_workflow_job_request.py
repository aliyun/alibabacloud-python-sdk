# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitWorkflowJobRequest(DaraModel):
    def __init__(
        self,
        extra_inputs: str = None,
        media_id: str = None,
        workflow_id: str = None,
    ):
        self.extra_inputs = extra_inputs
        # The media asset ID, which is the video ID. You can obtain the ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Assets** > **Audio/Video** to view the video ID.
        # - When you call the [Get the upload URL and credential for a video](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the video ID is the value of the VideoId response parameter.
        # - After a video is uploaded, you can call the [Search for media information](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID. The video ID is the value of the VideoId response parameter.
        self.media_id = media_id
        # The workflow ID. You can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing Configuration** > **Workflow Management** to view the ID.
        # 
        # This parameter is required.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_inputs is not None:
            result['ExtraInputs'] = self.extra_inputs

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInputs') is not None:
            self.extra_inputs = m.get('ExtraInputs')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

