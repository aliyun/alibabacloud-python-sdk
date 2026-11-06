# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawSkillTemplateRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        region_id: str = None,
        skill_template_id: str = None,
    ):
        # The application ID. This parameter is required when you call this operation. If this parameter is not specified, InvalidApplicationId.Malformed is returned.
        self.application_id = application_id
        # The application type.
        # 
        # > If you are calling this operation for the first time, you do not need to specify this parameter.
        self.application_type = application_type
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        self.region_id = region_id
        # The skill template ID.
        # 
        # This parameter is required.
        self.skill_template_id = skill_template_id

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

        if self.skill_template_id is not None:
            result['SkillTemplateId'] = self.skill_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkillTemplateId') is not None:
            self.skill_template_id = m.get('SkillTemplateId')

        return self

