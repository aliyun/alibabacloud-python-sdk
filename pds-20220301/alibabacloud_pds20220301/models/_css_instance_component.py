# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CssInstanceComponent(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        component_name: str = None,
        global_key: str = None,
        instance_property: List[main_models.CssInstanceProperty] = None,
        module_attr_status: int = None,
        tag: str = None,
    ):
        self.component_code = component_code
        self.component_name = component_name
        self.global_key = global_key
        self.instance_property = instance_property
        self.module_attr_status = module_attr_status
        self.tag = tag

    def validate(self):
        if self.instance_property:
            for v1 in self.instance_property:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['componentCode'] = self.component_code

        if self.component_name is not None:
            result['componentName'] = self.component_name

        if self.global_key is not None:
            result['globalKey'] = self.global_key

        result['instanceProperty'] = []
        if self.instance_property is not None:
            for k1 in self.instance_property:
                result['instanceProperty'].append(k1.to_map() if k1 else None)

        if self.module_attr_status is not None:
            result['moduleAttrStatus'] = self.module_attr_status

        if self.tag is not None:
            result['tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentCode') is not None:
            self.component_code = m.get('componentCode')

        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')

        if m.get('globalKey') is not None:
            self.global_key = m.get('globalKey')

        self.instance_property = []
        if m.get('instanceProperty') is not None:
            for k1 in m.get('instanceProperty'):
                temp_model = main_models.CssInstanceProperty()
                self.instance_property.append(temp_model.from_map(k1))

        if m.get('moduleAttrStatus') is not None:
            self.module_attr_status = m.get('moduleAttrStatus')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        return self

