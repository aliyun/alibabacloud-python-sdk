# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuthCodeRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        biz_region_id: str = None,
        resource_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The ID of the application to connect to. When specifying this parameter, you must also provide the matching AppVersionId. If omitted, the application configured in the creation or validation environment is used.
        self.app_id = app_id
        # The ID of the application version to connect to. This parameter is used together with AppId. This parameter is not the image version ID.
        self.app_version_id = app_version_id
        # The region compatibility parameter. The destination region of the current connection resource is determined by the execution region of the task. You cannot use this parameter to switch the task region. Omit this parameter.
        self.biz_region_id = biz_region_id
        # The type of the resource to connect to. Valid values:
        # 
        # - **BUILDER**: connect to the creation environment
        # - **VALIDATE**: connect to the validation environment
        # 
        # The corresponding environment must be created and in a connectable state.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The ID of the existing creation or validation task. Create the task and confirm that the corresponding resources are available before calling this operation.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The actual task type. It must match the creation or validation task corresponding to the TaskId. Use the TaskType returned by GetTask. The task must also have connectable creation or validation resources. You cannot obtain an authorization code for distribution or snapshot tasks that do not have connection resources. Valid values:
        # 
        # - **AUTO_CREATE_IMAGE_VHD**: automatically create a VHD image
        # - **RETRY_CREATE_IMAGE_VHD**: retry VHD image creation
        # - **AUTO_CREATE_VHD**: automatically create a VHD
        # - **RETRY_VHD**: retry VHD creation
        # - **AUTO_VALIDATE_VHD**: automatically validate a VHD
        # - **RETRY_VALIDATE_VHD**: retry VHD validation
        # - **APPLY_VHD_BUILDER**: apply for a VHD application recording environment
        # - **ADAPT_AUTO**: automatically create application adaptation
        # - **ADAPT_AUTO_RETRY**: retry automatic application adaptation creation
        # - **ADAPT_MANUAL**: manually create application adaptation
        # - **ADAPT_MANUAL_RETRY**: retry manual application adaptation creation
        # - **DESKTOP_CUSTOM_IMAGE**: create a custom image for cloud desktop
        # - **DESKTOP_CUSTOM_IMAGE_RETRY**: retry custom image creation for cloud desktop
        # - **IMAGE_MANUAL**: manually create an image
        # - **IMAGE_MANUAL_RETRY**: retry manual image creation
        # - **IMAGE_FROM_INSTANCE**: create an image from an instance
        # - **IMAGE_FROM_INSTANCE_RETRY**: retry image creation from an instance
        # - **IMAGE_DISTRIBUTE**: distribute an image to multiple regions
        # - **IMAGE_DISTRIBUTE_RETRY**: retry image distribution
        # - **SNAPSHOT_DISTRIBUTE**: distribute a snapshot to multiple regions
        # - **SNAPSHOT_DISTRIBUTE_RETRY**: retry snapshot distribution
        # - **SNAPSHOT_FROM_DISK**: create a snapshot from a disk
        # - **SNAPSHOT_FROM_DISK_RETRY**: retry snapshot creation from a disk
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

