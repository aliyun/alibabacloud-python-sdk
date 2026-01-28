# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class BatchFuzzyMatchDomainSensitiveWordResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sensitive_word_match_result_list: main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList = None,
    ):
        self.request_id = request_id
        self.sensitive_word_match_result_list = sensitive_word_match_result_list

    def validate(self):
        if self.sensitive_word_match_result_list:
            self.sensitive_word_match_result_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sensitive_word_match_result_list is not None:
            result['SensitiveWordMatchResultList'] = self.sensitive_word_match_result_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SensitiveWordMatchResultList') is not None:
            temp_model = main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList()
            self.sensitive_word_match_result_list = temp_model.from_map(m.get('SensitiveWordMatchResultList'))

        return self

class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList(DaraModel):
    def __init__(
        self,
        sensitive_word_match_result: List[main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult] = None,
    ):
        self.sensitive_word_match_result = sensitive_word_match_result

    def validate(self):
        if self.sensitive_word_match_result:
            for v1 in self.sensitive_word_match_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SensitiveWordMatchResult'] = []
        if self.sensitive_word_match_result is not None:
            for k1 in self.sensitive_word_match_result:
                result['SensitiveWordMatchResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_word_match_result = []
        if m.get('SensitiveWordMatchResult') is not None:
            for k1 in m.get('SensitiveWordMatchResult'):
                temp_model = main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult()
                self.sensitive_word_match_result.append(temp_model.from_map(k1))

        return self

class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult(DaraModel):
    def __init__(
        self,
        exist: bool = None,
        keyword: str = None,
        matched_sentive_words: main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords = None,
    ):
        self.exist = exist
        self.keyword = keyword
        self.matched_sentive_words = matched_sentive_words

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MatchedSentiveWords') is not None:
            temp_model = main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords()
            self.matched_sentive_words = temp_model.from_map(m.get('MatchedSentiveWords'))

        return self

class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords(DaraModel):
    def __init__(
        self,
        matched_sensitive_word: List[main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord] = None,
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
                temp_model = main_models.BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord()
                self.matched_sensitive_word.append(temp_model.from_map(k1))

        return self



class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord(DaraModel):
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

