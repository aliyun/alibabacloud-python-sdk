# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class UpdateChatSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        session: main_models.UpdateChatSessionResponseBodySession = None,
    ):
        # The business status code. A value of 200 indicates success. A non-200 value indicates a backend error code (ERR.* / InvalidParameter.*).
        self.code = code
        # The error description. This is empty when the request is successful.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The session ID.
        self.session = session

    def validate(self):
        if self.session:
            self.session.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session is not None:
            result['session'] = self.session.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('session') is not None:
            temp_model = main_models.UpdateChatSessionResponseBodySession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class UpdateChatSessionResponseBodySession(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        id: str = None,
        is_expired: bool = None,
        metadata: Dict[str, Any] = None,
        model: str = None,
        object: str = None,
        object_id: str = None,
        operating_object_name: List[str] = None,
        title: str = None,
        updated_at: int = None,
    ):
        # The creation time.
        self.created_at = created_at
        # The message ID.
        self.id = id
        # Indicates whether the creation time exceeds 30 days.
        self.is_expired = is_expired
        # The associated object ID.
        self.metadata = metadata
        # The abstract model name used by the session (quick/standard/flagship).
        self.model = model
        # The type.
        self.object = object
        # The associated object ID.
        self.object_id = object_id
        # The operating object name.
        self.operating_object_name = operating_object_name
        # The title.
        self.title = title
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.id is not None:
            result['id'] = self.id

        if self.is_expired is not None:
            result['isExpired'] = self.is_expired

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.model is not None:
            result['model'] = self.model

        if self.object is not None:
            result['object'] = self.object

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.title is not None:
            result['title'] = self.title

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isExpired') is not None:
            self.is_expired = m.get('isExpired')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

