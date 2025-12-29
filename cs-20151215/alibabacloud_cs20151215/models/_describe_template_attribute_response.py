# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeTemplateAttributeResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribeTemplateAttributeResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribeTemplateAttributeResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribeTemplateAttributeResponseBody(DaraModel):
    def __init__(
        self,
        id: str = None,
        acl: str = None,
        name: str = None,
        template: str = None,
        template_type: str = None,
        description: str = None,
        tags: str = None,
        template_with_hist_id: str = None,
        created: str = None,
        updated: str = None,
    ):
        # The ID of the template. When you update a template, a new template ID is generated.
        self.id = id
        # The access control policy of the template.
        self.acl = acl
        # The name of the template.
        self.name = name
        # The template content in the YAML format.
        self.template = template
        # The type of template. The value can be a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If the parameter is set to `compose`, the template is displayed on the Container Service - Swarm page in the console. Container Service for Swarm is deprecated.
        # *   If the value of the parameter is not `kubernetes`, the template is not displayed on the Templates page in the console. We recommend that you set the parameter to `kubernetes`.
        # 
        # Default value: `kubernetes`.
        self.template_type = template_type
        # The description of the template.
        self.description = description
        # The label of the template.
        self.tags = tags
        # The unique ID of the template. The value remains unchanged after the template is updated.
        self.template_with_hist_id = template_with_hist_id
        # The time when the template was created.
        self.created = created
        # The time when the template was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.acl is not None:
            result['acl'] = self.acl

        if self.name is not None:
            result['name'] = self.name

        if self.template is not None:
            result['template'] = self.template

        if self.template_type is not None:
            result['template_type'] = self.template_type

        if self.description is not None:
            result['description'] = self.description

        if self.tags is not None:
            result['tags'] = self.tags

        if self.template_with_hist_id is not None:
            result['template_with_hist_id'] = self.template_with_hist_id

        if self.created is not None:
            result['created'] = self.created

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('template') is not None:
            self.template = m.get('template')

        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('template_with_hist_id') is not None:
            self.template_with_hist_id = m.get('template_with_hist_id')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

