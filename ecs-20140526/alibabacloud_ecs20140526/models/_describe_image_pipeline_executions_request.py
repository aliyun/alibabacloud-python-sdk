# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImagePipelineExecutionsRequest(DaraModel):
    def __init__(
        self,
        execution_id: str = None,
        image_pipeline_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        tag: List[main_models.DescribeImagePipelineExecutionsRequestTag] = None,
    ):
        # The ID of the image build task.
        self.execution_id = execution_id
        # The ID of the image template.
        self.image_pipeline_id = image_pipeline_id
        # The maximum number of entries per page for paging. Valid values: 1 to 500.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The pagination token. Set this parameter to the value of NextToken returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the image build task. You can specify multiple values at the same time. Separate multiple values with commas (,). Example: `BUILDING,DISTRIBUTING`. Valid values:
        # 
        # - PREPARING: The task is being prepared. Resources such as the temporary intermediate instance are being created.
        # - REPAIRING: The task is being repaired. The source image is being repaired.
        # - BUILDING: The task is being built. Custom commands are being run and the image is being created.
        # - TESTING: The task is being tested. Custom test commands are being run.
        # - DISTRIBUTING: The task is being distributed. Image copying and sharing are being performed.
        # - RELEASING: Resources are being reclaimed. Temporary resources generated during the build process are being released.
        # - SUCCESS: The task succeeded.
        # - PARTITION_SUCCESS: The task partially succeeded. The image was built, but exceptions may have occurred during distribution or resource cleanup.
        # - FAILED: The task failed.
        # - TEST_FAILED: The test failed. The image was created, but the test failed.
        # - CANCELLING: The task is being canceled.
        # - CANCELLED: The task was canceled.
        # 
        # > If this parameter is empty, image build tasks in all states are queried.
        self.status = status
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.image_pipeline_id is not None:
            result['ImagePipelineId'] = self.image_pipeline_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('ImagePipelineId') is not None:
            self.image_pipeline_id = m.get('ImagePipelineId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeImagePipelineExecutionsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelineExecutionsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. Valid values of N: 1 to 20.
        self.key = key
        # The value of the tag. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

