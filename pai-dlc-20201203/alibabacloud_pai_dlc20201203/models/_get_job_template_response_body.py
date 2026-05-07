# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class GetJobTemplateResponseBody(DaraModel):
    def __init__(
        self,
        default_version: int = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        metadata: Dict[str, Any] = None,
        modified_by: str = None,
        request_id: str = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        total_count: int = None,
        user_id: str = None,
        versions: List[main_models.GetJobTemplateResponseBodyVersions] = None,
        workspace_id: str = None,
    ):
        # 当前默认使用的版本号
        self.default_version = default_version
        self.description = description
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modify_time = gmt_modify_time
        self.metadata = metadata
        self.modified_by = modified_by
        # 本次请求的 ID，用于诊断和答疑。
        self.request_id = request_id
        self.template_id = template_id
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.total_count = total_count
        self.user_id = user_id
        # 模板版本详情列表。查询单个版本时返回1个元素，查询所有版本时返回全部
        self.versions = versions
        self.workspace_id = workspace_id

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_id is not None:
            result['UserId'] = self.user_id

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.GetJobTemplateResponseBodyVersions()
                self.versions.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetJobTemplateResponseBodyVersions(DaraModel):
    def __init__(
        self,
        constraints: Dict[str, Any] = None,
        content: Any = None,
        created_by: str = None,
        gmt_create_time: str = None,
        version: int = None,
    ):
        # 字段约束规则。Key 为 JSONPath 表达式，Value 为约束类型
        self.constraints = constraints
        # 该版本的模板配置内容，JSON 格式
        self.content = content
        self.created_by = created_by
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.content is not None:
            result['Content'] = self.content

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

