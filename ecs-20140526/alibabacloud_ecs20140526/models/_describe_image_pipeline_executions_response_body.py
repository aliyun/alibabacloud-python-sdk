# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImagePipelineExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        image_pipeline_execution: main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecution = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The total number of returned image components.
        self.image_pipeline_execution = image_pipeline_execution
        # The request ID.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The maximum number of entries per page. Valid values: 1 to 500
        # 
        # Default value: 50.
        self.request_id = request_id
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists. For information about how to use the returned value, see the "Usage notes" section in this topic.
        self.total_count = total_count

    def validate(self):
        if self.image_pipeline_execution:
            self.image_pipeline_execution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_pipeline_execution is not None:
            result['ImagePipelineExecution'] = self.image_pipeline_execution.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImagePipelineExecution') is not None:
            temp_model = main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecution()
            self.image_pipeline_execution = temp_model.from_map(m.get('ImagePipelineExecution'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImagePipelineExecutionsResponseBodyImagePipelineExecution(DaraModel):
    def __init__(
        self,
        image_pipeline_execution_set: List[main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSet] = None,
    ):
        self.image_pipeline_execution_set = image_pipeline_execution_set

    def validate(self):
        if self.image_pipeline_execution_set:
            for v1 in self.image_pipeline_execution_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImagePipelineExecutionSet'] = []
        if self.image_pipeline_execution_set is not None:
            for k1 in self.image_pipeline_execution_set:
                result['ImagePipelineExecutionSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_pipeline_execution_set = []
        if m.get('ImagePipelineExecutionSet') is not None:
            for k1 in m.get('ImagePipelineExecutionSet'):
                temp_model = main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSet()
                self.image_pipeline_execution_set.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSet(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        execution_id: str = None,
        image_id: str = None,
        image_pipeline_id: str = None,
        message: str = None,
        modified_time: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSetTags = None,
    ):
        # Details of the image creation tasks.
        self.creation_time = creation_time
        # The data returned.
        self.execution_id = execution_id
        # The ID of the resource group.
        self.image_id = image_id
        # Details of the image creation task.
        self.image_pipeline_id = image_pipeline_id
        # The last modification time of the image creation task.
        self.message = message
        # The ID of the image template.
        self.modified_time = modified_time
        # The status of the image creation task. Valid values:
        # 
        # *   PREPARING: Resources, such as intermediate instances, are being created.
        # *   REPAIRING: The source image is being repaired.
        # *   BUILDING: The user-defined commands are being run and an image is being created.
        # *   TESTING: The user-defined test commands are being run.
        # *   DISTRIBUTING: The created image is being copied and shared.
        # *   RELEASING: The temporary resources generated during the image creation process are being released.
        # *   SUCCESS The image creation task is completed.
        # *   PARTITION_SUCCESS: The image creation task is partially completed. The image is created, but exceptions may occur when the image was copied or shared or when temporary resources were released.
        # *   FAILED: The image creation task fails.
        # *   TEST_FAILED: The image is created, but the test fails.
        # *   CANCELLING: The image creation task is being canceled.
        # *   CANCELLED: The image creation task is canceled.
        self.resource_group_id = resource_group_id
        # The time when the image creation task was created.
        self.status = status
        # The ID of the image.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_pipeline_id is not None:
            result['ImagePipelineId'] = self.image_pipeline_id

        if self.message is not None:
            result['Message'] = self.message

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImagePipelineId') is not None:
            self.image_pipeline_id = m.get('ImagePipelineId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSetTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelineExecutionsResponseBodyImagePipelineExecutionImagePipelineExecutionSetTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag of the image creation task.
        self.tag_key = tag_key
        # The tags of the image creation task.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

