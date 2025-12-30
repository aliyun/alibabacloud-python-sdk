# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateCustomTemplateResponseBody(DaraModel):
    def __init__(
        self,
        custom_template: main_models.CreateCustomTemplateResponseBodyCustomTemplate = None,
        request_id: str = None,
    ):
        # The template information.
        self.custom_template = custom_template
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.custom_template:
            self.custom_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_template is not None:
            result['CustomTemplate'] = self.custom_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTemplate') is not None:
            temp_model = main_models.CreateCustomTemplateResponseBodyCustomTemplate()
            self.custom_template = temp_model.from_map(m.get('CustomTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCustomTemplateResponseBodyCustomTemplate(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        is_default: bool = None,
        modified_time: str = None,
        status: str = None,
        subtype: str = None,
        template_config: str = None,
        template_id: str = None,
        template_name: str = None,
        type: int = None,
        type_name: str = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        # Indicates whether the template is the default template.
        self.is_default = is_default
        # The time when the template was last modified.
        self.modified_time = modified_time
        # The template state.
        self.status = status
        # The subtype name of the template.
        self.subtype = subtype
        # The template configurations.
        self.template_config = template_config
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The type ID of the template.
        self.type = type
        # The type name of the template.
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.status is not None:
            result['Status'] = self.status

        if self.subtype is not None:
            result['Subtype'] = self.subtype

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.type is not None:
            result['Type'] = self.type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

