# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstallCloudAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        patch_id: str = None,
        project_id: str = None,
        rendering_instance_id: str = None,
        rendering_instance_ids: List[str] = None,
    ):
        # Cloud application ID
        # 
        # This parameter is required.
        self.app_id = app_id
        # Page number for paged queries of instance associations under the project. Paged queries default to reverse order by instance association time. This applies only when ProjectId is not empty. It limits the maximum number of instances for actions within the project, controlling the impact scope. Default is 1.
        # 
        # 1. PageNumber value range:
        #    a. Method one (recommended): Calculate the upper limit using the total number of instances associated with the project. The ListRenderingProjectInstances interface provides this count.
        #    b. Method two: Determine if PageNumber reaches the project\\"s upper limit by checking the interface return value. This avoids calculating the range. PageNumber reaches the upper limit if the interface returns any of these conditions:
        #    ⅰ. A 403 status code and error code 200301.
        #    ⅱ. The sum of \\`SuccessInstanceCount\\` and \\`FailedInstanceCount\\` is less than \\`PageSize\\`.
        # 
        # 2. Scenario examples:
        #    a. Full installation for project instances: If the number of project instances exceeds \\`PageSize\\` (default 100), invoke Install multiple times. Increment PageNumber by 1 for each call to complete the full installation. Get project instance installation progress using the ListCloudAppInstallations interface.
        #    b. New instance installation for a project: Start with \\`PageNumber=1\\`. Paged queries default to reverse order by instance association time. The \\`PageNumber=1\\` page shows the latest new instances.
        self.page_number = page_number
        # Maximum number of instances selected for the project. This applies only when ProjectId is not empty. It limits the maximum number of instances for actions within the project, controlling the impact scope. Default is 100. The value range is 1-100.
        self.page_size = page_size
        # Patch package ID to install. This is only for Windows scenarios.
        # 
        # 1. Install \\`StablePatchId\\` by default.
        # 
        # 2. Enter \\`origin\\` to install the original version.
        self.patch_id = patch_id
        # Project ID
        self.project_id = project_id
        # Cloud application service instance ID
        self.rendering_instance_id = rendering_instance_id
        # List of cloud application service instance IDs
        self.rendering_instance_ids = rendering_instance_ids

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

        if self.rendering_instance_ids is not None:
            result['RenderingInstanceIds'] = self.rendering_instance_ids

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
            self.rendering_instance_ids = m.get('RenderingInstanceIds')

        return self

