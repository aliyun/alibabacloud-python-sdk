# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        max_concurrency: int = None,
        name: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
    ):
        # The description of the workflow.
        self.description = description
        # The application group ID. You can obtain the ID on the Application Management page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The maximum number of workflow instances that can be run at the same time. Default value: 1. The value 1 indicates that only one workflow instance is allowed. In this case, if the triggered workflow instance is still ongoing, no more workflow instances can be triggered even the time to schedule the next workflow arrives.
        self.max_concurrency = max_concurrency
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The namespace ID. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The time expression. You can set the time expression based on the selected method that is used to specify time.
        # 
        # - If you set the TimeType parameter to cron, you need to enter a standard cron expression. Online verification is supported.
        # - If you set the TimeType parameter to api, no time expression is required.
        self.time_expression = time_expression
        # The method that is used to specify the time. Valid values:
        # 
        # - 1: cron
        # - 100: api
        # 
        # This parameter is required.
        self.time_type = time_type
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

