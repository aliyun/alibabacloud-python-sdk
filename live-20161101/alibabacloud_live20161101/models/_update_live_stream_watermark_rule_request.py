# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveStreamWatermarkRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        owner_id: int = None,
        region_id: str = None,
        rule_id: str = None,
        template_id: str = None,
    ):
        # The description of the custom rule.
        self.description = description
        # The name of the custom rule.
        self.name = name
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the watermark rule.
        # 
        # >  You can obtain the rule ID by checking the value of the RuleId parameter that is returned by the [AddLiveStreamWatermarkRule](https://help.aliyun.com/document_detail/2848100.html) operation.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The ID of the watermark template.
        # 
        # >  You can obtain the template ID by checking the value of the TemplateId parameter that is returned by the [AddLiveStreamWatermark](https://help.aliyun.com/document_detail/2848096.html) operation.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

