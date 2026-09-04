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
        # The status code.
        self.code = code
        # The description of the to-do card type.
        self.description = description
        # The folder ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The tenant folder ID.
        # 
        # This parameter is required.
        self.id = id
        # The description of the status code.
        self.message = message
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The name of the digital employee (the operating object name, optional).
        self.operating_object_name = operating_object_name
        # The ID of the parent node.
        self.parent_id = parent_id
        # The path of the node.
        # 
        # This parameter is required.
        self.path = path
        # The request ID.
        self.request_id = request_id
        # The ID of the tenant for which the operation takes effect.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id
        # The user ID of the creator.
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

