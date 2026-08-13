# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseFileRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        file_ext: str = None,
        file_name: str = None,
        file_path: str = None,
        file_public_url: str = None,
        file_record_id: str = None,
        knowledge_id: str = None,
        name: str = None,
        operating_object_name: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # 资源描述（可选）
        self.description = description
        # 目标企业知识库目录 ID；不传时自动绑定到当前数字员工默认根目录，传入时必须是当前租户下已有的企业知识库目录
        self.directory_id = directory_id
        # 文件后缀名（可选，如 pdf、docx）
        self.file_ext = file_ext
        # 原始文件名（可选，含后缀）
        self.file_name = file_name
        # 文件 OSS 持久化地址（必填，对应 settings.file_path）
        # 
        # This parameter is required.
        self.file_path = file_path
        # 文件公开访问 URL（可选，带签名，对应 settings.file_public_url）
        self.file_public_url = file_public_url
        # 文件记录 ID（可选，对应 settings.file_record_id）
        self.file_record_id = file_record_id
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
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

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

        if self.file_ext is not None:
            result['fileExt'] = self.file_ext

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_path is not None:
            result['filePath'] = self.file_path

        if self.file_public_url is not None:
            result['filePublicUrl'] = self.file_public_url

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('fileExt') is not None:
            self.file_ext = m.get('fileExt')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')

        if m.get('filePublicUrl') is not None:
            self.file_public_url = m.get('filePublicUrl')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

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

        return self

