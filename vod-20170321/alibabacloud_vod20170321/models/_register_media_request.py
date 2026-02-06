# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterMediaRequest(DaraModel):
    def __init__(
        self,
        register_metadatas: str = None,
        template_group_id: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The metadata of the media files. The value must be a JSON string. You can specify the metadata for up to 10 media files at a time. For more information about the metadata of media files, see the **RegisterMetadata** section of this topic.
        # 
        # This parameter is required.
        self.register_metadatas = register_metadatas
        # The ID of the transcoding template group. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Processing** > **Transcoding Template Groups**. On the Transcoding Template Groups page, you can view the ID of the transcoding template group.
        # *   Obtain the value of the TranscodeTemplateGroupId parameter from the response to the [AddTranscodeTemplateGroup](https://help.aliyun.com/document_detail/102665.html) operation that you called to create a transcoding template group.
        # *   Obtain the value of the TranscodeTemplateGroupId parameter from the response to the [ListTranscodeTemplateGroup](https://help.aliyun.com/document_detail/102669.html) operation that you called to query transcoding template groups.
        # 
        # > 
        # 
        # *   If you do not need to transcode media files, set the TemplateGroupId parameter to VOD_NO_TRANSCODE. If you do not specify this configuration, errors occur on your files. If you need to transcode media files, specify the ID of the transcoding template group.
        # 
        # *   If you specify both WorkflowId and TemplateGroupId, the value of the WorkflowId parameter takes effect. For more information, see [Workflows](https://help.aliyun.com/document_detail/115347.html).
        self.template_group_id = template_group_id
        # The custom settings. The value must be a JSON string. You can configure settings such as message callbacks. For more information, see [UserData](~~86952#section_6fg_qll_v3w~~).
        # 
        # >  You cannot configure callbacks for this operation. No callback message is returned after the media files are registered even if you configure callback settings for this parameter. If you configure callback settings for the UserData parameter when you create media processing jobs such as transcoding and snapshot capture jobs for the media file, the callback URL that you specified is used. If you do not configure callback settings when you create media processing jobs, the callback URL that you specified for the UserData parameter when you register the media file is used.
        self.user_data = user_data
        # The ID of the workflow. To view the workflow ID, perform the following steps: Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Processing** > **Workflows**.
        # 
        # >  If you specify both WorkflowId and TemplateGroupId, the value of WorkflowId parameter takes effect. For more information, see [Workflows](https://help.aliyun.com/document_detail/115347.html).
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.register_metadatas is not None:
            result['RegisterMetadatas'] = self.register_metadatas

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegisterMetadatas') is not None:
            self.register_metadatas = m.get('RegisterMetadatas')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

