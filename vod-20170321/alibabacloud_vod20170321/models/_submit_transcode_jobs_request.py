# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTranscodeJobsRequest(DaraModel):
    def __init__(
        self,
        encrypt_config: str = None,
        override_params: str = None,
        pipeline_id: str = None,
        priority: str = None,
        reference_id: str = None,
        session_id: str = None,
        template_group_id: str = None,
        user_data: str = None,
        video_id: str = None,
    ):
        # The encryption configurations. The value must be a JSON string. This parameter is required only when you use HLS encryption.
        # 
        # > 
        # 
        # *   You must set **CipherText** in [EncrptConfig](https://help.aliyun.com/document_detail/86952.html) to the AES_128 cipher text that is obtained from the response to the [GenerateKMSDataKey](https://help.aliyun.com/document_detail/455051.html) operation. Otherwise, the HLS encryption fails. For more information about how to use HLS encryption, see [HLS encryption](https://help.aliyun.com/document_detail/68612.html).
        # 
        # *   You must select HLS encryption for the template specified by **TemplateGroupId** no matter you use HLS encryption or Alibaba Cloud proprietary cryptography. Otherwise, the transcoded file is not encrypted.
        self.encrypt_config = encrypt_config
        # The override parameter. The value must be a JSON string. You can use this parameter to override the image watermark, text watermark, or subtitle file specified in the transcoding template, or override the encoding format of the subtitle file. For more information about the data structure, see [OverrideParams](https://help.aliyun.com/document_detail/98618.html).
        self.override_params = override_params
        # The ID of the queue that you want to use to run the job.
        self.pipeline_id = pipeline_id
        # The priority of the transcoding job in all queued jobs.
        # 
        # *   Valid values: **1** to **10**.
        # *   A value of **10** indicates the highest priority.
        # *   Default value: **6**.
        # 
        # >  This parameter takes effect only on the queued transcoding jobs. The priorities of the in-progress transcoding jobs are not affected.
        self.priority = priority
        self.reference_id = reference_id
        # The custom identifier for deduplication. If you send a request, an error is returned if a request with the same identifier was sent in the last 7 days. A custom identifier can be up to 50 characters in length and can contain letters, digits, hyphens (-), and underscores (_). If you do not specify this parameter or leave this parameter empty, duplicate requests are not filtered.
        self.session_id = session_id
        # The ID of the transcoding template group that you want to use. To view the template group ID, perform the following operations: Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Processing** > **Transcoding Template Groups**.
        # 
        # This parameter is required.
        self.template_group_id = template_group_id
        # The custom settings. The value must be a JSON string. You can configure settings such as message callbacks. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # 
        # >  To use the callback configurations specified by this parameter, you must configure an HTTP callback URL and specify the types of the callback events in the ApsaraVideo VOD console. Otherwise, the callback configurations do not take effect.
        self.user_data = user_data
        # The ID of the video file. You can use one of the following methods to obtain the video ID:
        # 
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the video file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you call to upload the video.
        # *   Obtain the value of VideoId from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation after you upload the video.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypt_config is not None:
            result['EncryptConfig'] = self.encrypt_config

        if self.override_params is not None:
            result['OverrideParams'] = self.override_params

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptConfig') is not None:
            self.encrypt_config = m.get('EncryptConfig')

        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

