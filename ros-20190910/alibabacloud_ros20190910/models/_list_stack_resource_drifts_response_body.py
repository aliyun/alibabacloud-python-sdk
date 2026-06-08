# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStackResourceDriftsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_drifts: List[main_models.ListStackResourceDriftsResponseBodyResourceDrifts] = None,
    ):
        # The query token returned in this call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The resource drifts.
        self.resource_drifts = resource_drifts

    def validate(self):
        if self.resource_drifts:
            for v1 in self.resource_drifts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceDrifts'] = []
        if self.resource_drifts is not None:
            for k1 in self.resource_drifts:
                result['ResourceDrifts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_drifts = []
        if m.get('ResourceDrifts') is not None:
            for k1 in m.get('ResourceDrifts'):
                temp_model = main_models.ListStackResourceDriftsResponseBodyResourceDrifts()
                self.resource_drifts.append(temp_model.from_map(k1))

        return self

class ListStackResourceDriftsResponseBodyResourceDrifts(DaraModel):
    def __init__(
        self,
        actual_properties: str = None,
        drift_detection_time: str = None,
        expected_properties: str = None,
        logical_resource_id: str = None,
        module_info: main_models.ListStackResourceDriftsResponseBodyResourceDriftsModuleInfo = None,
        physical_resource_id: str = None,
        property_differences: List[main_models.ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences] = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
    ):
        # The actual JSON-formatted resource properties.
        self.actual_properties = actual_properties
        # The time when the drift detection operation was performed on the resource.
        self.drift_detection_time = drift_detection_time
        # The JSON-formatted resource properties that are defined in the template.
        self.expected_properties = expected_properties
        # The logical ID of the resource. The logical ID indicates the name of the resource that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The information about the modules from which the resource was created. This parameter is returned only if the resource is created from modules.
        self.module_info = module_info
        # The physical ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The property drifts of the resource.
        self.property_differences = property_differences
        # The drift state of the resource. Valid values:
        # 
        # *   DELETED: The actual configuration of the resource differs from its expected template configuration because the resource is deleted.
        # *   MODIFIED: The actual configuration of the resource differs from its expected template configuration.
        # *   NOT_CHECKED: Resource Orchestration Service (ROS) has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The actual configuration of the resource matches its expected template configuration.
        self.resource_drift_status = resource_drift_status
        # The resource type.
        self.resource_type = resource_type
        # The stack ID.
        self.stack_id = stack_id

    def validate(self):
        if self.module_info:
            self.module_info.validate()
        if self.property_differences:
            for v1 in self.property_differences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_properties is not None:
            result['ActualProperties'] = self.actual_properties

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.expected_properties is not None:
            result['ExpectedProperties'] = self.expected_properties

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.module_info is not None:
            result['ModuleInfo'] = self.module_info.to_map()

        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id

        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k1 in self.property_differences:
                result['PropertyDifferences'].append(k1.to_map() if k1 else None)

        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualProperties') is not None:
            self.actual_properties = m.get('ActualProperties')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('ExpectedProperties') is not None:
            self.expected_properties = m.get('ExpectedProperties')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('ModuleInfo') is not None:
            temp_model = main_models.ListStackResourceDriftsResponseBodyResourceDriftsModuleInfo()
            self.module_info = temp_model.from_map(m.get('ModuleInfo'))

        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')

        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k1 in m.get('PropertyDifferences'):
                temp_model = main_models.ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k1))

        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

class ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences(DaraModel):
    def __init__(
        self,
        actual_value: str = None,
        difference_type: str = None,
        expected_value: str = None,
        property_path: str = None,
    ):
        # The actual value of the resource property.
        self.actual_value = actual_value
        # The drift type of the resource property. Valid values:
        # 
        # *   ADD: The value is added to a resource property whose data type is Array or List.
        # *   REMOVE: The property is deleted from the current resource configuration.
        # *   NOT_EQUAL: The current property value differs from the expected value that is defined in the stack template.
        self.difference_type = difference_type
        # The expected value of the resource property that is defined in the template.
        self.expected_value = expected_value
        # The path of the resource property.
        self.property_path = property_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value

        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type

        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value

        if self.property_path is not None:
            result['PropertyPath'] = self.property_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')

        if m.get('DifferenceType') is not None:
            self.difference_type = m.get('DifferenceType')

        if m.get('ExpectedValue') is not None:
            self.expected_value = m.get('ExpectedValue')

        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')

        return self

class ListStackResourceDriftsResponseBodyResourceDriftsModuleInfo(DaraModel):
    def __init__(
        self,
        logical_id_hierarchy: str = None,
        type_hierarchy: str = None,
    ):
        # The concatenated logical IDs of one or more modules that contain the resource. The modules are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from Module B nested within Parent Module A:
        # 
        # `moduleA/moduleB`
        self.logical_id_hierarchy = logical_id_hierarchy
        # The concatenated types of one or more modules that contain the resource. The module types are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from a module of the `MODULE::ROS::Child::Example` type that is nested within a parent module of the `MODULE::ROS::Parent::Example` type:
        # 
        # `MODULE::ROS::Parent::Example/MODULE::ROS::Child::Example`
        self.type_hierarchy = type_hierarchy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_id_hierarchy is not None:
            result['LogicalIdHierarchy'] = self.logical_id_hierarchy

        if self.type_hierarchy is not None:
            result['TypeHierarchy'] = self.type_hierarchy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalIdHierarchy') is not None:
            self.logical_id_hierarchy = m.get('LogicalIdHierarchy')

        if m.get('TypeHierarchy') is not None:
            self.type_hierarchy = m.get('TypeHierarchy')

        return self

