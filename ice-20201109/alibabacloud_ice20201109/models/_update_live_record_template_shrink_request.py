# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveRecordTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        record_format_shrink: str = None,
        template_id: str = None,
    ):
        # The template name.
        # 
        # This parameter is required.
        self.name = name
        # The list of recording formats.
        # 
        # This parameter is required.
        self.record_format_shrink = record_format_shrink
        # The template ID.
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

        if self.record_format_shrink is not None:
            result['RecordFormat'] = self.record_format_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecordFormat') is not None:
            self.record_format_shrink = m.get('RecordFormat')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

