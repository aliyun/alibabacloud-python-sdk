# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class GetGlobalAcceleratorResourcesResponseBody(DaraModel):
    def __init__(
        self,
        associated_resources: List[main_models.GetGlobalAcceleratorResourcesResponseBodyAssociatedResources] = None,
        request_id: str = None,
    ):
        self.associated_resources = associated_resources
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.associated_resources:
            for v1 in self.associated_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedResources'] = []
        if self.associated_resources is not None:
            for k1 in self.associated_resources:
                result['AssociatedResources'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_resources = []
        if m.get('AssociatedResources') is not None:
            for k1 in m.get('AssociatedResources'):
                temp_model = main_models.GetGlobalAcceleratorResourcesResponseBodyAssociatedResources()
                self.associated_resources.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGlobalAcceleratorResourcesResponseBodyAssociatedResources(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        associated_mode: str = None,
        associated_resource_id: str = None,
        associated_resource_region_id: str = None,
        associated_resource_type: str = None,
        state: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.associated_mode = associated_mode
        self.associated_resource_id = associated_resource_id
        self.associated_resource_region_id = associated_resource_region_id
        self.associated_resource_type = associated_resource_type
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.associated_mode is not None:
            result['AssociatedMode'] = self.associated_mode

        if self.associated_resource_id is not None:
            result['AssociatedResourceId'] = self.associated_resource_id

        if self.associated_resource_region_id is not None:
            result['AssociatedResourceRegionId'] = self.associated_resource_region_id

        if self.associated_resource_type is not None:
            result['AssociatedResourceType'] = self.associated_resource_type

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AssociatedMode') is not None:
            self.associated_mode = m.get('AssociatedMode')

        if m.get('AssociatedResourceId') is not None:
            self.associated_resource_id = m.get('AssociatedResourceId')

        if m.get('AssociatedResourceRegionId') is not None:
            self.associated_resource_region_id = m.get('AssociatedResourceRegionId')

        if m.get('AssociatedResourceType') is not None:
            self.associated_resource_type = m.get('AssociatedResourceType')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

