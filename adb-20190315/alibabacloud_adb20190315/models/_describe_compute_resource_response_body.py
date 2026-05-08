# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeComputeResourceResponseBody(DaraModel):
    def __init__(
        self,
        compute_resource: List[main_models.DescribeComputeResourceResponseBodyComputeResource] = None,
        request_id: str = None,
    ):
        # The queried specifications of computing resources.
        self.compute_resource = compute_resource
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compute_resource:
            for v1 in self.compute_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComputeResource'] = []
        if self.compute_resource is not None:
            for k1 in self.compute_resource:
                result['ComputeResource'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_resource = []
        if m.get('ComputeResource') is not None:
            for k1 in m.get('ComputeResource'):
                temp_model = main_models.DescribeComputeResourceResponseBodyComputeResource()
                self.compute_resource.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeComputeResourceResponseBodyComputeResource(DaraModel):
    def __init__(
        self,
        display_value: str = None,
        real_value: str = None,
    ):
        # The specifications of computing resources displayed in the console.
        self.display_value = display_value
        # The actual specifications of computing resources.
        self.real_value = real_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_value is not None:
            result['DisplayValue'] = self.display_value

        if self.real_value is not None:
            result['RealValue'] = self.real_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayValue') is not None:
            self.display_value = m.get('DisplayValue')

        if m.get('RealValue') is not None:
            self.real_value = m.get('RealValue')

        return self

