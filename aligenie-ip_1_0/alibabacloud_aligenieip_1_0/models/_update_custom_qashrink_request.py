# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomQAShrinkRequest(DaraModel):
    def __init__(
        self,
        answers_shrink: str = None,
        custom_qaid: str = None,
        hotel_id: str = None,
        key_words_shrink: str = None,
        major_question: str = None,
        supplementary_questions_shrink: str = None,
    ):
        self.answers_shrink = answers_shrink
        # This parameter is required.
        self.custom_qaid = custom_qaid
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words_shrink = key_words_shrink
        self.major_question = major_question
        self.supplementary_questions_shrink = supplementary_questions_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answers_shrink is not None:
            result['Answers'] = self.answers_shrink

        if self.custom_qaid is not None:
            result['CustomQAId'] = self.custom_qaid

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.key_words_shrink is not None:
            result['KeyWords'] = self.key_words_shrink

        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question

        if self.supplementary_questions_shrink is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers_shrink = m.get('Answers')

        if m.get('CustomQAId') is not None:
            self.custom_qaid = m.get('CustomQAId')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('KeyWords') is not None:
            self.key_words_shrink = m.get('KeyWords')

        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')

        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions_shrink = m.get('SupplementaryQuestions')

        return self

