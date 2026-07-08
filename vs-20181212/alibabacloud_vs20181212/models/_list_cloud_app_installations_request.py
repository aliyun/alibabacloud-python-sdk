# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudAppInstallationsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        patch_id: str = None,
        project_id: str = None,
        rendering_instance_id: str = None,
        start_time: str = None,
    ):
        # Cloud application ID. Each ID maps to a unique application package.
        self.app_id = app_id
        # Application name.
        self.app_name = app_name
        # Application version.
        self.app_version = app_version
        # Time range filter. Use ISO 8601 format and UTC time, such as yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # Page number of the returned list. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # Number of entries per page for paged queries. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # Patch package ID. Supported only in Windows scenarios.
        # 
        # 1. Set to origin to return only original versions.
        self.patch_id = patch_id
        # Project ID.
        self.project_id = project_id
        # Cloud application service instance ID. Use this to list installations on a specific instance.
        self.rendering_instance_id = rendering_instance_id
        # Start time of the time range filter. Specify in ISO 8601 format using UTC time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

