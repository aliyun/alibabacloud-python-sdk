# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class DetectStackResourceDriftResponseBody(DaraModel):
    def __init__(
        self,
        actual_properties: str = None,
        drift_detection_time: str = None,
        expected_properties: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        property_differences: List[main_models.DetectStackResourceDriftResponseBodyPropertyDifferences] = None,
        request_id: str = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
    ):
        # The actual JSON-formatted resource properties.
        self.actual_properties = actual_properties
        # The time when the resource drift detection was initiated.
        self.drift_detection_time = drift_detection_time
        # The JSON-formatted resource properties that are defined in the template.
        self.expected_properties = expected_properties
        # The logical ID of the resource that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The physical ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The property drifts of the resource.
        self.property_differences = property_differences
        # The ID of the request.
        self.request_id = request_id
        # The drift status of the resource. Valid values:
        # 
        # *   DELETED: The actual configuration of the resource differs from its expected template configuration because the resource is deleted.
        # *   MODIFIED: The actual configuration of the resource differs from its expected template configuration.
        # *   NOT_CHECKED: Resource Orchestration Service (ROS) has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The actual configuration of the resource matches its expected template configuration.
        self.resource_drift_status = resource_drift_status
        # The type of the resource.
        self.resource_type = resource_type
        # The ID of the stack.
        self.stack_id = stack_id

    def validate(self):
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

        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id

        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k1 in self.property_differences:
                result['PropertyDifferences'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')

        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k1 in m.get('PropertyDifferences'):
                temp_model = main_models.DetectStackResourceDriftResponseBodyPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

class DetectStackResourceDriftResponseBodyPropertyDifferences(DaraModel):
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
        # *   ADD: The property value has been added to a resource property whose data type was Array or List.
        # *   REMOVE: The property has been deleted from the current resource configuration.
        # *   NOT_EQUAL: The current property value differs from the expected value defined in the stack template.
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

