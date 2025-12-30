# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaInfoRequest(DaraModel):
    def __init__(
        self,
        append_tags: bool = None,
        business_type: str = None,
        cate_id: int = None,
        category: str = None,
        cover_url: str = None,
        description: str = None,
        input_url: str = None,
        media_id: str = None,
        media_tags: str = None,
        reference_id: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # Specifies whether to append tags. Default value: false. Valid values:
        # 
        # *   true: updates the MediaTags parameter by appending new tags.
        # *   false: updates the MediaTags parameter by overwriting existing tags with new tags.
        self.append_tags = append_tags
        # The business type. Valid values:
        # 
        # *   subtitles
        # *   watermark
        # *   opening
        # *   ending
        # *   general
        self.business_type = business_type
        # The category ID.
        self.cate_id = cate_id
        # The category.
        # 
        # *   The value can be up to 64 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.category = category
        # The URL of the thumbnail.
        # 
        # *   The value can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.cover_url = cover_url
        # The content description.
        # 
        # *   The value can be up to 1,024 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The input URL of the media asset in another service. The URL must be bound to the ID of the media asset in IMS. The URL cannot be modified once registered.
        # 
        # For a media asset from Object Storage Service (OSS), the URL may have one of the following formats:
        # 
        # 1\\. http(s)://example-bucket.oss-cn-shanghai.aliyuncs.com/example.mp4
        # 
        # 2\\. oss://example-bucket/example.mp4. This format indicates that the region in which the OSS bucket of the media asset resides is the same as the region in which OSS is activated.
        self.input_url = input_url
        # The ID of the media asset. If this parameter is left empty, you must specify the input URL of the media asset, which has been registered in the IMS content library.
        self.media_id = media_id
        # The tags.
        # 
        # *   Up to 16 tags are supported.
        # *   Separate multiple tags with commas (,).
        # *   Each tag can be up to 32 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.media_tags = media_tags
        # The custom ID. The ID can be 6 to 64 characters in length and can contain only letters, digits, hyphens (-), and underscores (_). Make sure that the ID is unique among users.
        self.reference_id = reference_id
        # The title.
        # 
        # *   The value can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.title = title
        # The user data. It can be up to 1,024 bytes in size.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.append_tags is not None:
            result['AppendTags'] = self.append_tags

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.category is not None:
            result['Category'] = self.category

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppendTags') is not None:
            self.append_tags = m.get('AppendTags')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

