# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListWorkspaceQueuesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        queues: List[main_models.ListWorkspaceQueuesResponseBodyQueues] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The list of queues.
        self.queues = queues
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.queues:
            for v1 in self.queues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['queues'] = []
        if self.queues is not None:
            for k1 in self.queues:
                result['queues'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.queues = []
        if m.get('queues') is not None:
            for k1 in m.get('queues'):
                temp_model = main_models.ListWorkspaceQueuesResponseBodyQueues()
                self.queues.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListWorkspaceQueuesResponseBodyQueues(DaraModel):
    def __init__(
        self,
        allow_actions: List[main_models.ListWorkspaceQueuesResponseBodyQueuesAllowActions] = None,
        create_time: int = None,
        creator: str = None,
        environments: List[str] = None,
        max_resource: str = None,
        min_resource: str = None,
        payment_type: str = None,
        preheat: bool = None,
        properties: str = None,
        queue_name: str = None,
        queue_scope: str = None,
        queue_status: str = None,
        queue_type: str = None,
        region_id: str = None,
        used_resource: str = None,
        workspace_id: str = None,
    ):
        # The operations allowed for the queue.
        self.allow_actions = allow_actions
        # The time when the workspace was created.
        self.create_time = create_time
        # The ID of the user who created the queue.
        self.creator = creator
        # The environment types of the queue.
        self.environments = environments
        # The maximum capacity of resources that can be used in the queue.
        self.max_resource = max_resource
        # The minimum capacity of resources that can be used in the queue.
        self.min_resource = min_resource
        # The billing method. Valid values:
        # 
        # *   PayAsYouGo
        # *   Pre
        self.payment_type = payment_type
        self.preheat = preheat
        # The queue label.
        self.properties = properties
        # The name of the queue.
        self.queue_name = queue_name
        # The queue architecture.
        self.queue_scope = queue_scope
        # The status of the queue.
        self.queue_status = queue_status
        # The type of the queue. Valid values:
        # 
        # *   instance
        # *   instanceChildren
        self.queue_type = queue_type
        # The region ID.
        self.region_id = region_id
        # The capacity of resources that are used in the queue.
        self.used_resource = used_resource
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.allow_actions:
            for v1 in self.allow_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['allowActions'] = []
        if self.allow_actions is not None:
            for k1 in self.allow_actions:
                result['allowActions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator is not None:
            result['creator'] = self.creator

        if self.environments is not None:
            result['environments'] = self.environments

        if self.max_resource is not None:
            result['maxResource'] = self.max_resource

        if self.min_resource is not None:
            result['minResource'] = self.min_resource

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.preheat is not None:
            result['preheat'] = self.preheat

        if self.properties is not None:
            result['properties'] = self.properties

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.queue_scope is not None:
            result['queueScope'] = self.queue_scope

        if self.queue_status is not None:
            result['queueStatus'] = self.queue_status

        if self.queue_type is not None:
            result['queueType'] = self.queue_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.used_resource is not None:
            result['usedResource'] = self.used_resource

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allow_actions = []
        if m.get('allowActions') is not None:
            for k1 in m.get('allowActions'):
                temp_model = main_models.ListWorkspaceQueuesResponseBodyQueuesAllowActions()
                self.allow_actions.append(temp_model.from_map(k1))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('environments') is not None:
            self.environments = m.get('environments')

        if m.get('maxResource') is not None:
            self.max_resource = m.get('maxResource')

        if m.get('minResource') is not None:
            self.min_resource = m.get('minResource')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('preheat') is not None:
            self.preheat = m.get('preheat')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('queueScope') is not None:
            self.queue_scope = m.get('queueScope')

        if m.get('queueStatus') is not None:
            self.queue_status = m.get('queueStatus')

        if m.get('queueType') is not None:
            self.queue_type = m.get('queueType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('usedResource') is not None:
            self.used_resource = m.get('usedResource')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListWorkspaceQueuesResponseBodyQueuesAllowActions(DaraModel):
    def __init__(
        self,
        action_arn: str = None,
        action_name: str = None,
        dependencies: List[str] = None,
        description: str = None,
        display_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of a behavior.
        self.action_arn = action_arn
        # The name of the permission.
        self.action_name = action_name
        # The dependencies of the operation.
        self.dependencies = dependencies
        # The description of the operation.
        self.description = description
        # The display name of the permission.
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_arn is not None:
            result['actionArn'] = self.action_arn

        if self.action_name is not None:
            result['actionName'] = self.action_name

        if self.dependencies is not None:
            result['dependencies'] = self.dependencies

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionArn') is not None:
            self.action_arn = m.get('actionArn')

        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')

        if m.get('dependencies') is not None:
            self.dependencies = m.get('dependencies')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        return self

