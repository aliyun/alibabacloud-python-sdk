# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAITemplateRequest(DaraModel):
    def __init__(
        self,
        template_config: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The detailed configurations of the AI template. The value is a JSON string. For more information, see [AITemplateConfig](~~89863#title-vd3-499-o36~~).
        # 
        # This parameter is required.
        self.template_config = template_config
        # The ID of the AI template. You can use one of the following methods to obtain the ID:
        # 
        # *   Call the [AddAITemplate](https://help.aliyun.com/document_detail/102930.html) operation to add an AI template if no AI template exists. The value of TemplateId in the response is the ID of the AI template.
        # *   Call the [ListAITemplate](https://help.aliyun.com/document_detail/102936.html) operation if the template already exists. The value of TemplateId in the response is the ID of the AI template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The name of the AI template. The name can be up to 128 bytes in length.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

