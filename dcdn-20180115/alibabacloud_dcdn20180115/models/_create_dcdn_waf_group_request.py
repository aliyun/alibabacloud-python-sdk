# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDcdnWafGroupRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        subscribe: str = None,
        template_id: int = None,
    ):
        # The name of the WAF rule group. The name can be up to 128 characters in length. This parameter is required when you create a custom WAF rule group.
        self.name = name
        # Specifies whether to enable subscription. Valid values:
        # 
        # *   **on**
        # *   **off**
        # 
        # When you replicate a custom rule group, do not specify this parameter.
        self.subscribe = subscribe
        # The ID of the rule group to be replicated. This parameter is required when you replicate a custom WAF rule group. You can call the [DescribeDcdnWafGroups](~~DescribeDcdnWafGroups~~) operation to query the ID of the rule group. If no template is used, set the value to 0 or do not specify this parameter.
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

        if self.subscribe is not None:
            result['Subscribe'] = self.subscribe

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Subscribe') is not None:
            self.subscribe = m.get('Subscribe')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

