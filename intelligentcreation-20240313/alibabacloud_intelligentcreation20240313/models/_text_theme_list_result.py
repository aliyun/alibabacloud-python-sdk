# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class TextThemeListResult(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        text_theme_list: List[main_models.TextTheme] = None,
    ):
        self.request_id = request_id
        # This parameter is required.
        self.text_theme_list = text_theme_list

    def validate(self):
        if self.text_theme_list:
            for v1 in self.text_theme_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['textThemeList'] = []
        if self.text_theme_list is not None:
            for k1 in self.text_theme_list:
                result['textThemeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.text_theme_list = []
        if m.get('textThemeList') is not None:
            for k1 in m.get('textThemeList'):
                temp_model = main_models.TextTheme()
                self.text_theme_list.append(temp_model.from_map(k1))

        return self

