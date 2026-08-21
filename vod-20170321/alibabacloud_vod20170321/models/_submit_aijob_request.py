# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIJobRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        media_id: str = None,
        owner_account: str = None,
        owner_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        types: str = None,
        user_data: str = None,
    ):
        # The AI job configuration in JSON format.
        # - If `Types` is set to `AIVideoTag`, `Config` supports the `AnalyseTypes` parameter to specify the analysis algorithm types for the intelligent tagging job. Valid values:
        #   - ASR: speech recognition. Identifies tags from the audio speech in the video.
        #   - OCR: optical character recognition. Identifies tags from the text in the video images.
        # - If `Types` is set to `AIMediaDNA`, `Config` supports the `DNADBId` parameter to specify the fingerprint library ID for the media fingerprint job.
        self.config = config
        # The video ID. You can obtain the video ID by using one of the following methods:
        # - For videos uploaded in the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - When you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the video ID is the value of the VideoId response parameter.
        # - After the video is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID, which is the value of the VideoId response parameter.
        self.media_id = media_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The AI job type. Separate multiple job types with commas (,). Valid values:
        # 
        # - **AIMediaDNA**: media fingerprint.
        # - **AIVideoTag**: intelligent tagging.
        self.types = types
        # The custom settings in JSON format. For more information about the parameter structure, see [UserData](~~86952#h2--userdata-div-id-userdata-div-3~~).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.types is not None:
            result['Types'] = self.types

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

