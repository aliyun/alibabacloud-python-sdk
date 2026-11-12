# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolarClawSkillTemplateRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        region_id: str = None,
        skill_template_desc: str = None,
        skill_template_name: str = None,
        skill_template_param: str = None,
    ):
        # The application ID. This parameter is required. If this parameter is not provided, an InvalidApplicationId.Malformed (HTTP 400) error is returned.
        self.application_id = application_id
        # The application type.
        # 
        # > If you are calling this operation for the first time, you do not need to specify this parameter.
        self.application_type = application_type
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to view all available regions for the current account, including region IDs.
        self.region_id = region_id
        # The description of the skill template.
        self.skill_template_desc = skill_template_desc
        # The name of the skill template.
        # 
        # This parameter is required.
        self.skill_template_name = skill_template_name
        # The skill template parameters. Specify a standard JSON object string with the skill identifier as the key, such as {"skill1":{"skillName":"polarclawhub","version":"0.0.0"}}. JSON arrays or single-quote formats are not accepted.
        # 
        # This parameter is required.
        self.skill_template_param = skill_template_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skill_template_desc is not None:
            result['SkillTemplateDesc'] = self.skill_template_desc

        if self.skill_template_name is not None:
            result['SkillTemplateName'] = self.skill_template_name

        if self.skill_template_param is not None:
            result['SkillTemplateParam'] = self.skill_template_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkillTemplateDesc') is not None:
            self.skill_template_desc = m.get('SkillTemplateDesc')

        if m.get('SkillTemplateName') is not None:
            self.skill_template_name = m.get('SkillTemplateName')

        if m.get('SkillTemplateParam') is not None:
            self.skill_template_param = m.get('SkillTemplateParam')

        return self

