# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchImageRequest(DaraModel):
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
        tags: List[str] = None,
        text: str = None,
    ):
        # Color
        self.color_hex = color_hex
        # Indicates whether the image contains a person.
        self.has_person = has_person
        # Image category. Valid values:
        # - normal: Illustrations or article images.
        # - banner: Background images or image carousels.
        # - goods: Product or service images.
        self.image_category = image_category
        # Image aspect ratio, including:
        # "16:9"
        # "4:3"
        # "2:1"
        # "1:1"
        # "3:4"
        # "9:16"
        self.image_ratio = image_ratio
        # Maximum image height.
        self.max_height = max_height
        # Number of items per page in a paged query. Maximum value is 100. Default value is 20.
        self.max_results = max_results
        # Maximum image width (inclusive).
        self.max_width = max_width
        # Minimum image height
        self.min_height = min_height
        # Minimum image width (inclusive).
        self.min_width = min_width
        # Query credential (Token). Set this parameter to the NextToken value returned in the previous API call. You do not need to set this parameter for the initial API call. If NextToken is specified, the request parameters PageSize and PageNumber become invalid, and the TotalCount in the returned data is also invalid.
        self.next_token = next_token
        # Osskey。
        self.oss_key = oss_key
        # Number of results to return. Default value is 10.
        self.size = size
        # Starting position of the return result. Valid values: 0 to 499. Default value is 0.
        self.start = start
        # Tags.
        self.tags = tags
        # Description text for searching images.
        # 
        # > Supports up to 512 characters.
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

        if self.tags is not None:
            result['Tags'] = self.tags

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
            self.tags = m.get('Tags')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

