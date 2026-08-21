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
        # The AI task pipeline ID.
        # 
        # > A default ID is available, so this parameter is optional. If you need to perform batch imports, use a separate task pipeline. Submit a ticket to request configuration or contact Alibaba Cloud after-sales support for configuration. For more information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
        self.aipipeline_id = aipipeline_id
        # The AI image template ID. You can obtain the template ID by using one of the following methods:
        # - When you create an image template by calling the [AddAITemplate](https://help.aliyun.com/document_detail/102930.html) operation, the template ID is the value of the TemplateId parameter in the response.
        # - After the template is created, you can call the [ListAITemplate](https://help.aliyun.com/document_detail/102936.html) operation to query the AI image template ID, which is the value of the TemplateId parameter in the response.
        # 
        # This parameter is required.
        self.aitemplate_id = aitemplate_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The custom settings.
        # - The value must be a JSON string.
        # - The value must contain the MessageCallback or Extend parameter.
        # - The maximum length is 512 bytes.
        # 
        # For more information about the parameter structure, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        self.user_data = user_data
        # The video ID. You can obtain the video ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - When you upload a video by calling the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation, the video ID is the value of the VideoId parameter in the response.
        # - After the video is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID, which is the value of the VideoId parameter in the response.
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

