# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProcessDefinitionWithScheduleShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_email_address: str = None,
        description: str = None,
        execution_type: str = None,
        global_params_shrink: str = None,
        name: str = None,
        product_namespace: str = None,
        publish: bool = None,
        region_id: str = None,
        resource_queue: str = None,
        retry_times: int = None,
        run_as: str = None,
        schedule_shrink: str = None,
        tags_shrink: str = None,
        task_definition_json_shrink: str = None,
        task_parallelism: int = None,
        task_relation_json_shrink: str = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The description of the workflow.
        # 
        # This parameter is required.
        self.description = description
        # The execution policy
        # 
        # This parameter is required.
        self.execution_type = execution_type
        self.global_params_shrink = global_params_shrink
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # Specifies whether to publish the workflow.
        self.publish = publish
        # The region ID.
        self.region_id = region_id
        # The resource queue.
        self.resource_queue = resource_queue
        # The number of retries.
        self.retry_times = retry_times
        # The ID of the Alibaba Cloud account used by the user who creates the workflow.
        self.run_as = run_as
        # The scheduling settings.
        self.schedule_shrink = schedule_shrink
        # The tags.
        self.tags_shrink = tags_shrink
        # The descriptions of all nodes in the workflow.
        # 
        # This parameter is required.
        self.task_definition_json_shrink = task_definition_json_shrink
        # The node parallelism.
        self.task_parallelism = task_parallelism
        # The dependencies of all nodes in the workflow. preTaskCode specifies the ID of an upstream node, and postTaskCode specifies the ID of a downstream node. The ID of each node is unique. If a node does not have an upstream node, set preTaskCode to 0.
        # 
        # This parameter is required.
        self.task_relation_json_shrink = task_relation_json_shrink
        # The default timeout period of the workflow.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address

        if self.description is not None:
            result['description'] = self.description

        if self.execution_type is not None:
            result['executionType'] = self.execution_type

        if self.global_params_shrink is not None:
            result['globalParams'] = self.global_params_shrink

        if self.name is not None:
            result['name'] = self.name

        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace

        if self.publish is not None:
            result['publish'] = self.publish

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_queue is not None:
            result['resourceQueue'] = self.resource_queue

        if self.retry_times is not None:
            result['retryTimes'] = self.retry_times

        if self.run_as is not None:
            result['runAs'] = self.run_as

        if self.schedule_shrink is not None:
            result['schedule'] = self.schedule_shrink

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        if self.task_definition_json_shrink is not None:
            result['taskDefinitionJson'] = self.task_definition_json_shrink

        if self.task_parallelism is not None:
            result['taskParallelism'] = self.task_parallelism

        if self.task_relation_json_shrink is not None:
            result['taskRelationJson'] = self.task_relation_json_shrink

        if self.timeout is not None:
            result['timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')

        if m.get('globalParams') is not None:
            self.global_params_shrink = m.get('globalParams')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')

        if m.get('publish') is not None:
            self.publish = m.get('publish')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceQueue') is not None:
            self.resource_queue = m.get('resourceQueue')

        if m.get('retryTimes') is not None:
            self.retry_times = m.get('retryTimes')

        if m.get('runAs') is not None:
            self.run_as = m.get('runAs')

        if m.get('schedule') is not None:
            self.schedule_shrink = m.get('schedule')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('taskDefinitionJson') is not None:
            self.task_definition_json_shrink = m.get('taskDefinitionJson')

        if m.get('taskParallelism') is not None:
            self.task_parallelism = m.get('taskParallelism')

        if m.get('taskRelationJson') is not None:
            self.task_relation_json_shrink = m.get('taskRelationJson')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        return self

