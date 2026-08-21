# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshUploadVideoRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        reference_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        video_id: str = None,
    ):
        self.owner_id = owner_id
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens, and underscores are supported. The value must be 6 to 64 characters in length and is unique at the user level.
        self.reference_id = reference_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The audio or video ID. You can obtain the ID by using one of the following methods:
        # - For videos uploaded by using the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - If the audio or video is uploaded by calling the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation, the audio or video ID is the value of the VideoId parameter in the response.
        # - After the audio or video is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId parameter in the response.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

