# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateRequest(DaraModel):
    def __init__(
        self,
        related_mediaid_flag: str = None,
        template_id: str = None,
    ):
        # Specifies whether to return the information about the associated materials. Default value: 0. Valid values: 0 and 1. A value of 1 specifies that the information about the associated materials is returned. This parameter is valid only for regular templates.
        self.related_mediaid_flag = related_mediaid_flag
        # The template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.related_mediaid_flag is not None:
            result['RelatedMediaidFlag'] = self.related_mediaid_flag

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelatedMediaidFlag') is not None:
            self.related_mediaid_flag = m.get('RelatedMediaidFlag')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

