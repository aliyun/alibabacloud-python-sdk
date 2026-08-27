# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalDingtalkMeetingRequest(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        description: str = None,
        directory_id: str = None,
        name: str = None,
        notes: str = None,
        operating_object_name: str = None,
        room_code: str = None,
        tenant_id: str = None,
    ):
        # The credential ID.
        self.credential_id = credential_id
        # The pipeline description.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The image name.
        # 
        # This parameter is required.
        self.name = name
        # The meeting notes content (optional). The notes are used for auxiliary analysis.
        self.notes = notes
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The meeting code.
        # 
        # This parameter is required.
        self.room_code = room_code
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

        if self.name is not None:
            result['name'] = self.name

        if self.notes is not None:
            result['notes'] = self.notes

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.room_code is not None:
            result['roomCode'] = self.room_code

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

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('roomCode') is not None:
            self.room_code = m.get('roomCode')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

