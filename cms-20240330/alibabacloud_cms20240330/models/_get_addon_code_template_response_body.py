# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetAddonCodeTemplateResponseBody(DaraModel):
    def __init__(
        self,
        codes: List[main_models.GetAddonCodeTemplateResponseBodyCodes] = None,
        request_id: str = None,
    ):
        self.codes = codes
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.codes:
            for v1 in self.codes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['codes'] = []
        if self.codes is not None:
            for k1 in self.codes:
                result['codes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.codes = []
        if m.get('codes') is not None:
            for k1 in m.get('codes'):
                temp_model = main_models.GetAddonCodeTemplateResponseBodyCodes()
                self.codes.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAddonCodeTemplateResponseBodyCodes(DaraModel):
    def __init__(
        self,
        code_template: str = None,
        name: str = None,
    ):
        self.code_template = code_template
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_template is not None:
            result['codeTemplate'] = self.code_template

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeTemplate') is not None:
            self.code_template = m.get('codeTemplate')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

