# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SizeChartExtractRequest(DaraModel):
    def __init__(
        self,
        column_name_list: List[str] = None,
        image_url: str = None,
        language_model: str = None,
    ):
        # The list of column names to extract, such as Size, Bust, and Length.
        self.column_name_list = column_name_list
        # The URL of the size chart image to extract.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The language model that controls the output language, such as en and cn.
        self.language_model = language_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name_list is not None:
            result['ColumnNameList'] = self.column_name_list

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.language_model is not None:
            result['LanguageModel'] = self.language_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnNameList') is not None:
            self.column_name_list = m.get('ColumnNameList')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('LanguageModel') is not None:
            self.language_model = m.get('LanguageModel')

        return self

