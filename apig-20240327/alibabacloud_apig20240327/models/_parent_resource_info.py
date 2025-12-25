# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ParentResourceInfo(DaraModel):
    def __init__(
        self,
        api_info: main_models.HttpApiApiInfo = None,
        resource_type: str = None,
    ):
        self.api_info = api_info
        self.resource_type = resource_type

    def validate(self):
        if self.api_info:
            self.api_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_info is not None:
            result['apiInfo'] = self.api_info.to_map()

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiInfo') is not None:
            temp_model = main_models.HttpApiApiInfo()
            self.api_info = temp_model.from_map(m.get('apiInfo'))

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

