# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class TemplateQuestion(DaraModel):
    def __init__(
        self,
        children: List[main_models.TemplateQuestion] = None,
        exif: Dict[str, Any] = None,
        mark_title: str = None,
        options: List[main_models.QuestionOption] = None,
        pre_options: List[str] = None,
        question_id: int = None,
        type: str = None,
    ):
        # List of child nodes
        self.children = children
        # Additional properties
        self.exif = exif
        # Title
        self.mark_title = mark_title
        # List of options
        self.options = options
        # List of pre-filled values
        self.pre_options = pre_options
        # Question ID
        self.question_id = question_id
        # Type, including the following:  
        # - TEXT_EDIT  
        # - CHECKBOX  
        # - INPUT  
        # - PICTURE  
        # - VIDEO  
        # - OPEN_ENDED  
        # - SLOT  
        # - RADIO
        self.type = type

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()
        if self.options:
            for v1 in self.options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.exif is not None:
            result['Exif'] = self.exif

        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title

        result['Options'] = []
        if self.options is not None:
            for k1 in self.options:
                result['Options'].append(k1.to_map() if k1 else None)

        if self.pre_options is not None:
            result['PreOptions'] = self.pre_options

        if self.question_id is not None:
            result['QuestionId'] = self.question_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.TemplateQuestion()
                self.children.append(temp_model.from_map(k1))

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')

        self.options = []
        if m.get('Options') is not None:
            for k1 in m.get('Options'):
                temp_model = main_models.QuestionOption()
                self.options.append(temp_model.from_map(k1))

        if m.get('PreOptions') is not None:
            self.pre_options = m.get('PreOptions')

        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

