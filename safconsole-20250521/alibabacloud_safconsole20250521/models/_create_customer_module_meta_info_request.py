# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomerModuleMetaInfoRequest(DaraModel):
    def __init__(
        self,
        customer_module_id: int = None,
        feature_string: str = None,
        feature_template: str = None,
    ):
        # Customer model ID.
        self.customer_module_id = customer_module_id
        # A string representation of List<Object>, where Object has the following structure:
        # {
        # "mappingName": "xxx"
        # }
        self.feature_string = feature_string
        # Version of the feature adopted.
        self.feature_template = feature_template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_module_id is not None:
            result['CustomerModuleId'] = self.customer_module_id

        if self.feature_string is not None:
            result['FeatureString'] = self.feature_string

        if self.feature_template is not None:
            result['FeatureTemplate'] = self.feature_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerModuleId') is not None:
            self.customer_module_id = m.get('CustomerModuleId')

        if m.get('FeatureString') is not None:
            self.feature_string = m.get('FeatureString')

        if m.get('FeatureTemplate') is not None:
            self.feature_template = m.get('FeatureTemplate')

        return self

