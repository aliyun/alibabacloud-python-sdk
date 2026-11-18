# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterMediaRequest(DaraModel):
    def __init__(
        self,
        enable_first_frame_cover: bool = None,
        generate_thumbnail: bool = None,
        register_metadatas: str = None,
        template_group_id: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # Specifies whether to use the first frame of the video as the thumbnail.
        self.enable_first_frame_cover = enable_first_frame_cover
        # Specifies whether to generate a thumbnail for the video.
        self.generate_thumbnail = generate_thumbnail
        # The metadata of the media assets to be registered. The value is a JSON string. You can specify the metadata for up to 10 media assets at a time. For more information about the parameter structure, see the **RegisterMetadata** table below.
        # 
        # This parameter is required.
        self.register_metadatas = register_metadatas
        # The ID of the transcoding template group. You can obtain the ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing Configuration** > **Transcoding Template Groups** to view the ID of the transcoding template group.
        # - When you create a transcoding template group by calling the [Create a transcoding template group](https://help.aliyun.com/document_detail/102665.html) operation, the ID of the transcoding template group is the value of the TranscodeTemplateGroupId response parameter.
        # - When you query transcoding template groups by calling the [Query transcoding configurations](https://help.aliyun.com/document_detail/102669.html) operation, the ID of the transcoding template group is the value of the TranscodeTemplateGroupId response parameter.
        # 
        # > - If transcoding is not required, set this parameter to VOD_NO_TRANSCODE, which specifies the no-transcoding template group. Otherwise, the video status is **Upload Completed**, and you cannot use the playback service to play the audio or video. If transcoding is required, specify the ID of the corresponding transcoding template group.
        # > - If both WorkflowId and TemplateGroupId are specified, WorkflowId takes precedence. For more information, see [Media workflows](https://help.aliyun.com/document_detail/115347.html).
        # > - The task for this parameter is an [asynchronous task](https://help.aliyun.com/document_detail/3027551.html). After the task is submitted, it is not immediately completed but queued for asynchronous execution in the background.
        self.template_group_id = template_group_id
        # The custom settings. The value is a JSON string. You can configure settings such as message callbacks. For more information about the parameter, see [UserData](~~86952#section_6fg_qll_v3w~~).
        # > This operation does not support callbacks. Even if a message callback is configured in this parameter, no callback message is generated after the media asset registration is completed. When you subsequently initiate media processing such as transcoding and snapshot generation for the registered media assets, if you separately configure a message callback in UserData when initiating the transcoding or snapshot generation, that callback URL takes precedence. If no callback is separately configured, the callback URL configured in UserData during the media asset registration is used.
        self.user_data = user_data
        # The ID of the media workflow. You can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing Configuration** > **Workflow Management** to view the workflow ID.
        # 
        # > - If both WorkflowId and TemplateGroupId are specified, WorkflowId takes precedence. For more information, see [Media workflows](https://help.aliyun.com/document_detail/115347.html).
        # > - The task for this parameter is an [asynchronous task](https://help.aliyun.com/document_detail/3027551.html). After the task is submitted, it is not immediately completed but queued for asynchronous execution in the background.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_first_frame_cover is not None:
            result['EnableFirstFrameCover'] = self.enable_first_frame_cover

        if self.generate_thumbnail is not None:
            result['GenerateThumbnail'] = self.generate_thumbnail

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
        if m.get('EnableFirstFrameCover') is not None:
            self.enable_first_frame_cover = m.get('EnableFirstFrameCover')

        if m.get('GenerateThumbnail') is not None:
            self.generate_thumbnail = m.get('GenerateThumbnail')

        if m.get('RegisterMetadatas') is not None:
            self.register_metadatas = m.get('RegisterMetadatas')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

