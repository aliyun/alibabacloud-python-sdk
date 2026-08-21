# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDynamicImageRequest(DaraModel):
    def __init__(
        self,
        dynamic_image_ids: str = None,
        video_id: str = None,
    ):
        # The list of animated sticker IDs. The animated sticker ID is the value of the DynamicImageId response parameter returned by the [ListDynamicImage](https://help.aliyun.com/document_detail/180958.html) operation.
        # 
        # - Separate multiple IDs with commas (,). You can specify a maximum of 10 IDs.
        # - **If you do not specify this parameter, all animated stickers associated with the specified VideoId are deleted. However, if the video has more than 10 animated stickers, the deletion request is rejected.**
        self.dynamic_image_ids = dynamic_image_ids
        # The ID of the video associated with the animated stickers that you want to delete. You can obtain the video ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - Obtain the video ID from the value of the VideoId response parameter when you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential.
        # - After the video is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID, which is the value of the VideoId response parameter.
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
        if self.dynamic_image_ids is not None:
            result['DynamicImageIds'] = self.dynamic_image_ids

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicImageIds') is not None:
            self.dynamic_image_ids = m.get('DynamicImageIds')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

