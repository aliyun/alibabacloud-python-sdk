# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class WritingOutline(DaraModel):
    def __init__(
        self,
        articles: List[main_models.OutlineWritingArticle] = None,
        children: List[main_models.WritingOutline] = None,
        outline: str = None,
        outline_id: str = None,
        search_key_word_list: List[str] = None,
        word_count: str = None,
        writing_tips: str = None,
    ):
        self.articles = articles
        self.children = children
        self.outline = outline
        self.outline_id = outline_id
        self.search_key_word_list = search_key_word_list
        self.word_count = word_count
        self.writing_tips = writing_tips

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()
        if self.children:
            for v1 in self.children:
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

        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.outline is not None:
            result['Outline'] = self.outline

        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id

        if self.search_key_word_list is not None:
            result['SearchKeyWordList'] = self.search_key_word_list

        if self.word_count is not None:
            result['WordCount'] = self.word_count

        if self.writing_tips is not None:
            result['WritingTips'] = self.writing_tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.OutlineWritingArticle()
                self.articles.append(temp_model.from_map(k1))

        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.WritingOutline()
                self.children.append(temp_model.from_map(k1))

        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')

        if m.get('SearchKeyWordList') is not None:
            self.search_key_word_list = m.get('SearchKeyWordList')

        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        if m.get('WritingTips') is not None:
            self.writing_tips = m.get('WritingTips')

        return self

