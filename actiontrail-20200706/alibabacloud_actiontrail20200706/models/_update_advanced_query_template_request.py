# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAdvancedQueryTemplateRequest(DaraModel):
    def __init__(
        self,
        simple_query: bool = None,
        template_id: str = None,
        template_name: str = None,
        template_sql: str = None,
    ):
        # Specifies whether to enable the simple query mode.
        # 
        # This parameter is required.
        self.simple_query = simple_query
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The name of the template. The maximum length is 64 characters.
        self.template_name = template_name
        # The query statement of the template.
        self.template_sql = template_sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.simple_query is not None:
            result['SimpleQuery'] = self.simple_query

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_sql is not None:
            result['TemplateSql'] = self.template_sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimpleQuery') is not None:
            self.simple_query = m.get('SimpleQuery')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateSql') is not None:
            self.template_sql = m.get('TemplateSql')

        return self

