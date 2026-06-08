# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStackResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[main_models.ListStackResourcesResponseBodyResources] = None,
    ):
        # Details about resources.
        self.request_id = request_id
        # The resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListStackResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class ListStackResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        drift_detection_time: str = None,
        logical_resource_id: str = None,
        module_info: main_models.ListStackResourcesResponseBodyResourcesModuleInfo = None,
        physical_resource_id: str = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
    ):
        # The time when the resource was created. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The time when the most recent successful drift detection was performed on the stack.
        self.drift_detection_time = drift_detection_time
        # The logical ID of the resource. The logical ID is the resource name that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The information about the modules from which the resource is created. This parameter is returned only if the resource is created from modules.
        self.module_info = module_info
        # The physical ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The drift state of the resource in the most recent successful drift detection. Valid values:
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
        # The stack name.\\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or letter.
        self.stack_name = stack_name
        # The state of the resource. Valid values:
        # 
        # *   INIT_COMPLETE: The resource is pending to be created.
        # *   CREATE_COMPLETE: The resource is created.
        # *   CREATE_FAILED: The resource failed to be created.
        # *   CREATE_IN_PROGRESS: The resource is being created.
        # *   UPDATE_IN_PROGRESS: The resource is being updated.
        # *   UPDATE_FAILED: The resource failed to be updated.
        # *   UPDATE_COMPLETE: The resource is updated.
        # *   DELETE_IN_PROGRESS: The resource is being deleted.
        # *   DELETE_FAILED: The resource failed to be deleted.
        # *   DELETE_COMPLETE: The resource is deleted.
        # *   CHECK_IN_PROGRESS: The resource is being validated.
        # *   CHECK_FAILED: The resource failed to be validated.
        # *   CHECK_COMPLETE: The resource is validated.
        # *   IMPORT_IN_PROGRESS: The resource is being imported.
        # *   IMPORT_FAILED: The resource failed to be imported.
        # *   IMPORT_COMPLETE: The resource is imported.
        self.status = status
        # The reason why the resource is in its current state.
        self.status_reason = status_reason
        # The time when the resource was updated. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
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

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.module_info is not None:
            result['ModuleInfo'] = self.module_info.to_map()

        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id

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

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('ModuleInfo') is not None:
            temp_model = main_models.ListStackResourcesResponseBodyResourcesModuleInfo()
            self.module_info = temp_model.from_map(m.get('ModuleInfo'))

        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')

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

class ListStackResourcesResponseBodyResourcesModuleInfo(DaraModel):
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

