# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateTemplateContentRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        template_url: str = None,
    ):
        # The content of the template.
        self.content = content
        # The ID of the region.
        self.region_id = region_id
        # The URL that is used to store the content of the Operation Orchestration Service (OOS) template in the Alibaba Cloud Object Storage Service (OSS). Only the public-read URL is supported. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url

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

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        return self

