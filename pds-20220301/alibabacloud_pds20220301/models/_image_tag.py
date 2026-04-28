# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageTag(DaraModel):
    def __init__(
        self,
        count: int = None,
        cover_file_category: str = None,
        cover_file_id: str = None,
        cover_overall_score: float = None,
        cover_tag_confidence: float = None,
        cover_url: str = None,
        name: str = None,
    ):
        # The number of files in the group.
        self.count = count
        # The category of the cover image.
        self.cover_file_category = cover_file_category
        # The ID of the cover file.
        self.cover_file_id = cover_file_id
        # The score of the cover image.
        self.cover_overall_score = cover_overall_score
        # The confidence level of the cover image tag.
        self.cover_tag_confidence = cover_tag_confidence
        # The URL of the cover image.
        self.cover_url = cover_url
        # The name of the tag.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.cover_file_category is not None:
            result['cover_file_category'] = self.cover_file_category

        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id

        if self.cover_overall_score is not None:
            result['cover_overall_score'] = self.cover_overall_score

        if self.cover_tag_confidence is not None:
            result['cover_tag_confidence'] = self.cover_tag_confidence

        if self.cover_url is not None:
            result['cover_url'] = self.cover_url

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('cover_file_category') is not None:
            self.cover_file_category = m.get('cover_file_category')

        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')

        if m.get('cover_overall_score') is not None:
            self.cover_overall_score = m.get('cover_overall_score')

        if m.get('cover_tag_confidence') is not None:
            self.cover_tag_confidence = m.get('cover_tag_confidence')

        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

