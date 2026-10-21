# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SizeChartExtractAsyncRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        column_name_list: List[str] = None,
        image_url: str = None,
        language_model: str = None,
    ):
        # The business order number of the caller. It is recorded when the request is accepted and returned as is when you query the asynchronous task result.
        self.biz_id = biz_id
        # The list of column names to extract, such as Size, Bust, and Length.
        self.column_name_list = column_name_list
        # The image URL. The image must be in the JPG, JPEG, PNG, BMP, or WEBP format. The resolution must be between 256 × 256 pixels and 3000 × 3000 pixels, and the file size cannot exceed 10 MB.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The output language format. If you do not specify this parameter, the original language is used. If the original image language is Chinese or English, specifying en outputs English, and specifying cn outputs Chinese.
        self.language_model = language_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.column_name_list is not None:
            result['ColumnNameList'] = self.column_name_list

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.language_model is not None:
            result['LanguageModel'] = self.language_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ColumnNameList') is not None:
            self.column_name_list = m.get('ColumnNameList')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('LanguageModel') is not None:
            self.language_model = m.get('LanguageModel')

        return self

