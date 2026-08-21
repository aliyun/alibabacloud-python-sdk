# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadVideoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cover_url: str = None,
        description: str = None,
        enable_first_frame_cover: bool = None,
        file_name: str = None,
        file_size: int = None,
        generate_thumbnail: bool = None,
        reference_id: str = None,
        storage_location: str = None,
        tags: str = None,
        template_group_id: str = None,
        title: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The application ID. Default value: **app-1000000**. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The category ID. You can obtain the category ID by using one of the following methods:
        # 
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Management Configuration** > **Category Management** to view the category ID.
        # - When you create a category by calling the [AddCategory](~~AddCategory~~) operation, the category ID is the value of the CateId parameter in the response.
        # - When you query categories by calling the [GetCategories](~~GetCategories~~) operation, the category ID is the value of the CateId parameter in the response.
        self.cate_id = cate_id
        # The URL of the custom video thumbnail.
        self.cover_url = cover_url
        # The description of the audio or video file displayed in ApsaraVideo VOD after the upload is complete.
        # 
        # - The description can be up to 1024 characters in length.
        # - The value is encoded in UTF-8.
        self.description = description
        self.enable_first_frame_cover = enable_first_frame_cover
        # The address of the audio or video source file to be uploaded.
        # 
        # - The file name extension is required and is not case-sensitive.
        # - For supported file name extensions, see [Upload overview](https://help.aliyun.com/document_detail/55396.html).
        # 
        # This parameter is required.
        self.file_name = file_name
        # The size of the audio or video source file to be uploaded. Unit: bytes.
        self.file_size = file_size
        self.generate_thumbnail = generate_thumbnail
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens, and underscores are supported. The length is 6 to 64 characters. The ID is unique at the user level.
        self.reference_id = reference_id
        # The storage address. You can obtain the storage address by using the following method:
        # Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Management Configuration** > **Storage Management** to view the storage address.
        # 
        # > If this parameter is not specified, the audio or video file is uploaded to the default storage address. If no default storage address exists, the file is uploaded to the first storage address in the storage list. If this parameter is specified, the audio or video file is uploaded to the specified storage address.
        self.storage_location = storage_location
        # The tags of the audio or video file.
        # 
        # - You can specify up to 16 tags.
        # - To specify multiple tags, separate them with commas (,).
        # - Each tag can be up to 32 characters in length.
        # - The value is encoded in UTF-8.
        self.tags = tags
        # The ID of the transcoding template group. You can obtain the ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing Configuration** > **Transcoding Template Groups** to view the transcoding template group ID.
        # - When you create a transcoding template group by calling the [Create a transcoding template group](https://help.aliyun.com/document_detail/102665.html) operation, the transcoding template group ID is the value of the TranscodeTemplateGroupId parameter in the response.
        # - When you query transcoding template groups by calling the [Query transcoding configurations](https://help.aliyun.com/document_detail/102669.html) operation, the transcoding template group ID is the value of the TranscodeTemplateGroupId parameter in the response.
        # 
        # >- If both WorkflowId and TemplateGroupId are specified, WorkflowId takes precedence.
        # >- If this parameter is not specified, the default transcoding template group is used for transcoding. If a transcoding template group ID is specified, the specified template group is used for transcoding.
        # >- If this parameter is set to the built-in **No Transcoding** template group, only the [Video Upload Complete](https://help.aliyun.com/document_detail/55630.html) event notification is sent after the audio or video file is uploaded. The [Transcode Complete for a Single Definition](https://help.aliyun.com/document_detail/55636.html) event notification is not sent.
        # > - This parameter triggers an [asynchronous task](https://help.aliyun.com/document_detail/3027551.html). After submission, the task is not immediately completed and is queued for asynchronous execution in the background.
        # >- To ensure normal playback, when the built-in **No Transcoding** template group is used, only the following formats support direct playback without transcoding after the audio or video file is uploaded: MP4, FLV, MP3, M3U8, and WEBM. Other formats support storage only (check the file name extension of FileName). If you use ApsaraVideo Player, the player version must be 3.1.0 or later.
        self.template_group_id = template_group_id
        # The title of the audio or video file displayed in ApsaraVideo VOD after the upload is complete.
        # 
        # - The title can be up to 128 characters in length.
        # - The value is encoded in UTF-8.
        # 
        # This parameter is required.
        self.title = title
        # The custom settings in a JSON string. The settings support message callbacks, upload acceleration, and other configurations. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # 
        # > - To use the message callback in this parameter, you must configure an HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect. If no callback URL is specified for subsequent tasks, callbacks are sent to this address by default. To configure HTTP callbacks in the console, see [Callback settings](https://help.aliyun.com/document_detail/86071.html).
        # > - To use the upload acceleration feature, you must [submit a Yida form](https://yida.alibaba-inc.com/o/ticketapply) to apply for activation. For more information, see [Upload instructions](https://help.aliyun.com/document_detail/55396.html).
        self.user_data = user_data
        # The workflow ID. Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing Configuration** > **Workflow Management** to view the workflow ID.
        # 
        # > - If both WorkflowId and TemplateGroupId are specified, WorkflowId takes precedence. For more information, see [Workflows](https://help.aliyun.com/document_detail/115347.html).
        # > - This parameter triggers an [asynchronous task](https://help.aliyun.com/document_detail/3027551.html). After submission, the task is not immediately completed and is queued for asynchronous execution in the background.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_first_frame_cover is not None:
            result['EnableFirstFrameCover'] = self.enable_first_frame_cover

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.generate_thumbnail is not None:
            result['GenerateThumbnail'] = self.generate_thumbnail

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableFirstFrameCover') is not None:
            self.enable_first_frame_cover = m.get('EnableFirstFrameCover')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GenerateThumbnail') is not None:
            self.generate_thumbnail = m.get('GenerateThumbnail')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

