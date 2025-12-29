# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class GetExecutionTemplateResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
        template: main_models.GetExecutionTemplateResponseBodyTemplate = None,
    ):
        # The content of the template.
        self.content = content
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the template.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template is not None:
            result['Template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Template') is not None:
            temp_model = main_models.GetExecutionTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class GetExecutionTemplateResponseBodyTemplate(DaraModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The creator of the template.
        self.created_by = created_by
        # The time when the template was created.
        self.created_date = created_date
        # The description of the template.
        self.description = description
        # The SHA-256 value of the template content.
        self.hash = hash
        # The share type of the template. The share type of a user-created template is **Private**.
        self.share_type = share_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version
        # The user who last updated the template.
        self.updated_by = updated_by
        # The time when the template was last updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.description is not None:
            result['Description'] = self.description

        if self.hash is not None:
            result['Hash'] = self.hash

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Hash') is not None:
            self.hash = m.get('Hash')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        return self

