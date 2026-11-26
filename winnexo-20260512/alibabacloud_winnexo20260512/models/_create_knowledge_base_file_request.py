# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseFileRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
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
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The description of the alias.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The file name extension. This parameter is optional. Examples: pdf and docx.
        self.file_ext = file_ext
        # The file name.
        self.file_name = file_name
        # The file path.
        # 
        # This parameter is required.
        self.file_path = file_path
        # The publicly accessible URL of the DingTalk online document.
        self.file_public_url = file_public_url
        # The file record ID. This parameter is optional and corresponds to settings.file_record_id.
        self.file_record_id = file_record_id
        # Not supported. Ignore this parameter.
        self.knowledge_id = knowledge_id
        # The name of the AI assistant.
        # 
        # This parameter is required.
        self.name = name
        # The name of the digital employee (operating object name). This parameter is optional.
        self.operating_object_name = operating_object_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The resource labels. This parameter is optional. Specify a JSON string list, such as ["tagA","tagB"].
        self.source_tags = source_tags
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

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

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

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

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

