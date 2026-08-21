# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteImageRequest(DaraModel):
    def __init__(
        self,
        delete_image_type: str = None,
        image_ids: str = None,
        image_type: str = None,
        image_urls: str = None,
        video_id: str = None,
    ):
        # The type of image deletion operation. Valid values:
        # 
        # - **ImageURL**: deletes images based on image URLs.
        # - **ImageId**: deletes images based on image IDs.
        # - **VideoId**: deletes images associated with a video based on the video ID.
        # 
        # This parameter is required.
        self.delete_image_type = delete_image_type
        # The image IDs. Separate multiple IDs with commas (,). A maximum of 20 IDs are supported. You can obtain image IDs by using the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Image** to view the IDs.
        # - Obtain the IDs from the response of the [CreateUploadImage](~~CreateUploadImage~~) operation that is called to obtain the upload URL and credential.
        # - Obtain the IDs from the response of the [SearchMedia](~~SearchMedia~~) operation that is called to query images.
        # 
        # > This parameter is available and required only when **DeleteImageType** is set to **ImageId**.
        self.image_ids = image_ids
        # The type of images associated with the video that you want to delete. Valid values:
        # 
        # - **CoverSnapshot**: thumbnail snapshot.
        # - **NormalSnapshot**: regular snapshot.
        # - **SpriteSnapshot**: sprite snapshot.
        # - **SpriteOriginSnapshot**: sprite source image.
        # - **All**: all of the preceding image types. If the value is not `All`, you can specify multiple image types. Separate multiple values with commas (,).
        # 
        # > This parameter is available and required only when **DeleteImageType** is set to **VideoId**.
        self.image_type = image_type
        # The image URLs. The value is the `ImageURL` parameter returned by the [CreateUploadImage](~~CreateUploadImage~~) operation. Separate multiple URLs with commas (,). A maximum of 20 URLs are supported.
        # 
        # > This parameter is available and required only when **DeleteImageType** is set to **ImageURL**.
        self.image_urls = image_urls
        # The video ID. Only a single video ID is supported. You can obtain the video ID by using the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - Obtain the ID from the response of the [CreateUploadVideo](~~CreateUploadVideo~~) operation that is called to obtain the upload URL and credential.
        # - Obtain the ID from the response of the [SearchMedia](~~SearchMedia~~) operation that is called to query videos.
        # 
        # > This parameter is available and required only when **DeleteImageType** is set to **VideoId**.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_image_type is not None:
            result['DeleteImageType'] = self.delete_image_type

        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.image_urls is not None:
            result['ImageURLs'] = self.image_urls

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteImageType') is not None:
            self.delete_image_type = m.get('DeleteImageType')

        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ImageURLs') is not None:
            self.image_urls = m.get('ImageURLs')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

