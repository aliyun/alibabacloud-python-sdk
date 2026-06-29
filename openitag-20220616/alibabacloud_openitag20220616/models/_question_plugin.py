# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class QuestionPlugin(DaraModel):
    def __init__(
        self,
        can_select: bool = None,
        children: List[main_models.QuestionPlugin] = None,
        default_result: str = None,
        display: bool = None,
        exif: Dict[str, Any] = None,
        hot_key_map: str = None,
        mark_title: str = None,
        mark_title_alias: str = None,
        must_fill: bool = None,
        options: List[main_models.QuestionOption] = None,
        pre_options: List[str] = None,
        question_id: str = None,
        rule: str = None,
        select_group: str = None,
        selected: bool = None,
        type: str = None,
    ):
        # Whether it can be selected
        self.can_select = can_select
        # List of child widgets
        self.children = children
        # Default result
        self.default_result = default_result
        # Whether it is displayed
        # 
        # This parameter is required.
        self.display = display
        # Additional remarks
        self.exif = exif
        # Keyboard shortcut map
        self.hot_key_map = hot_key_map
        # Widget title
        # 
        # This parameter is required.
        self.mark_title = mark_title
        # Question alias
        self.mark_title_alias = mark_title_alias
        # Whether it is required
        # 
        # This parameter is required.
        self.must_fill = must_fill
        # List of options configuration
        # 
        # This parameter is required.
        self.options = options
        # List of predefined options for fill-in-the-blank questions
        self.pre_options = pre_options
        # Question widget ID
        # 
        # This parameter is required.
        self.question_id = question_id
        # Regular expression, validation rule
        self.rule = rule
        # Selection group
        self.select_group = select_group
        # Whether it is selected
        self.selected = selected
        # Widget type
        # 
        # This parameter is required.
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
        if self.can_select is not None:
            result['CanSelect'] = self.can_select

        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.default_result is not None:
            result['DefaultResult'] = self.default_result

        if self.display is not None:
            result['Display'] = self.display

        if self.exif is not None:
            result['Exif'] = self.exif

        if self.hot_key_map is not None:
            result['HotKeyMap'] = self.hot_key_map

        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title

        if self.mark_title_alias is not None:
            result['MarkTitleAlias'] = self.mark_title_alias

        if self.must_fill is not None:
            result['MustFill'] = self.must_fill

        result['Options'] = []
        if self.options is not None:
            for k1 in self.options:
                result['Options'].append(k1.to_map() if k1 else None)

        if self.pre_options is not None:
            result['PreOptions'] = self.pre_options

        if self.question_id is not None:
            result['QuestionId'] = self.question_id

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.select_group is not None:
            result['SelectGroup'] = self.select_group

        if self.selected is not None:
            result['Selected'] = self.selected

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSelect') is not None:
            self.can_select = m.get('CanSelect')

        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.QuestionPlugin()
                self.children.append(temp_model.from_map(k1))

        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('HotKeyMap') is not None:
            self.hot_key_map = m.get('HotKeyMap')

        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')

        if m.get('MarkTitleAlias') is not None:
            self.mark_title_alias = m.get('MarkTitleAlias')

        if m.get('MustFill') is not None:
            self.must_fill = m.get('MustFill')

        self.options = []
        if m.get('Options') is not None:
            for k1 in m.get('Options'):
                temp_model = main_models.QuestionOption()
                self.options.append(temp_model.from_map(k1))

        if m.get('PreOptions') is not None:
            self.pre_options = m.get('PreOptions')

        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('SelectGroup') is not None:
            self.select_group = m.get('SelectGroup')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

