# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListStacksResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        stacks: List[main_models.ListStacksResponseBodyStacks] = None,
        total_count: int = None,
    ):
        # The maximum number of results returned.
        self.max_results = max_results
        # The pagination token. This parameter is empty if no more pages are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of stacks.
        self.stacks = stacks
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.stacks:
            for v1 in self.stacks:
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['stacks'] = []
        if self.stacks is not None:
            for k1 in self.stacks:
                result['stacks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.stacks = []
        if m.get('stacks') is not None:
            for k1 in m.get('stacks'):
                temp_model = main_models.ListStacksResponseBodyStacks()
                self.stacks.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListStacksResponseBodyStacks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        stack_description: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The description of the stack.
        self.description = description
        # The stack name.
        self.name = name
        # The creation source. Valid values:
        # - OSS: a template stored in Object Storage Service (OSS).
        # - IAC_SERVICE_MODULE: a template created in the automation service console.
        self.source = source
        # The path of the configuration source. The value cannot exceed 1000 characters.
        # - If the source is OSS, the value is in the format oss::<file link> and must be a zip file, such as oss::https://terraform-pipeline.oss-eu-central-1.aliyuncs.com/code.zip.
        # - If the source is IAC_SERVICE_MODULE, the value is a template ID, such as mod-xxxxx.
        self.source_path = source_path
        # The description of the stack.
        self.stack_description = stack_description
        # The stack ID, which is the unique identifier generated after the stack is created.
        self.stack_id = stack_id
        # The stack name (deprecated). Use name instead.
        self.stack_name = stack_name
        # The stack status.
        # | Name | Description |
        # |------|------|
        # | Creating | Being created |
        # | Created | Creation complete |
        # | Waiting | Waiting for deployment |
        # | Deploying | Being deployed |
        # | Deployed | Deployment complete |
        # | Errored | Deployment failed |
        # | Deleting | Being deleted |
        # | Deleted | Deleted |
        # | DeleteFailed | Deletion failed |.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.stack_description is not None:
            result['stackDescription'] = self.stack_description

        if self.stack_id is not None:
            result['stackId'] = self.stack_id

        if self.stack_name is not None:
            result['stackName'] = self.stack_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('stackDescription') is not None:
            self.stack_description = m.get('stackDescription')

        if m.get('stackId') is not None:
            self.stack_id = m.get('stackId')

        if m.get('stackName') is not None:
            self.stack_name = m.get('stackName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

