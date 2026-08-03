# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAdvancedQueryTemplateRequest(DaraModel):
    def __init__(
        self,
        simple_query: bool = None,
        template_name: str = None,
        template_sql: str = None,
    ):
        # Specifies whether to enable the simple query mode.
        # 
        # This parameter is required.
        self.simple_query = simple_query
        # The name of the template, which can contain a maximum of 64 characters. Uniqueness is not required.
        self.template_name = template_name
        # The query statement of the template.
        # 
        # This parameter is required.
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

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_sql is not None:
            result['TemplateSql'] = self.template_sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimpleQuery') is not None:
            self.simple_query = m.get('SimpleQuery')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateSql') is not None:
            self.template_sql = m.get('TemplateSql')

        return self

