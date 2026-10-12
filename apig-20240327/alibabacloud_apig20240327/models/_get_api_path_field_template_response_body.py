# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetApiPathFieldTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetApiPathFieldTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetApiPathFieldTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetApiPathFieldTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        field_paths: Dict[str, List[main_models.DataFieldPathsValue]] = None,
        path: str = None,
        protocol: str = None,
        template_name: str = None,
    ):
        # The description text of the field template.
        self.description = description
        # The set of fields defined by the field template, grouped by mapping key. Each group contains a set of template field items.
        self.field_paths = field_paths
        # The API request path corresponding to the field template.
        self.path = path
        # The API protocol applicable to the field template, such as openai.
        self.protocol = protocol
        # The name of the field template.
        self.template_name = template_name

    def validate(self):
        if self.field_paths:
            for v1 in self.field_paths.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        result['fieldPaths'] = {}
        if self.field_paths is not None:
            for k1, v1 in self.field_paths.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['fieldPaths'][k1] = l1

        if self.path is not None:
            result['path'] = self.path

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.template_name is not None:
            result['templateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        self.field_paths = {}
        if m.get('fieldPaths') is not None:
            for k1, v1 in m.get('fieldPaths').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataFieldPathsValue()
                    l1.append(temp_model.from_map(k2))
                self.field_paths[k1] = l1

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        return self

