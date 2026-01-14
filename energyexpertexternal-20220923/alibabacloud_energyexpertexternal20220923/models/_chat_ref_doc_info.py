# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class ChatRefDocInfo(DaraModel):
    def __init__(
        self,
        page_list_info: List[main_models.ChatRefDocPageInfo] = None,
        pages: int = None,
    ):
        self.page_list_info = page_list_info
        self.pages = pages

    def validate(self):
        if self.page_list_info:
            for v1 in self.page_list_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['pageListInfo'] = []
        if self.page_list_info is not None:
            for k1 in self.page_list_info:
                result['pageListInfo'].append(k1.to_map() if k1 else None)

        if self.pages is not None:
            result['pages'] = self.pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_list_info = []
        if m.get('pageListInfo') is not None:
            for k1 in m.get('pageListInfo'):
                temp_model = main_models.ChatRefDocPageInfo()
                self.page_list_info.append(temp_model.from_map(k1))

        if m.get('pages') is not None:
            self.pages = m.get('pages')

        return self

