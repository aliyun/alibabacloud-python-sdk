# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceKeywordsResponseBody(DaraModel):
    def __init__(
        self,
        key: str = None,
        request_id: str = None,
        words: main_models.DescribeInstanceKeywordsResponseBodyWords = None,
    ):
        # The type of reserved keyword returned.
        self.key = key
        # The ID of the request.
        self.request_id = request_id
        # The reserved keywords.
        self.words = words

    def validate(self):
        if self.words:
            self.words.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.words is not None:
            result['Words'] = self.words.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Words') is not None:
            temp_model = main_models.DescribeInstanceKeywordsResponseBodyWords()
            self.words = temp_model.from_map(m.get('Words'))

        return self

class DescribeInstanceKeywordsResponseBodyWords(DaraModel):
    def __init__(
        self,
        word: List[str] = None,
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
            result['word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')

        return self

