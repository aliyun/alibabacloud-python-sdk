# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class BatchBindTemplateResponseBody(DaraModel):
    def __init__(
        self,
        bindings: List[main_models.BatchBindTemplateResponseBodyBindings] = None,
        request_id: str = None,
    ):
        self.bindings = bindings
        self.request_id = request_id

    def validate(self):
        if self.bindings:
            for v1 in self.bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bindings'] = []
        if self.bindings is not None:
            for k1 in self.bindings:
                result['Bindings'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k1 in m.get('Bindings'):
                temp_model = main_models.BatchBindTemplateResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchBindTemplateResponseBodyBindings(DaraModel):
    def __init__(
        self,
        error: str = None,
        instance_id: str = None,
        instance_type: str = None,
        template_id: str = None,
    ):
        self.error = error
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

