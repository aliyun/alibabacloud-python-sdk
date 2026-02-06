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
        file_name: str = None,
        file_size: int = None,
        reference_id: str = None,
        storage_location: str = None,
        tags: str = None,
        template_group_id: str = None,
        title: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The ID of the application. Default value: **app-1000000**. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The ID of the category. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Categories** to view the category ID of the media file.
        # *   Obtain the value of CateId from the response to the [AddCategory](~~AddCategory~~) operation.
        # *   Obtain the value of CateId from the response to the [GetCategories](~~GetCategories~~) operation.
        self.cate_id = cate_id
        # The URL of the custom video thumbnail.
        self.cover_url = cover_url
        # The description of the audio or video file.
        # 
        # *   The value can be up to 1,024 characters in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The name of the source file.
        # 
        # *   The name must contain a file name extension, which is not case-sensitive.
        # *   For more information about file name extensions supported by ApsaraVideo VOD, see [Overview](https://help.aliyun.com/document_detail/55396.html).
        # 
        # This parameter is required.
        self.file_name = file_name
        # The size of the source file. Unit: bytes.
        self.file_size = file_size
        self.reference_id = reference_id
        # The storage address. Perform the following operations to obtain the storage address: Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Storage**. On the Storage page, view the storage address.
        # 
        # >  If you leave this parameter empty, audio and video files are uploaded to the default storage address. If you specify a storage address, audio and video files are uploaded to the specified address.
        self.storage_location = storage_location
        # The tags of the audio or video file.
        # 
        # *   You can specify a maximum of 16 tags.
        # *   If you want to specify multiple tags, separate the tags with commas (,).
        # *   Each tag can be up to 32 characters in length.
        # *   The value must be encoded in UTF-8.
        self.tags = tags
        # The ID of the transcoding template group. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the ApsaraVideo VOD console. In the left-side navigation pane, choose Configuration Management > Media Processing > Transcoding Template Groups. On the Transcoding Template Groups page, you can view the ID of the transcoding template group.[](https://vod.console.aliyun.com)************
        # *   Obtain the value of the TranscodeTemplateGroupId parameter from the response to the [AddTranscodeTemplateGroup](https://help.aliyun.com/document_detail/102665.html) operation that you called to create a transcoding template group.
        # *   Obtain the value of the TranscodeTemplateGroupId parameter from the response to the [ListTranscodeTemplateGroup](https://help.aliyun.com/document_detail/102669.html) operation that you called to query transcoding template groups.
        # 
        # > *   If you specify both WorkflowId and TemplateGroupId, the value of the WorkflowId parameter takes effect.
        # > *   If this parameter is not specified, transcoding is performed based on the default transcoding template group. If the transcoding template group ID is specified, transcoding is performed based on the specified template group.
        # > *   If the **No Transcoding** template group is used, only the [FileUploadComplete](https://help.aliyun.com/document_detail/55630.html) event notification is returned after a video is uploaded. The [StreamTranscodeComplete](https://help.aliyun.com/document_detail/55636.html) event notification is not returned.
        # > *   If you use the **No Transcoding** template group to upload videos, only videos in the format of MP4, FLV, MP3, M3U8, or WebM can be played. Videos in other formats can only be stored in ApsaraVideo VOD. You can view the file name extension to obtain the video format. If you want to use ApsaraVideo Player, make sure that the version of the player is V3.1.0 or later.
        self.template_group_id = template_group_id
        # The title of the audio or video file.
        # 
        # *   The title can be up to 128 characters in length.
        # *   The value must be encoded in UTF-8.
        # 
        # This parameter is required.
        self.title = title
        # The custom configurations such as callback configurations and upload acceleration configurations. The value must be a JSON string. For more information, see [Request parameters](https://help.aliyun.com/document_detail/86952.html).
        # 
        # > *   The callback configurations take effect only after you specify the HTTP callback URL and select specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](https://help.aliyun.com/document_detail/86071.html).
        # >*   If you want to enable the upload acceleration feature, [submit a request on Yida](https://yida.alibaba-inc.com/o/ticketapply). For more information, see [Overview](https://help.aliyun.com/document_detail/55396.html).
        self.user_data = user_data
        # The ID of the workflow. To view the ID of the workflow, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Processing** > **Workflows**.
        # 
        # > If you specify the WorkflowId and TemplateGroupId parameters, the value of the WorkflowId parameter takes effect. For more information, see [Workflows](https://help.aliyun.com/document_detail/115347.html).
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

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

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

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

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

