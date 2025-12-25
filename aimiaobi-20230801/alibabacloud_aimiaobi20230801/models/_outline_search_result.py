# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class OutlineSearchResult(DaraModel):
    def __init__(
        self,
        articles: List[main_models.OutlineWritingArticle] = None,
        outline: str = None,
        outline_id: str = None,
        primary_outline: str = None,
        query: str = None,
    ):
        self.articles = articles
        self.outline = outline
        self.outline_id = outline_id
        self.primary_outline = primary_outline
        self.query = query

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Articles'] = []
        if self.articles is not None:
            for k1 in self.articles:
                result['Articles'].append(k1.to_map() if k1 else None)

        if self.outline is not None:
            result['Outline'] = self.outline

        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id

        if self.primary_outline is not None:
            result['PrimaryOutline'] = self.primary_outline

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.OutlineWritingArticle()
                self.articles.append(temp_model.from_map(k1))

        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')

        if m.get('PrimaryOutline') is not None:
            self.primary_outline = m.get('PrimaryOutline')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

