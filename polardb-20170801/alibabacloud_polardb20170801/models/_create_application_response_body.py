# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        components: List[main_models.CreateApplicationResponseBodyComponents] = None,
        description: str = None,
        order_id: str = None,
        request_id: str = None,
        resource_available: bool = None,
        resource_group_id: str = None,
    ):
        self.application_id = application_id
        self.components = components
        self.description = description
        self.order_id = order_id
        self.request_id = request_id
        self.resource_available = resource_available
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_available is not None:
            result['ResourceAvailable'] = self.resource_available

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.CreateApplicationResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceAvailable') is not None:
            self.resource_available = m.get('ResourceAvailable')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class CreateApplicationResponseBodyComponents(DaraModel):
    def __init__(
        self,
        component_id: str = None,
    ):
        self.component_id = component_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        return self

