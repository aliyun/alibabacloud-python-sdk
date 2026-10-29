# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallCloudAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        patch_id: str = None,
        project_id: str = None,
        rendering_instance_id: str = None,
        rendering_instance_ids_shrink: str = None,
    ):
        # The cloud application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The page number for the paged query of instance associations under the project. By default, the paged query is sorted by instance association time in descending order. This parameter takes effect only when ProjectId is not empty. It limits the maximum number of instances on which the operation is executed under the project to control the impact scope. Default value: 1.
        # 1. About the value range of PageNumber:
        #   a. [Recommended] Method 1: Calculate the upper limit based on the total number of instances associated with the project (you can call the ListRenderingProjectInstances operation to obtain the total number).
        #   b. Method 2: Determine whether PageNumber has reached the upper limit of the project based on the response. [Advantage: You do not need to calculate the value range.] If the response meets either of the following conditions, PageNumber has reached the upper limit:
        #     i. The response returns HTTP status code 403 and error code 200301.
        #     ii. The response returns SuccessInstanceCount + FailedInstanceCount < PageSize.
        # 2. Example scenarios:
        #   a. Full installation for instances under a project: If the number of instances in the project is greater than PageSize (default value: 100), you can call the Install operation multiple times by incrementing PageNumber by 1 each time to perform a full installation. You can call the ListCloudAppInstallations operation to query the installation progress of the instances.
        #   b. Installation for newly added instances under a project: Start with PageNumber=1. By default, the paged query is sorted by instance association time in descending order. The page with PageNumber=1 contains the most recently added instances.
        self.page_number = page_number
        # The maximum number of instances that can be selected under the project. This parameter takes effect only when ProjectId is not empty. It limits the maximum number of instances on which the operation is performed under the project to control the impact scope. Default value: 100. Valid values: 1 to 100.
        self.page_size = page_size
        # The patch package ID to install. This parameter is supported only in Windows scenarios.
        # 1. By default, StablePatchId is installed.
        # 2. If you set the value to origin, the original version is installed.
        self.patch_id = patch_id
        # The project ID.
        self.project_id = project_id
        # The cloud application service instance ID.
        self.rendering_instance_id = rendering_instance_id
        # The list of cloud application service instance IDs.
        self.rendering_instance_ids_shrink = rendering_instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.rendering_instance_ids_shrink is not None:
            result['RenderingInstanceIds'] = self.rendering_instance_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RenderingInstanceIds') is not None:
            self.rendering_instance_ids_shrink = m.get('RenderingInstanceIds')

        return self

