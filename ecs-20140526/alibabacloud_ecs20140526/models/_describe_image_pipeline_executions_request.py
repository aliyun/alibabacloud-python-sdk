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
        # The ID of the image building task.
        self.execution_id = execution_id
        # The ID of the image template.
        self.image_pipeline_id = image_pipeline_id
        # The number of entries to return on each page. Valid values: 1 to 500.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The query token. Set the value to the `NextToken` value returned from a previous call to this operation. This parameter is not required for the first call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the image building task. You can specify multiple values, separated by commas. Example: `BUILDING,DISTRIBUTING`. Valid values:
        # 
        # - PREPARING: The system is preparing resources, such as a temporary transit instance.
        # 
        # - REPAIRING: The system is repairing the source image.
        # 
        # - BUILDING: The system is building the image. This includes executing user-defined commands and creating the image.
        # 
        # - TESTING: The system is testing the created image by running user-defined test commands.
        # 
        # - DISTRIBUTING: The system is distributing the image. This includes copying and sharing the image.
        # 
        # - RELEASING: The system is releasing temporary resources generated during the build process.
        # 
        # - SUCCESS: The task completed successfully.
        # 
        # - PARTITION_SUCCESS: The task is partially successful. The image was created, but an error may have occurred during distribution or resource cleanup.
        # 
        # - FAILED: The image building task failed.
        # 
        # - TEST_FAILED: The image was created successfully, but it failed the user-defined tests.
        # 
        # - CANCELLING: The system is canceling the image building task.
        # 
        # - CANCELLED: The image building task was canceled.
        # 
        # > If you omit this parameter, the operation returns image building tasks of all statuses.
        self.status = status
        # The list of tags.
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
        # The key of tag N. The value of N can be from 1 to 20.
        self.key = key
        # The value of tag N. The value of N can be from 1 to 20.
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

