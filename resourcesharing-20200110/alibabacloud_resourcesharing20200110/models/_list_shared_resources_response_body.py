# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class ListSharedResourcesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        shared_resources: List[main_models.ListSharedResourcesResponseBodySharedResources] = None,
    ):
        # The token that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information of the shared resources.
        self.shared_resources = shared_resources

    def validate(self):
        if self.shared_resources:
            for v1 in self.shared_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SharedResources'] = []
        if self.shared_resources is not None:
            for k1 in self.shared_resources:
                result['SharedResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.shared_resources = []
        if m.get('SharedResources') is not None:
            for k1 in m.get('SharedResources'):
                temp_model = main_models.ListSharedResourcesResponseBodySharedResources()
                self.shared_resources.append(temp_model.from_map(k1))

        return self

class ListSharedResourcesResponseBodySharedResources(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_share_id: str = None,
        resource_status: str = None,
        resource_status_message: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        # The time when the shared resource was associated with the resource share.
        self.create_time = create_time
        self.resource_arn = resource_arn
        # The ID of the shared resource.
        self.resource_id = resource_id
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The status of the shared resource. This parameter is returned only when you query the resources that other accounts share with you.
        # 
        # Valid values:
        # 
        # *   Available: The resource is available.
        # *   ZonalResourceInaccessible: The resource is unavailable in the current zone.
        # *   LimitExceeded: The resource is unavailable because the maximum number of resources that other accounts can share with you exceeds the upper limit.
        # *   Unavailable: The resource is unavailable.
        self.resource_status = resource_status
        # The cause of the association failure.
        self.resource_status_message = resource_status_message
        # The type of the shared resource.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](https://help.aliyun.com/document_detail/450526.html).
        self.resource_type = resource_type
        # The time when the association of the shared resource was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.resource_status_message is not None:
            result['ResourceStatusMessage'] = self.resource_status_message

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('ResourceStatusMessage') is not None:
            self.resource_status_message = m.get('ResourceStatusMessage')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

