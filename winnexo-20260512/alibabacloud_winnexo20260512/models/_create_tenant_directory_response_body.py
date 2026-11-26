# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTenantDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        directory_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        message: str = None,
        name: str = None,
        operating_object_name: str = None,
        parent_id: int = None,
        path: str = None,
        request_id: str = None,
        tenant_id: int = None,
        user_id: int = None,
    ):
        # The business status code. A value of 200 indicates success. If the request fails, a specific business error code is returned.
        self.code = code
        # The description of the created directory. If no description is set, the value is empty.
        self.description = description
        # The business ID of the newly created directory. You can use this ID to read or update the knowledge base configuration for standard enterprise root directories.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The time when the directory was created. The value is a UNIX timestamp in seconds.
        self.gmt_create = gmt_create
        # The time when the directory was last modified. The value is a UNIX timestamp in seconds.
        self.gmt_modified = gmt_modified
        # The internal primary key of the directory. You can use this key as the parentId when you create a subdirectory. This key is different from the business ID directoryId.
        # 
        # This parameter is required.
        self.id = id
        # The response message. The value is success if the request is successful. If the request fails, this parameter describes the cause of the error.
        self.message = message
        # The name of the created directory.
        # 
        # This parameter is required.
        self.name = name
        # The legacy single digital employee association field. You cannot use this field to replace the mode and association list returned by GetKnowledgeBaseConfiguration.
        self.operating_object_name = operating_object_name
        # The internal primary key of the parent directory. This value is empty for enterprise root directories.
        self.parent_id = parent_id
        # The path of the created directory.
        # 
        # This parameter is required.
        self.path = path
        # The request tracking ID. You can use this ID to troubleshoot issues related to this call.
        self.request_id = request_id
        # The ID of the tenant to which the directory belongs.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id
        # The ID of the platform user who created the directory.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.path is not None:
            result['path'] = self.path

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

