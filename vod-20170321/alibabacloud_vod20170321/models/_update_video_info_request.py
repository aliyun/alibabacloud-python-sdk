# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVideoInfoRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cover_url: str = None,
        description: str = None,
        reference_id: str = None,
        tags: str = None,
        title: str = None,
        user_data: str = None,
        video_id: str = None,
    ):
        # The category ID. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Categories** to view the category ID of the media file.
        # *   View the value of the CateId parameter returned by the [AddCategory](https://help.aliyun.com/document_detail/56401.html) operation that you called to create a category.
        # *   View the value of the CateId parameter returned by the [GetCategories](https://help.aliyun.com/document_detail/56406.html) operation that you called to query a category.
        self.cate_id = cate_id
        # The URL of the audio/video thumbnail.
        self.cover_url = cover_url
        # The description of the audio or video file.
        # 
        # *   The description can be up to 1,024 bytes in length.
        # *   The value is encoded in UTF-8.
        self.description = description
        self.reference_id = reference_id
        # The tags of the media file.
        # 
        # *   Each tag can be up to 32 bytes in length. You can specify up to 16 tags.
        # *   Separate multiple tags with commas (,).
        # *   The value is encoded in UTF-8.
        self.tags = tags
        # The title of the audio or video file.
        # 
        # *   The name cannot exceed 128 bytes.
        # *   The value is encoded in UTF-8.
        self.title = title
        # Custom settings. This is a JSON string that supports message callbacks, upload acceleration, and other settings. For more information, please refer to [UserData](https://help.aliyun.com/document_detail/86952.html).
        self.user_data = user_data
        # The ID of the audio or video file. Perform the following operations to obtain the storage address:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the audio or video file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you called to obtain the upload URL and credential.
        # *   View the value of the VideoId parameter returned by the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you called to query media information after the audio or video file is uploaded.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

