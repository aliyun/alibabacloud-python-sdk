# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaRequest(DaraModel):
    def __init__(
        self,
        append_tags: bool = None,
        cover_url: str = None,
        description: str = None,
        dynamic_meta_data: str = None,
        input_url: str = None,
        media_id: str = None,
        media_tags: str = None,
        title: str = None,
        user_data: str = None,
    ):
        self.append_tags = append_tags
        self.cover_url = cover_url
        self.description = description
        self.dynamic_meta_data = dynamic_meta_data
        self.input_url = input_url
        self.media_id = media_id
        self.media_tags = media_tags
        self.title = title
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

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.dynamic_meta_data is not None:
            result['DynamicMetaData'] = self.dynamic_meta_data

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppendTags') is not None:
            self.append_tags = m.get('AppendTags')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DynamicMetaData') is not None:
            self.dynamic_meta_data = m.get('DynamicMetaData')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

