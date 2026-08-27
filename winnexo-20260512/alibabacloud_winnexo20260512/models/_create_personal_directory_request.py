# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalDirectoryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        operating_object_name: str = None,
        parent_directory_id: str = None,
        tenant_id: str = None,
    ):
        # The workspace description.
        self.description = description
        # The name of the digital human.
        # 
        # This parameter is required.
        self.name = name
        # The name of the digital human (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The folder ID.
        self.parent_directory_id = parent_directory_id
        # The tenant ID.
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

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

