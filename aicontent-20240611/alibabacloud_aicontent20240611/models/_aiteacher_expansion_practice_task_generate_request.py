# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AITeacherExpansionPracticeTaskGenerateRequest(DaraModel):
    def __init__(
        self,
        grade: str = None,
        key_sentences: List[str] = None,
        key_words: List[str] = None,
        learning_object: str = None,
        text_content: str = None,
        textbook: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.grade = grade
        self.key_sentences = key_sentences
        self.key_words = key_words
        self.learning_object = learning_object
        # This parameter is required.
        self.text_content = text_content
        self.textbook = textbook
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grade is not None:
            result['grade'] = self.grade

        if self.key_sentences is not None:
            result['keySentences'] = self.key_sentences

        if self.key_words is not None:
            result['keyWords'] = self.key_words

        if self.learning_object is not None:
            result['learningObject'] = self.learning_object

        if self.text_content is not None:
            result['textContent'] = self.text_content

        if self.textbook is not None:
            result['textbook'] = self.textbook

        if self.topic is not None:
            result['topic'] = self.topic

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('keySentences') is not None:
            self.key_sentences = m.get('keySentences')

        if m.get('keyWords') is not None:
            self.key_words = m.get('keyWords')

        if m.get('learningObject') is not None:
            self.learning_object = m.get('learningObject')

        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')

        if m.get('textbook') is not None:
            self.textbook = m.get('textbook')

        if m.get('topic') is not None:
            self.topic = m.get('topic')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

