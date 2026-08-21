# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDigitalWatermarkExtractResultRequest(DaraModel):
    def __init__(
        self,
        extract_type: str = None,
        job_id: str = None,
        media_id: str = None,
        owner_account: str = None,
        owner_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
    ):
        # The type of watermark extraction. Valid values:
        # 
        # - **TraceMark**: tracing watermark.
        # - **CopyrightMark**: copyright watermark.
        # 
        # This parameter is required.
        self.extract_type = extract_type
        # The ID of the watermark extraction job.
        # - The job ID is returned after you call the [SubmitDigitalWatermarkExtractJob](~~SubmitDigitalWatermarkExtractJob~~) operation.
        # - If you specify this parameter, the result of the specified watermark extraction job is returned. If you do not specify this parameter, the results of all historical watermark extraction jobs for the video are returned.
        self.job_id = job_id
        # The ID of the video to query. Only a single video ID is supported. You can obtain the video ID by using the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - Call the [SearchMedia](~~SearchMedia~~) operation. The video ID (VideoId) is returned in the response.
        # 
        # This parameter is required.
        self.media_id = media_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extract_type is not None:
            result['ExtractType'] = self.extract_type

        if self.job_id is not None:
            result['JobId'] = self.job_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtractType') is not None:
            self.extract_type = m.get('ExtractType')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

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

        return self

