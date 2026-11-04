# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecordPlanRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        template_id: str = None,
    ):
        # The name of the recording plan.
        # 
        # The name must be less than 48 characters in length and can contain letters, digits, and the following special characters: hyphens (-), underscores (_), at signs (@), periods (.), and colons (:).
        # 
        # This parameter is required.
        self.name = name
        # The ID of the recording plan. You can call [QueryRecordPlans](https://help.aliyun.com/document_detail/107896.html) to query the ID.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The ID of the time template to be associated with the recording plan. You can call [QueryTimeTemplate](https://help.aliyun.com/document_detail/107890.html) to query the ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

