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
        self.color_hex = color_hex
        self.has_person = has_person
        self.image_category = image_category
        self.image_ratio = image_ratio
        self.max_height = max_height
        self.max_results = max_results
        self.max_width = max_width
        self.min_height = min_height
        self.min_width = min_width
        self.next_token = next_token
        # Osskey。
        self.oss_key = oss_key
        self.size = size
        self.start = start
        self.tags_shrink = tags_shrink
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

