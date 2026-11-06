# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawSkillTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        skill_templates: List[main_models.DescribePolarClawSkillTemplateResponseBodySkillTemplates] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The skill template group.
        self.skill_templates = skill_templates

    def validate(self):
        if self.skill_templates:
            for v1 in self.skill_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillTemplates'] = []
        if self.skill_templates is not None:
            for k1 in self.skill_templates:
                result['SkillTemplates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_templates = []
        if m.get('SkillTemplates') is not None:
            for k1 in m.get('SkillTemplates'):
                temp_model = main_models.DescribePolarClawSkillTemplateResponseBodySkillTemplates()
                self.skill_templates.append(temp_model.from_map(k1))

        return self

class DescribePolarClawSkillTemplateResponseBodySkillTemplates(DaraModel):
    def __init__(
        self,
        created: str = None,
        modified: str = None,
        skill_template_desc: str = None,
        skill_template_id: str = None,
        skill_template_name: str = None,
        skills: Dict[str, str] = None,
        src_application_id: str = None,
    ):
        # Indicates whether the template is actually created.
        self.created = created
        # The last modification time of the parameter template.
        self.modified = modified
        # The description of the skill template.
        self.skill_template_desc = skill_template_desc
        # The skill template ID.
        self.skill_template_id = skill_template_id
        # The name of the skill template.
        self.skill_template_name = skill_template_name
        # The map of associated skill details. The key is the skill identifier, and the value is a JSON string that can be parsed into an array of skill details. Each array element contains skillName and version.
        self.skills = skills
        # The source application ID.
        self.src_application_id = src_application_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['Created'] = self.created

        if self.modified is not None:
            result['Modified'] = self.modified

        if self.skill_template_desc is not None:
            result['SkillTemplateDesc'] = self.skill_template_desc

        if self.skill_template_id is not None:
            result['SkillTemplateId'] = self.skill_template_id

        if self.skill_template_name is not None:
            result['SkillTemplateName'] = self.skill_template_name

        if self.skills is not None:
            result['Skills'] = self.skills

        if self.src_application_id is not None:
            result['SrcApplicationId'] = self.src_application_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Modified') is not None:
            self.modified = m.get('Modified')

        if m.get('SkillTemplateDesc') is not None:
            self.skill_template_desc = m.get('SkillTemplateDesc')

        if m.get('SkillTemplateId') is not None:
            self.skill_template_id = m.get('SkillTemplateId')

        if m.get('SkillTemplateName') is not None:
            self.skill_template_name = m.get('SkillTemplateName')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        if m.get('SrcApplicationId') is not None:
            self.src_application_id = m.get('SrcApplicationId')

        return self

