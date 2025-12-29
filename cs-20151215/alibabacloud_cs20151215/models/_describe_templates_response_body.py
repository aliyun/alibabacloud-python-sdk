# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeTemplatesResponseBodyPageInfo = None,
        templates: List[main_models.DescribeTemplatesResponseBodyTemplates] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The list of returned templates.
        self.templates = templates

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()

        result['templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_info') is not None:
            temp_model = main_models.DescribeTemplatesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        self.templates = []
        if m.get('templates') is not None:
            for k1 in m.get('templates'):
                temp_model = main_models.DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class DescribeTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        acl: str = None,
        created: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        tags: str = None,
        template: str = None,
        template_type: str = None,
        template_with_hist_id: str = None,
        updated: str = None,
    ):
        # The access control policy of the template. Valid values:
        # 
        # *   `private`: The template is private.
        # *   `public`: The template is public.
        # *   `shared`: The template can be shared.
        # 
        # Default value: `private`.
        self.acl = acl
        # The time when the template was created.
        self.created = created
        # The description of the template.
        self.description = description
        # The ID of the template.
        self.id = id
        # The name of the template.
        self.name = name
        # The label of the template. By default, the value is the name of the template.
        self.tags = tags
        # The template content in the YAML format.
        self.template = template
        # The type of template. This parameter can be set to a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If the parameter is set to `compose`, the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated.
        self.template_type = template_type
        # The ID of the parent template. The value of `template_with_hist_id` is the same for each template version. This allows you to manage different template versions.
        self.template_with_hist_id = template_with_hist_id
        # The time when the template was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.created is not None:
            result['created'] = self.created

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.tags is not None:
            result['tags'] = self.tags

        if self.template is not None:
            result['template'] = self.template

        if self.template_type is not None:
            result['template_type'] = self.template_type

        if self.template_with_hist_id is not None:
            result['template_with_hist_id'] = self.template_with_hist_id

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('template') is not None:
            self.template = m.get('template')

        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')

        if m.get('template_with_hist_id') is not None:
            self.template_with_hist_id = m.get('template_with_hist_id')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class DescribeTemplatesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

