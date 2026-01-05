# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDataQualityScanRunRequest(DaraModel):
    def __init__(
        self,
        data_quality_scan_id: int = None,
        parameters: List[main_models.CreateDataQualityScanRunRequestParameters] = None,
        project_id: int = None,
        runtime_resource: main_models.CreateDataQualityScanRunRequestRuntimeResource = None,
    ):
        # The ID of the data quality monitor.
        self.data_quality_scan_id = data_quality_scan_id
        # The parameter settings used during the actual run. The `triggerTime` parameter is required.
        self.parameters = parameters
        # The project ID.
        self.project_id = project_id
        # The scheduling resource group used when running the data quality monitor. This resource group uses the same data structure as in the scheduling API.
        self.runtime_resource = runtime_resource

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_scan_id is not None:
            result['DataQualityScanId'] = self.data_quality_scan_id

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityScanId') is not None:
            self.data_quality_scan_id = m.get('DataQualityScanId')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateDataQualityScanRunRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.CreateDataQualityScanRunRequestRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        return self

class CreateDataQualityScanRunRequestRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: float = None,
        id: str = None,
        image: str = None,
    ):
        # The Compute Resources (CUs) reserved for running the data quality monitor in the resource group.
        self.cu = cu
        # The resource group ID.
        self.id = id
        # The image settings used when running the data quality monitor in the resource group.
        self.image = image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.id is not None:
            result['Id'] = self.id

        if self.image is not None:
            result['Image'] = self.image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        return self

class CreateDataQualityScanRunRequestParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value. You can use a scheduling time expression.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

