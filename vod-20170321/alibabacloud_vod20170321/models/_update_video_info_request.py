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
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Management** > **Categories** to view the category ID.
        # - Obtain the category ID from the value of the CateId response parameter when you call the [AddCategory](https://help.aliyun.com/document_detail/56401.html) operation to create a category.
        # - Call the [GetCategories](https://help.aliyun.com/document_detail/56406.html) operation to query the category ID, which is the value of the CateId response parameter.
        self.cate_id = cate_id
        # The thumbnail URL of the audio or video file.
        self.cover_url = cover_url
        # The description of the audio or video file.
        # 
        # - The description can be up to 1024 bytes in length.
        # - The value is encoded in UTF-8.
        self.description = description
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens, and underscores are supported. The value must be 6 to 64 characters in length and is unique at the user level.
        self.reference_id = reference_id
        # The tags.
        # 
        # - Each tag can be up to 32 bytes in length. A maximum of 16 tags can be specified.
        # - Separate multiple tags with commas (,).
        # - The value is encoded in UTF-8.
        self.tags = tags
        # The title of the audio or video file.
        # 
        # - The title can be up to 128 bytes in length.
        # - The value is encoded in UTF-8.
        self.title = title
        # The custom settings. The value is a JSON string that supports settings such as message callbacks and upload acceleration. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        self.user_data = user_data
        # The audio or video ID. You can obtain the ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - Obtain the video ID from the value of the VideoId response parameter when you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential.
        # - After the video is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
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

