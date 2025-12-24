# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomTemplateRequest(DaraModel):
    def __init__(
        self,
        custom_template: str = None,
        owner_id: int = None,
        region_id: str = None,
        template: str = None,
    ):
        # The configuration of the template. The value is in the following JSON format: {height:xxx,scale:xxx,gop:xxx,bframes:xxx,cdesc:xxx}. All fields are required. If any field is left empty, the call fails.
        # 
        # >  For more information, see **Fields of the CustomTemplate parameter**.
        # 
        # This parameter is required.
        self.custom_template = custom_template
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the template.
        # 
        # > Record the template name. The template name is required if you want to use, query, or delete the template.
        # 
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_template is not None:
            result['CustomTemplate'] = self.custom_template

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTemplate') is not None:
            self.custom_template = m.get('CustomTemplate')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

