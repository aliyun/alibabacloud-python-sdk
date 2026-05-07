# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ListJobTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        job_templates: List[main_models.ListJobTemplatesResponseBodyJobTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.job_templates = job_templates
        self.page_number = page_number
        self.page_size = page_size
        # 本次请求的 ID，用于诊断和答疑。
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.job_templates:
            for v1 in self.job_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobTemplates'] = []
        if self.job_templates is not None:
            for k1 in self.job_templates:
                result['JobTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_templates = []
        if m.get('JobTemplates') is not None:
            for k1 in m.get('JobTemplates'):
                temp_model = main_models.ListJobTemplatesResponseBodyJobTemplates()
                self.job_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListJobTemplatesResponseBodyJobTemplates(DaraModel):
    def __init__(
        self,
        default_version: int = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        metadata: Dict[str, Any] = None,
        modified_by: str = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.default_version = default_version
        self.description = description
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modify_time = gmt_modify_time
        self.metadata = metadata
        self.modified_by = modified_by
        self.template_id = template_id
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.modified_by is not None:
            result['ModifiedBy'] = self.modified_by

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('ModifiedBy') is not None:
            self.modified_by = m.get('ModifiedBy')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

