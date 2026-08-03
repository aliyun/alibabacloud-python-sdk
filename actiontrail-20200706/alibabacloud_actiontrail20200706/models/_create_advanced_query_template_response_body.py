# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAdvancedQueryTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        simple_query: str = None,
        template_id: str = None,
        template_name: str = None,
        template_sql: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the simple query mode is enabled.
        self.simple_query = simple_query
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The query statement.
        self.template_sql = template_sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SimpleQuery') is not None:
            self.simple_query = m.get('SimpleQuery')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateSql') is not None:
            self.template_sql = m.get('TemplateSql')

        return self

