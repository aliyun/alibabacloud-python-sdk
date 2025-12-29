# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The name of the template. The name can be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The version of the template. The default value is the latest version of the template.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

