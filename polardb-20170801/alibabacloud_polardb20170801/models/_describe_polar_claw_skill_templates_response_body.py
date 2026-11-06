# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawSkillTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        skill_templates: List[main_models.DescribePolarClawSkillTemplatesResponseBodySkillTemplates] = None,
        total_count: str = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The skill templates.
        self.skill_templates = skill_templates
        # The total number of entries. This parameter is returned only when you query a list.
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillTemplates'] = []
        if self.skill_templates is not None:
            for k1 in self.skill_templates:
                result['SkillTemplates'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_templates = []
        if m.get('SkillTemplates') is not None:
            for k1 in m.get('SkillTemplates'):
                temp_model = main_models.DescribePolarClawSkillTemplatesResponseBodySkillTemplates()
                self.skill_templates.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePolarClawSkillTemplatesResponseBodySkillTemplates(DaraModel):
    def __init__(
        self,
        created: str = None,
        id: str = None,
        modified: str = None,
        skill_counts: str = None,
        skill_template_desc: str = None,
        skill_template_id: str = None,
        skill_template_name: str = None,
        skill_template_type: str = None,
        src_application_id: str = None,
    ):
        # The time when the skill template was created in UTC.
        self.created = created
        # The rule ID.
        self.id = id
        # The time when the skill template was last modified in UTC.
        self.modified = modified
        # The number of skills.
        self.skill_counts = skill_counts
        # The skill template description.
        self.skill_template_desc = skill_template_desc
        # The skill template ID.
        self.skill_template_id = skill_template_id
        # The skill template name.
        self.skill_template_name = skill_template_name
        # The skill templatetype. Valid values: 0: system template. 1: user template.
        self.skill_template_type = skill_template_type
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

        if self.id is not None:
            result['Id'] = self.id

        if self.modified is not None:
            result['Modified'] = self.modified

        if self.skill_counts is not None:
            result['SkillCounts'] = self.skill_counts

        if self.skill_template_desc is not None:
            result['SkillTemplateDesc'] = self.skill_template_desc

        if self.skill_template_id is not None:
            result['SkillTemplateId'] = self.skill_template_id

        if self.skill_template_name is not None:
            result['SkillTemplateName'] = self.skill_template_name

        if self.skill_template_type is not None:
            result['SkillTemplateType'] = self.skill_template_type

        if self.src_application_id is not None:
            result['SrcApplicationId'] = self.src_application_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Modified') is not None:
            self.modified = m.get('Modified')

        if m.get('SkillCounts') is not None:
            self.skill_counts = m.get('SkillCounts')

        if m.get('SkillTemplateDesc') is not None:
            self.skill_template_desc = m.get('SkillTemplateDesc')

        if m.get('SkillTemplateId') is not None:
            self.skill_template_id = m.get('SkillTemplateId')

        if m.get('SkillTemplateName') is not None:
            self.skill_template_name = m.get('SkillTemplateName')

        if m.get('SkillTemplateType') is not None:
            self.skill_template_type = m.get('SkillTemplateType')

        if m.get('SrcApplicationId') is not None:
            self.src_application_id = m.get('SrcApplicationId')

        return self

