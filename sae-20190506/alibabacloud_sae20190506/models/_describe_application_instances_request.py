# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationInstancesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        group_id: str = None,
        instance_id: str = None,
        page_size: int = None,
        pipeline_id: str = None,
        reverse: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The number of the page to return.
        self.current_page = current_page
        # The ID of the application group. Call the [DescribeApplicationGroups](https://help.aliyun.com/document_detail/126249.html) operation to get the ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The application instance ID.
        self.instance_id = instance_id
        # The number of entries to return on each page. Default value: **10**. The value must be in the range (0, 1000000000).
        self.page_size = page_size
        # The batch ID. Call the [DescribeChangeOrder](https://help.aliyun.com/document_detail/126617.html) operation to get the ID.
        self.pipeline_id = pipeline_id
        # Specifies the sort order of the application instances. Instances are sorted first by running status, and then by instance ID. Valid values:
        # 
        # - **true**: The instances are sorted in descending order.
        # 
        # - **false**: The instances are sorted in ascending order.
        # 
        # Instance statuses in ascending order:
        # 
        # 1. **Error**: An error occurred during instance startup.
        # 
        # 2. **CrashLoopBackOff**: The container fails to start and enters a crash-restart loop.
        # 
        # 3. **ErrImagePull**: An error occurred while pulling the container image for the instance.
        # 
        # 4. **ImagePullBackOff**: The system is repeatedly trying and failing to pull the container image.
        # 
        # 5. **Pending**: The instance is waiting to be scheduled.
        # 
        # 6. **Unknown**: An unknown exception occurred.
        # 
        # 7. **Terminating**: The instance is being terminated.
        # 
        # 8. **NotFound**: The instance cannot be found.
        # 
        # 9. **PodInitializing**: The instance is being initialized.
        # 
        # 10. **Init:0/1**: The instance is being initialized.
        # 
        # 11. **Running**: The instance is running.
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        return self

