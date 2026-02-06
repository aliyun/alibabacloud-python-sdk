# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadMediaByURLRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        session_id: str = None,
        storage_location: str = None,
        template_group_id: str = None,
        upload_metadatas: str = None,
        upload_urls: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The ID of the application. Default value: **app-1000000**. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The custom identifier for deduplication. If you specify this parameter and send a request, an error is returned if a request with the same identifier was sent in the last 10 minutes. A custom identifier can be up to 50 characters in length and can contain letters, digits, hyphens (-), and underscores (_). If you do not specify this parameter or leave this parameter empty, duplicate requests are not filtered.
        self.session_id = session_id
        # The storage address of the media file.
        # 
        # To view the storage address, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/?spm=a2c4g.11186623.2.15.6948257eaZ4m54#/vod/settings/censored). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Storage**. If you do not specify a storage address, the default storage address is used.
        self.storage_location = storage_location
        # The ID of the transcoding template group. You can use one of the following methods to obtain the ID of the transcoding template group:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Processing** > **Transcoding Template Groups**. On the Transcoding Template Groups page, view the ID of the transcoding template group.
        # *   Obtain the value of TranscodeTemplateGroupId from the response to the [AddTranscodeTemplateGroup](https://help.aliyun.com/document_detail/102665.html) operation.
        # *   Obtain the value of TranscodeTemplateGroupId from the response to the [ListTranscodeTemplateGroup](https://help.aliyun.com/document_detail/102669.html) operation.
        # 
        # >-   If you leave this parameter empty, the default transcoding template group is used for transcoding. If you specify this parameter, the specified transcoding template group is used for transcoding.
        # >-   You can also specify the ID of the transcoding template group in `UploadMetadatas`. If you specify this parameter and TemplateGroupId in UploadMetadatas, the TemplateGroupId in UploadMetadatas takes effect.
        self.template_group_id = template_group_id
        # The metadata of the media file that you want to upload. The value must be a JSON string.
        # 
        # *   This parameter takes effect only if SourceURL matches the URL that you specified for UploadURLs.
        # *   You must convert the JSON-formatted data such as `[UploadMetadata, UploadMetadata,…]` to a JSON string.
        # *   For more information, see the **UploadMetadata** table.
        self.upload_metadatas = upload_metadatas
        # The URL of the media file.
        # 
        # *   You must include a file name extension in the URL, such as `https://****.mp4`.
        # 
        #     *   If the URL does not contain a file name extension, specify a file name extension for `FileExtension` in `UploadMetadatas`.
        #     *   If you specify `FileExtension` when the URL contains a file name extension, the file name extension that you specified for `FileExtension` takes effect.
        #     *   For more information about file name extensions supported by ApsaraVideo VOD, see [Overview](https://help.aliyun.com/document_detail/55396.html).
        # 
        # *   URL encoding is required. Separate multiple URLs with commas (,). You can specify a maximum of 20 URLs.
        # 
        # *   Special characters may cause upload failures. You must encode URLs before you separate them with commas (,).
        # 
        # This parameter is required.
        self.upload_urls = upload_urls
        # The custom configurations such as callback configurations and upload acceleration configurations. The value must be a JSON string. For more information, see [Request parameters](~~86952#UserData~~).
        # 
        # >-   The callback configurations take effect only after you specify the HTTP callback URL and select specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](https://help.aliyun.com/document_detail/86071.html).
        # >-   If you want to enable the upload acceleration feature, [submit a request on Yida](https://yida.alibaba-inc.com/o/ticketapply). For more information, see [Overview](https://help.aliyun.com/document_detail/55396.html).
        self.user_data = user_data
        # The ID of the workflow. To view the ID of the workflow, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Processing** > **Workflows**.
        # 
        # > If you specify WorkflowId and TemplateGroupId, the value of WorkflowId takes effect. For more information, see [Workflows](https://help.aliyun.com/document_detail/115347.html).
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

