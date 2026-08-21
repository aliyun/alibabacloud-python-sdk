# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAITemplateRequest(DaraModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        # The AI template ID. You can obtain the ID by using one of the following methods:
        # - When you call the [AddAITemplate](https://help.aliyun.com/document_detail/102930.html) operation to add an AI template, the AI template ID is the value of the TemplateId parameter in the response.
        # - After the AI template is added, you can call the [ListAITemplate](https://help.aliyun.com/document_detail/102936.html) operation to query the AI template ID, which is the value of the TemplateId parameter in the response.
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
        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

