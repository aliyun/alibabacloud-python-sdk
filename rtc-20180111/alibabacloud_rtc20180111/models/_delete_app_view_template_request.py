# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DeleteAppViewTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        template: main_models.DeleteAppViewTemplateRequestTemplate = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.template is not None:
            result['Template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Template') is not None:
            temp_model = main_models.DeleteAppViewTemplateRequestTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class DeleteAppViewTemplateRequestTemplate(DaraModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

