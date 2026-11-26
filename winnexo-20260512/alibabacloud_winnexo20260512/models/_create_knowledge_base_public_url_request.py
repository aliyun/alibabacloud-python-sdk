# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBasePublicUrlRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        description: str = None,
        directory_id: str = None,
        name: str = None,
        notes: str = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        original_url: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If specified, the operation is performed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The description of the resource.
        self.description = description
        # The ID of the target folder in the enterprise knowledge base. This parameter is required, and you must have knowledge base management permissions on the knowledge base.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The name of the resource. If not specified, the URL is used.
        self.name = name
        # The analysis instructions.
        self.notes = notes
        # The name of the operating object.
        self.operating_object_name = operating_object_name
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The URL of the public HTTP or HTTPS web page.
        # 
        # This parameter is required.
        self.original_url = original_url
        # The list of resource tags in JSON string format.
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

        if self.name is not None:
            result['name'] = self.name

        if self.notes is not None:
            result['notes'] = self.notes

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.original_url is not None:
            result['originalUrl'] = self.original_url

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

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('originalUrl') is not None:
            self.original_url = m.get('originalUrl')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

