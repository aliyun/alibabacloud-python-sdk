# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ImageInsight(DaraModel):
    def __init__(
        self,
        caption: str = None,
        description: str = None,
        multilingual_content: Dict[str, main_models.MultilingualContentEntry] = None,
    ):
        self.caption = caption
        self.description = description
        # The multilingual image content.
        self.multilingual_content = multilingual_content

    def validate(self):
        if self.multilingual_content:
            for v1 in self.multilingual_content.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.description is not None:
            result['Description'] = self.description

        result['MultilingualContent'] = {}
        if self.multilingual_content is not None:
            for k1, v1 in self.multilingual_content.items():
                result['MultilingualContent'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.multilingual_content = {}
        if m.get('MultilingualContent') is not None:
            for k1, v1 in m.get('MultilingualContent').items():
                temp_model = main_models.MultilingualContentEntry()
                self.multilingual_content[k1] = temp_model.from_map(v1)

        return self

