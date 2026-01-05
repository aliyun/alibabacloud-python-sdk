# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class GetInstancePropertiesResponseBody(DaraModel):
    def __init__(
        self,
        property_template_model: main_models.GetInstancePropertiesResponseBodyPropertyTemplateModel = None,
        request_id: str = None,
    ):
        self.property_template_model = property_template_model
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.property_template_model:
            self.property_template_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_template_model is not None:
            result['PropertyTemplateModel'] = self.property_template_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyTemplateModel') is not None:
            temp_model = main_models.GetInstancePropertiesResponseBodyPropertyTemplateModel()
            self.property_template_model = temp_model.from_map(m.get('PropertyTemplateModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstancePropertiesResponseBodyPropertyTemplateModel(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        return self

