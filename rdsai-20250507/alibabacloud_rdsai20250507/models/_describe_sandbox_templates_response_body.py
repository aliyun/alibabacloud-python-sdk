# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeSandboxTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sandbox_templates: List[main_models.DescribeSandboxTemplatesResponseBodySandboxTemplates] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.sandbox_templates = sandbox_templates
        self.total_count = total_count

    def validate(self):
        if self.sandbox_templates:
            for v1 in self.sandbox_templates:
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SandboxTemplates'] = []
        if self.sandbox_templates is not None:
            for k1 in self.sandbox_templates:
                result['SandboxTemplates'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sandbox_templates = []
        if m.get('SandboxTemplates') is not None:
            for k1 in m.get('SandboxTemplates'):
                temp_model = main_models.DescribeSandboxTemplatesResponseBodySandboxTemplates()
                self.sandbox_templates.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSandboxTemplatesResponseBodySandboxTemplates(DaraModel):
    def __init__(
        self,
        default_cpu: str = None,
        default_memory: str = None,
        description: str = None,
        enable_vpc_access: str = None,
        name: str = None,
        template_id: str = None,
    ):
        self.default_cpu = default_cpu
        self.default_memory = default_memory
        self.description = description
        self.enable_vpc_access = enable_vpc_access
        self.name = name
        self.template_id = template_id

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

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_vpc_access is not None:
            result['EnableVpcAccess'] = self.enable_vpc_access

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCpu') is not None:
            self.default_cpu = m.get('DefaultCpu')

        if m.get('DefaultMemory') is not None:
            self.default_memory = m.get('DefaultMemory')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableVpcAccess') is not None:
            self.enable_vpc_access = m.get('EnableVpcAccess')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

