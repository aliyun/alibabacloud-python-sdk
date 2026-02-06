# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIImageJobRequest(DaraModel):
    def __init__(
        self,
        aipipeline_id: str = None,
        aitemplate_id: str = None,
        owner_account: str = None,
        owner_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        user_data: str = None,
        video_id: str = None,
    ):
        # The ID of the pipeline that is used for the AI processing job.
        # 
        # >  This parameter is optional if you specify a default pipeline ID. If you want to use a separate pipeline to submit multiple AI processing jobs., submit a ticket or contact Alibaba Cloud after-sales engineers. For more information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
        self.aipipeline_id = aipipeline_id
        # The ID of the AI template. You can use one of the following methods to obtain the ID:
        # 
        # *   Obtain the value of TemplateId from the response to the [AddAITemplate](https://help.aliyun.com/document_detail/102930.html) that you call to create the template.
        # *   Obtain the value of TemplateId from the response to the [ListAITemplate](https://help.aliyun.com/document_detail/102936.html) operation after you create the template.
        # 
        # This parameter is required.
        self.aitemplate_id = aitemplate_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The user data.
        # 
        # *   The value must be a JSON string.
        # *   You must specify the MessageCallback or Extend parameter.
        # *   The value can contain a maximum of 512 bytes.
        # 
        # For more information, see the "UserData: specifies the custom configurations for media upload" section of the [Request parameters](https://help.aliyun.com/document_detail/86952.html) topic.
        self.user_data = user_data
        # The ID of the video. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the video file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you call to upload the video.
        # *   Obtain the value of VideoId from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation after you upload the video.
        # 
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aipipeline_id is not None:
            result['AIPipelineId'] = self.aipipeline_id

        if self.aitemplate_id is not None:
            result['AITemplateId'] = self.aitemplate_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIPipelineId') is not None:
            self.aipipeline_id = m.get('AIPipelineId')

        if m.get('AITemplateId') is not None:
            self.aitemplate_id = m.get('AITemplateId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

