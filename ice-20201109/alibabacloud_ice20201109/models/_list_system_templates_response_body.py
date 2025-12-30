# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListSystemTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        system_template_list: List[main_models.ListSystemTemplatesResponseBodySystemTemplateList] = None,
        total: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried templates.
        self.system_template_list = system_template_list
        # The total number of templates.
        self.total = total

    def validate(self):
        if self.system_template_list:
            for v1 in self.system_template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SystemTemplateList'] = []
        if self.system_template_list is not None:
            for k1 in self.system_template_list:
                result['SystemTemplateList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.system_template_list = []
        if m.get('SystemTemplateList') is not None:
            for k1 in m.get('SystemTemplateList'):
                temp_model = main_models.ListSystemTemplatesResponseBodySystemTemplateList()
                self.system_template_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSystemTemplatesResponseBodySystemTemplateList(DaraModel):
    def __init__(
        self,
        status: str = None,
        subtype: int = None,
        subtype_name: str = None,
        template_config: str = None,
        template_id: str = None,
        template_name: str = None,
        type: int = None,
        type_name: str = None,
    ):
        # The template state.
        self.status = status
        # The subtype ID of the template.
        self.subtype = subtype
        # The subtype name of the template.
        self.subtype_name = subtype_name
        # The template parameters.
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
        if self.status is not None:
            result['Status'] = self.status

        if self.subtype is not None:
            result['Subtype'] = self.subtype

        if self.subtype_name is not None:
            result['SubtypeName'] = self.subtype_name

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
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')

        if m.get('SubtypeName') is not None:
            self.subtype_name = m.get('SubtypeName')

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

