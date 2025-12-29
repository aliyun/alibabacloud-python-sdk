# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateTemplateRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        version_name: str = None,
    ):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        # 
        # This parameter is required.
        self.content = content
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tag keys and tag values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The name of the template. The name can be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The name of the version of the template.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

