# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class FuzzyMatchDomainSensitiveWordResponseBody(DaraModel):
    def __init__(
        self,
        exist: bool = None,
        keyword: str = None,
        matched_sentive_words: main_models.FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords = None,
        request_id: str = None,
    ):
        self.exist = exist
        self.keyword = keyword
        self.matched_sentive_words = matched_sentive_words
        self.request_id = request_id

    def validate(self):
        if self.matched_sentive_words:
            self.matched_sentive_words.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exist is not None:
            result['Exist'] = self.exist

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.matched_sentive_words is not None:
            result['MatchedSentiveWords'] = self.matched_sentive_words.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MatchedSentiveWords') is not None:
            temp_model = main_models.FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords()
            self.matched_sentive_words = temp_model.from_map(m.get('MatchedSentiveWords'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords(DaraModel):
    def __init__(
        self,
        matched_sensitive_word: List[main_models.FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord] = None,
    ):
        self.matched_sensitive_word = matched_sensitive_word

    def validate(self):
        if self.matched_sensitive_word:
            for v1 in self.matched_sensitive_word:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MatchedSensitiveWord'] = []
        if self.matched_sensitive_word is not None:
            for k1 in self.matched_sensitive_word:
                result['MatchedSensitiveWord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matched_sensitive_word = []
        if m.get('MatchedSensitiveWord') is not None:
            for k1 in m.get('MatchedSensitiveWord'):
                temp_model = main_models.FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord()
                self.matched_sensitive_word.append(temp_model.from_map(k1))

        return self

class FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord(DaraModel):
    def __init__(
        self,
        word: str = None,
    ):
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

