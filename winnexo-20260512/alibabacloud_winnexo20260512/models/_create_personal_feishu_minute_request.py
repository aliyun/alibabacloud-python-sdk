# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalFeishuMinuteRequest(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        description: str = None,
        directory_id: str = None,
        minute_token: str = None,
        name: str = None,
        operating_object_name: str = None,
        tenant_id: str = None,
    ):
        # The credential ID.
        # 
        # This parameter is required.
        self.credential_id = credential_id
        # The resource description.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The Lark Minutes token (unique identifier of the minutes record, required).
        # 
        # This parameter is required.
        self.minute_token = minute_token
        # The resource name.
        # 
        # This parameter is required.
        self.name = name
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.minute_token is not None:
            result['minuteToken'] = self.minute_token

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('minuteToken') is not None:
            self.minute_token = m.get('minuteToken')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

