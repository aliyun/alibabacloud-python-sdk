# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetStackResourceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        drift_detection_time: str = None,
        logical_resource_id: str = None,
        metadata: Dict[str, Any] = None,
        module_info: main_models.GetStackResourceResponseBodyModuleInfo = None,
        physical_resource_id: str = None,
        request_id: str = None,
        resource_attributes: List[Dict[str, Any]] = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
    ):
        # The resource type.
        self.create_time = create_time
        # The reason why the resource is in its current state.
        self.description = description
        # The ID of the stack.
        self.drift_detection_time = drift_detection_time
        # The time when the resource was updated.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.logical_resource_id = logical_resource_id
        # The list of the resource properties.
        self.metadata = metadata
        # The information about the modules from which the resource is created. This parameter is returned only if the resource is created from modules.
        self.module_info = module_info
        # The metadata.
        self.physical_resource_id = physical_resource_id
        # The physical ID of the resource.
        self.request_id = request_id
        # The status of the resource in the last successful drift detection. Valid values:
        # 
        # *   DELETED: The actual configuration of the resource differs from its expected template configuration because the resource is deleted.
        # *   MODIFIED: The actual configuration of the resource differs from its expected template configuration.
        # *   NOT_CHECKED: ROS has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The actual configuration of the resource matches its expected template configuration.
        self.resource_attributes = resource_attributes
        # The time when the last successful drift detection was performed on the stack.
        self.resource_drift_status = resource_drift_status
        # The logical ID of the resource defined in the template.
        self.resource_type = resource_type
        # The ID of the stack.
        self.stack_id = stack_id
        # The name of the stack.
        self.stack_name = stack_name
        # The ID of the request.
        self.status = status
        # The time when the resource was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.status_reason = status_reason
        # The name of the stack.
        # 
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). The name must start with a digit or letter.
        self.update_time = update_time

    def validate(self):
        if self.module_info:
            self.module_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.module_info is not None:
            result['ModuleInfo'] = self.module_info.to_map()

        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_attributes is not None:
            result['ResourceAttributes'] = self.resource_attributes

        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('ModuleInfo') is not None:
            temp_model = main_models.GetStackResourceResponseBodyModuleInfo()
            self.module_info = temp_model.from_map(m.get('ModuleInfo'))

        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceAttributes') is not None:
            self.resource_attributes = m.get('ResourceAttributes')

        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetStackResourceResponseBodyModuleInfo(DaraModel):
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

