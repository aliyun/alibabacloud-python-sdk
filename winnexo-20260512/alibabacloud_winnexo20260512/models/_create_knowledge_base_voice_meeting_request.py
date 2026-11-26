# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseVoiceMeetingRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        description: str = None,
        directory_id: str = None,
        file_url: str = None,
        name: str = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # token
        self.app_token = app_token
        # The description of the AI assistant.
        self.description = description
        # The directory ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The attachment URL in Yida.
        # 
        # This parameter is required.
        self.file_url = file_url
        # The name of the AI assistant.
        # 
        # This parameter is required.
        self.name = name
        # The name of the digital employee. This is the name of the operating object and is optional.
        self.operating_object_name = operating_object_name
        # The code of the operator.
        self.ops_user_code = ops_user_code
        # The ID of the operator.
        self.ops_user_id = ops_user_id
        # The resource tags. This parameter is optional and accepts a JSON string list, such as ["tagA","tagB"].
        self.source_tags = source_tags
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
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

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

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

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

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

