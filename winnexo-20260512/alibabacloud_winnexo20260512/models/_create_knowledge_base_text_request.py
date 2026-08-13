# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseTextRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        knowledge_id: str = None,
        name: str = None,
        operating_object_name: str = None,
        source_tags: str = None,
        tenant_id: str = None,
        text_content: str = None,
    ):
        # 资源描述（可选）
        self.description = description
        # 目标企业知识库目录 ID；不传时自动绑定到当前数字员工默认根目录，传入时必须是当前租户下已有的企业知识库目录
        self.directory_id = directory_id
        # 知识库 ID（可选，透传给 document_agent）
        self.knowledge_id = knowledge_id
        # 资源显示名称
        # 
        # This parameter is required.
        self.name = name
        # 数字员工名称（运营对象 name，可选）
        self.operating_object_name = operating_object_name
        # 资源标签（可选，JSON 字符串列表，如 ["tagA","tagB"]）
        self.source_tags = source_tags
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 纯文本正文（必填）
        # 
        # This parameter is required.
        self.text_content = text_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.knowledge_id is not None:
            result['knowledgeId'] = self.knowledge_id

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.text_content is not None:
            result['textContent'] = self.text_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('knowledgeId') is not None:
            self.knowledge_id = m.get('knowledgeId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')

        return self

