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
        # The category ID. You can obtain the ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Asset Management Settings** > **Category Management** to view the category ID.
        # - When you call the [AddCategory](https://help.aliyun.com/document_detail/56401.html) operation to create a category, the category ID is the value of the CateId response parameter.
        # - When you call the [GetCategories](https://help.aliyun.com/document_detail/56406.html) operation to query categories, the category ID is the value of the CateId response parameter.
        self.cate_id = cate_id
        # The URL of the thumbnail for the audio or video file.
        self.cover_url = cover_url
        # The description of the audio or video file.
        # 
        # - The description can be up to 1,024 bytes in length.
        # - The description must be encoded in UTF-8.
        self.description = description
        # The custom ID. The ID must be 6 to 64 characters in length and can contain only lowercase letters, uppercase letters, digits, hyphens, and underscores. The ID must be unique per user.
        self.reference_id = reference_id
        # The tags.
        # 
        # - A single tag can be up to 32 bytes in length. You can add up to 16 tags.
        # - Separate multiple tags with commas (,).
        # - Tags must be encoded in UTF-8.
        self.tags = tags
        # The title of the audio or video file.
        # 
        # - The title can be up to 128 bytes in length.
        # - The title must be encoded in UTF-8.
        self.title = title
        # The custom settings. The value is a JSON string that supports settings such as message callbacks and upload acceleration. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        self.user_data = user_data
        # The audio or video file ID. You can obtain the ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Assets** > **Audio and Video** to view the audio or video file ID.
        # - When you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the audio or video file ID is the value of the VideoId response parameter.
        # - After a video is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video file ID. The ID is the value of the VideoId response parameter.
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

