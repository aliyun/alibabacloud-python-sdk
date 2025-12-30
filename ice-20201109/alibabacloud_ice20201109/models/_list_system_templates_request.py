# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSystemTemplatesRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        subtype: str = None,
        template_id: str = None,
        type: str = None,
    ):
        # The template name.
        self.name = name
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 20 Valid values: 1 to 100.
        self.page_size = page_size
        # The template state. Valid values: Normal, Invisible, and All.
        self.status = status
        # The subtype ID of the template.
        self.subtype = subtype
        # The template ID.
        self.template_id = template_id
        # The template type. Separate multiple types with commas (,).
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.subtype is not None:
            result['Subtype'] = self.subtype

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

