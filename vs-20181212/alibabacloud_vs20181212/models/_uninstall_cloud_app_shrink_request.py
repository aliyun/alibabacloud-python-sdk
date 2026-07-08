# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UninstallCloudAppShrinkRequest(DaraModel):
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
        # Cloud application ID
        # 
        # This parameter is required.
        self.app_id = app_id
        # Page number for paged queries of instance associations in the project. Results are sorted by association time in descending order. This parameter applies only when ProjectId is not empty. It limits the maximum number of instances affected by this operation to control impact scope. Default value: 1.
        # 
        # 1. Valid PageNumber range:
        #    a. Recommended method: Calculate the upper limit based on the total number of instances associated with the project. You can get this count using the ListRenderingProjectInstances API.
        #    b. Alternative method: Check the API response to determine whether PageNumber has reached the upper limit. This avoids manual calculation. PageNumber has reached the upper limit if either of the following occurs:
        #    ⅰ. The API returns HTTP status 403 and error code 200301.
        #    ⅱ. The sum of SuccessInstanceCount and FailedInstanceCount in the response is less than PageSize.
        # 
        # 2. Example scenario:
        #    a. Full uninstall across all project instances: If the project has more instances than PageSize (default 100), call UninstallCloudApp multiple times, incrementing PageNumber by 1 each time. Track uninstall progress using the ListCloudAppInstallations API.
        self.page_number = page_number
        # Maximum number of instances selected in the project. This parameter applies only when ProjectId is not empty. It limits the maximum number of instances affected by this operation to control impact scope. Default value: 100. Valid values: 1 to 100.
        self.page_size = page_size
        # ID of the patch package to uninstall. Supported only on Windows.
        # 
        # 1. Default: uninstall the StablePatchId.
        # 
        # 2. Set to origin to uninstall the original version.
        # 
        # 3. Set to all to uninstall all installed versions.
        self.patch_id = patch_id
        # Project ID
        self.project_id = project_id
        # Cloud application instance ID
        self.rendering_instance_id = rendering_instance_id
        # List of cloud application instance IDs
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

