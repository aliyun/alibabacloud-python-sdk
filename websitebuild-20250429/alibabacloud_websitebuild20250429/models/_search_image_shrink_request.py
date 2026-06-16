# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchImageShrinkRequest(DaraModel):
    def __init__(
        self,
        color_hex: str = None,
        has_person: bool = None,
        image_category: str = None,
        image_ratio: str = None,
        max_height: int = None,
        max_results: int = None,
        max_width: int = None,
        min_height: int = None,
        min_width: int = None,
        next_token: str = None,
        oss_key: str = None,
        size: int = None,
        start: int = None,
        tags_shrink: str = None,
        text: str = None,
    ):
        # The color.
        self.color_hex = color_hex
        # Specifies whether the image contains a person.
        self.has_person = has_person
        # The image category. Valid values:
        # - normal: illustrations or article images.
        # - banner: background images or carousel images.
        # - goods: product or service images.
        self.image_category = image_category
        # The aspect ratio of the image. Valid values:
        # "16:9"
        # "4:3"
        # "2:1"
        # "1:1"
        # "3:4"
        # "9:16".
        self.image_ratio = image_ratio
        # The maximum height of the image.
        self.max_height = max_height
        # The number of entries per page for paging queries. Maximum value: 100. Default value: 20.
        self.max_results = max_results
        # The maximum width of the image, inclusive.
        self.max_width = max_width
        # The minimum height of the image.
        self.min_height = min_height
        # The minimum width of the image, inclusive.
        self.min_width = min_width
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request. If NextToken is specified, the PageSize and PageNumber request parameters do not take effect, and the TotalCount value in the response is invalid.
        self.next_token = next_token
        # The OSS key.
        self.oss_key = oss_key
        # The number of returned results. Default value: 10.
        self.size = size
        # The start position of the returned results. Valid values: 0 to 499. Default value: 0.
        self.start = start
        # The tags.
        self.tags_shrink = tags_shrink
        # The description text used to search for images.
        # 
        # >Maximum length: 512 characters.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color_hex is not None:
            result['ColorHex'] = self.color_hex

        if self.has_person is not None:
            result['HasPerson'] = self.has_person

        if self.image_category is not None:
            result['ImageCategory'] = self.image_category

        if self.image_ratio is not None:
            result['ImageRatio'] = self.image_ratio

        if self.max_height is not None:
            result['MaxHeight'] = self.max_height

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.max_width is not None:
            result['MaxWidth'] = self.max_width

        if self.min_height is not None:
            result['MinHeight'] = self.min_height

        if self.min_width is not None:
            result['MinWidth'] = self.min_width

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.size is not None:
            result['Size'] = self.size

        if self.start is not None:
            result['Start'] = self.start

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorHex') is not None:
            self.color_hex = m.get('ColorHex')

        if m.get('HasPerson') is not None:
            self.has_person = m.get('HasPerson')

        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')

        if m.get('ImageRatio') is not None:
            self.image_ratio = m.get('ImageRatio')

        if m.get('MaxHeight') is not None:
            self.max_height = m.get('MaxHeight')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MaxWidth') is not None:
            self.max_width = m.get('MaxWidth')

        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')

        if m.get('MinWidth') is not None:
            self.min_width = m.get('MinWidth')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

