# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportMediaRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        cover_url: str = None,
        description: str = None,
        dynamic_meta_data: str = None,
        entity_id: str = None,
        import_source: str = None,
        input_url: str = None,
        media_tags: str = None,
        media_type: str = None,
        overwrite: bool = None,
        register_config: str = None,
        title: str = None,
        user_data: str = None,
    ):
        self.category_id = category_id
        self.cover_url = cover_url
        self.description = description
        self.dynamic_meta_data = dynamic_meta_data
        self.entity_id = entity_id
        self.import_source = import_source
        self.input_url = input_url
        self.media_tags = media_tags
        self.media_type = media_type
        self.overwrite = overwrite
        self.register_config = register_config
        self.title = title
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.dynamic_meta_data is not None:
            result['DynamicMetaData'] = self.dynamic_meta_data

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.import_source is not None:
            result['ImportSource'] = self.import_source

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.register_config is not None:
            result['RegisterConfig'] = self.register_config

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DynamicMetaData') is not None:
            self.dynamic_meta_data = m.get('DynamicMetaData')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('ImportSource') is not None:
            self.import_source = m.get('ImportSource')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('RegisterConfig') is not None:
            self.register_config = m.get('RegisterConfig')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

