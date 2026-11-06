# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListWuyingServerWorkloadTemplateResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        workload_templates: List[main_models.ListWuyingServerWorkloadTemplateResponseBodyWorkloadTemplates] = None,
    ):
        # A compatibility field. The current version does not use this field to indicate the number of returned entries.
        self.max_results = max_results
        # A compatibility field. The current version does not generate a next page token.
        self.next_token = next_token
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id
        # The list of workload templates. Up to 100 templates are returned, sorted by template configuration order.
        self.workload_templates = workload_templates

    def validate(self):
        if self.workload_templates:
            for v1 in self.workload_templates:
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

        result['WorkloadTemplates'] = []
        if self.workload_templates is not None:
            for k1 in self.workload_templates:
                result['WorkloadTemplates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.workload_templates = []
        if m.get('WorkloadTemplates') is not None:
            for k1 in m.get('WorkloadTemplates'):
                temp_model = main_models.ListWuyingServerWorkloadTemplateResponseBodyWorkloadTemplates()
                self.workload_templates.append(temp_model.from_map(k1))

        return self

class ListWuyingServerWorkloadTemplateResponseBodyWorkloadTemplates(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        name: str = None,
    ):
        # The rendered template content. The original text is Base64-encoded after being encoded in UTF-8. You must decode the Base64 string before use.
        self.content = content
        # The description of the workload template.
        self.description = description
        # The name of the workload template.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

