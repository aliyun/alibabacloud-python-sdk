# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeCommonSandboxTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        templates: List[main_models.DescribeCommonSandboxTemplatesResponseBodyTemplates] = None,
    ):
        # A reserved parameter. You do not need to specify this parameter.
        self.max_results = max_results
        # The token that indicates the position from which the query starts. Set this parameter to empty to start from the beginning.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The sandbox templates.
        self.templates = templates

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.DescribeCommonSandboxTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class DescribeCommonSandboxTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        default_cpu: str = None,
        default_memory: str = None,
        default_replicas: int = None,
        description: str = None,
        name: str = None,
    ):
        # The default number of CPUs for sandboxes created by using this template.
        self.default_cpu = default_cpu
        # The default memory size for sandboxes created by using this template. The unit ends with Gi.
        self.default_memory = default_memory
        # The default number of prewarmed sandboxes.
        self.default_replicas = default_replicas
        # The description of the sandbox template.
        self.description = description
        # The name of the sandbox template.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_cpu is not None:
            result['DefaultCpu'] = self.default_cpu

        if self.default_memory is not None:
            result['DefaultMemory'] = self.default_memory

        if self.default_replicas is not None:
            result['DefaultReplicas'] = self.default_replicas

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCpu') is not None:
            self.default_cpu = m.get('DefaultCpu')

        if m.get('DefaultMemory') is not None:
            self.default_memory = m.get('DefaultMemory')

        if m.get('DefaultReplicas') is not None:
            self.default_replicas = m.get('DefaultReplicas')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

