# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadMediaByURLRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        enable_first_frame_cover: bool = None,
        generate_thumbnail: bool = None,
        session_id: str = None,
        storage_location: str = None,
        template_group_id: str = None,
        upload_metadatas: str = None,
        upload_urls: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The application ID. Default value: **app-1000000**. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # Specifies whether to use the first frame of the video as the cover.
        self.enable_first_frame_cover = enable_first_frame_cover
        # Specifies whether to generate a thumbnail for the video.
        self.generate_thumbnail = generate_thumbnail
        # The custom deduplication identifier. If this parameter is passed in a request and a request with the same identifier was detected within the past 10 minutes, an error is returned for the current request.
        # >  
        # > - The deduplication identifier is custom. It can be up to 50 characters in length and supports uppercase and lowercase letters, digits, hyphens (-), and underscores (_). If you do not pass this parameter or pass an empty string, deduplication is not performed.
        self.session_id = session_id
        # The storage address of the media file.
        # 
        # Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/?spm=a2c4g.11186623.2.15.6948257eaZ4m54#/vod/settings/censored) and choose **Configuration Management** > **Media Asset Management Configuration** > **Storage Management** to view the storage address. If you do not specify this parameter, the default storage address is used.
        self.storage_location = storage_location
        # The ID of the transcoding template group. You can obtain the ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing Configuration** > **Transcoding Template Groups** to view the ID of the transcoding template group.
        # - When you create a transcoding template group by calling the [Create a transcoding template group](https://help.aliyun.com/document_detail/102665.html) operation, the ID of the transcoding template group is the value of the TranscodeTemplateGroupId response parameter.
        # - When you query transcoding template groups by calling the [Query transcoding template groups](https://help.aliyun.com/document_detail/102669.html) operation, the ID is the value of the TranscodeTemplateGroupId response parameter.
        # 
        # >- If you do not specify the ID of a transcoding template group, the default transcoding template group is used for transcoding. If you specify the ID of a transcoding template group, the specified template group is used for transcoding.
        # >- You can also set this parameter in `UploadMetadatas`. If TemplateGroupId is set in both `UploadMetadatas` and here, the TemplateGroupId set in `UploadMetadatas` prevails.
        self.template_group_id = template_group_id
        # The metadata of the media files to be uploaded. The value is a JSON string.
        # 
        # - The metadata takes effect only when it matches the URL in UploadURLs.
        # - JSON format: `[UploadMetadata, UploadMetadata,…]`. The value must be converted to a JSON string.
        # - For more information, see the **UploadMetadata** table below.
        self.upload_metadatas = upload_metadatas
        # The URLs of the source media files.
        # - The URL must include a file name extension. For example, in `https://****.mp4`, mp4 is the file name extension.
        #     - If the URL does not contain a file name extension, you can specify it by passing `FileExtension` in `UploadMetadatas`.
        #     - If the URL contains a file name extension and `FileExtension` is also passed, the passed `FileExtension` prevails.
        #     - For supported file name extensions, see [Upload overview](https://help.aliyun.com/document_detail/55396.html).
        # 
        # > - The URLs must be URL-encoded. Separate multiple URLs with commas (,). You can specify up to 20 URLs. To prevent upload failures caused by special characters, **URL-encode** the URLs before concatenating them with commas.
        # 
        # This parameter is required.
        self.upload_urls = upload_urls
        # The custom settings. The value is a JSON string. You can configure settings such as message callbacks and upload acceleration. For more information, see [UserData](~~86952#UserData~~).
        # 
        # > - To use the message callback feature in this parameter, you must configure an HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect. For more information about how to configure HTTP callbacks in the console, see [Callback settings](https://help.aliyun.com/document_detail/86071.html).
        # > - To use the upload acceleration feature, you must submit a ticket to apply for activation. For more information, see [Upload instructions](https://help.aliyun.com/document_detail/55396.html). For more information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
        self.user_data = user_data
        # The workflow ID. You can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing Configuration** > **Workflow Management** to view the workflow ID.
        # 
        # > If both WorkflowId and TemplateGroupId are passed, WorkflowId prevails. For usage instructions, see [Workflows](https://help.aliyun.com/document_detail/115347.html).
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

        if self.enable_first_frame_cover is not None:
            result['EnableFirstFrameCover'] = self.enable_first_frame_cover

        if self.generate_thumbnail is not None:
            result['GenerateThumbnail'] = self.generate_thumbnail

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.upload_metadatas is not None:
            result['UploadMetadatas'] = self.upload_metadatas

        if self.upload_urls is not None:
            result['UploadURLs'] = self.upload_urls

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EnableFirstFrameCover') is not None:
            self.enable_first_frame_cover = m.get('EnableFirstFrameCover')

        if m.get('GenerateThumbnail') is not None:
            self.generate_thumbnail = m.get('GenerateThumbnail')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('UploadMetadatas') is not None:
            self.upload_metadatas = m.get('UploadMetadatas')

        if m.get('UploadURLs') is not None:
            self.upload_urls = m.get('UploadURLs')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

