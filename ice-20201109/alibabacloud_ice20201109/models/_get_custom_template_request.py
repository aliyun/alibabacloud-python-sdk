# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCustomTemplateRequest(DaraModel):
    def __init__(
        self,
        subtype: int = None,
        template_id: str = None,
        type: int = None,
    ):
        # The template subtype.
        self.subtype = subtype
        # The template ID.
        self.template_id = template_id
        # The ID of the template type that is used to query the default template. This parameter is required if TemplateId is not specified.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subtype is not None:
            result['Subtype'] = self.subtype

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

