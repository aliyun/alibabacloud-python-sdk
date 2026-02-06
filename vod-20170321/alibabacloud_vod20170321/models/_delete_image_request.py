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
        # The method that is used to delete images. Valid values:
        # 
        # *   **ImageURL**: deletes images based on URLs.
        # *   **ImageId**: deletes images based on image IDs.
        # *   **VideoId**: deletes images associated with a video based on the video ID.
        # 
        # This parameter is required.
        self.delete_image_type = delete_image_type
        # The ID of the image. You can specify up to 20 image IDs and separate them with commas (,). You can use one of the following methods to obtain the image ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Media Files** > **Image** to view the image ID.
        # *   Obtain the image ID from the response to the [CreateUploadImage](~~CreateUploadImage~~) operation that you call to obtain the upload credential and URL.
        # *   Obtain the image ID from the response to the [SearchMedia](~~SearchMedia~~) operation that you call to query images.
        # 
        # >  This parameter takes effect and is required only if you set **DeleteImageType** to **ImageId**.
        self.image_ids = image_ids
        # The type of images that you want to delete. The images are associated with the video. Valid values:
        # 
        # *   **CoverSnapshot**: thumbnail snapshot.
        # *   **NormalSnapshot**: regular snapshot.
        # *   **SpriteSnapshot**: sprite snapshot.
        # *   **SpriteOriginSnapshot**: sprite source snapshot.
        # *   **All**: images of all the preceding types. You can specify multiple types other than `All` for this parameter. Separate multiple types with commas (,).
        # 
        # >  This parameter takes effect and is required only if you set **DeleteImageType** to **VideoId**.
        self.image_type = image_type
        # The URL of the image. You can obtain the value of `ImageURL` from the response to the [CreateUploadImage](~~CreateUploadImage~~) operation. You can specify up to 20 URLs and separate them with commas (,).
        # 
        # >  This parameter takes effect and is required only if you set **DeleteImageType** to **ImageURL**.
        self.image_urls = image_urls
        # The ID of the video. You can specify only one ID. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the media file.
        # *   Obtain the video ID from the response to the [CreateUploadVideo](~~CreateUploadVideo~~) operation that you call to obtain the upload credential and URL.
        # *   Obtain the video ID from the response to the [SearchMedia](~~SearchMedia~~) operation that you call to query videos.
        # 
        # >  This parameter takes effect and is required only if you set **DeleteImageType** to **VideoId**.
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

