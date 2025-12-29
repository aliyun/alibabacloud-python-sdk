# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddCustomQAV2Request(DaraModel):
    def __init__(
        self,
        answers: List[str] = None,
        hotel_id: str = None,
        key_words: List[str] = None,
        major_question: str = None,
        supplementary_questions: List[str] = None,
    ):
        # This parameter is required.
        self.answers = answers
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words = key_words
        self.major_question = major_question
        self.supplementary_questions = supplementary_questions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answers is not None:
            result['Answers'] = self.answers

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question

        if self.supplementary_questions is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')

        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions = m.get('SupplementaryQuestions')

        return self

