# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitWorkflowJobRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        workflow_id: str = None,
    ):
        # The ID of the media file. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the audio or video file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of the VideoId parameter when you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to upload media files.
        # *   Obtain the value of the VideoId parameter when you call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation after you upload media files.
        self.media_id = media_id
        # The ID of the workflow. To view the ID of the workflow, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Processing** > **Workflows**.
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
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

