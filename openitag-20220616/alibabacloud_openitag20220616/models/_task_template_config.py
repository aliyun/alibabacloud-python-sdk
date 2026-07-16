# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class TaskTemplateConfig(DaraModel):
    def __init__(
        self,
        exif: Dict[str, str] = None,
        resource_key: str = None,
        select_questions: List[str] = None,
        template_option_map: Dict[str, main_models.TaskTemplateOptionConfig] = None,
        template_relation_id: str = None,
    ):
        # Additional information for template configuration.
        self.exif = exif
        # Display field corresponding to the View.
        self.resource_key = resource_key
        # List of questions in the template.
        self.select_questions = select_questions
        # Template options configuration.
        self.template_option_map = template_option_map
        # Template ID on which this depends.
        self.template_relation_id = template_relation_id

    def validate(self):
        if self.template_option_map:
            for v1 in self.template_option_map.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exif is not None:
            result['Exif'] = self.exif

        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key

        if self.select_questions is not None:
            result['SelectQuestions'] = self.select_questions

        result['TemplateOptionMap'] = {}
        if self.template_option_map is not None:
            for k1, v1 in self.template_option_map.items():
                result['TemplateOptionMap'][k1] = v1.to_map() if v1 else None

        if self.template_relation_id is not None:
            result['TemplateRelationId'] = self.template_relation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')

        if m.get('SelectQuestions') is not None:
            self.select_questions = m.get('SelectQuestions')

        self.template_option_map = {}
        if m.get('TemplateOptionMap') is not None:
            for k1, v1 in m.get('TemplateOptionMap').items():
                temp_model = main_models.TaskTemplateOptionConfig()
                self.template_option_map[k1] = temp_model.from_map(v1)

        if m.get('TemplateRelationId') is not None:
            self.template_relation_id = m.get('TemplateRelationId')

        return self

