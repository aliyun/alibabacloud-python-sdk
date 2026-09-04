# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetChatSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        messages: List[main_models.GetChatSessionResponseBodyMessages] = None,
        request_id: str = None,
        session: main_models.GetChatSessionResponseBodySession = None,
    ):
        # The error code.
        self.code = code
        # The status code description.
        self.message = message
        # The message data detail structure.
        self.messages = messages
        # The request ID.
        self.request_id = request_id
        # The session information.
        self.session = session

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
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

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

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

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.GetChatSessionResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('session') is not None:
            temp_model = main_models.GetChatSessionResponseBodySession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class GetChatSessionResponseBodySession(DaraModel):
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
        # Indicates whether the creation time is older than 30 days.
        self.is_expired = is_expired
        # The session metadata.
        self.metadata = metadata
        # The abstract model name used by the session (quick/standard/flagship).
        self.model = model
        # The type.
        self.object = object
        # The associated object ID.
        self.object_id = object_id
        # The list of digital employee names.
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

class GetChatSessionResponseBodyMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        context_cleared: bool = None,
        from_share: bool = None,
        id: str = None,
        metadata: Dict[str, Any] = None,
        object: str = None,
        role: str = None,
        share_user_name: str = None,
        status: str = None,
        trace_id: str = None,
        update_at: int = None,
        user_feedback: str = None,
    ):
        # The message content.
        self.content = content
        # Indicates whether the LLM context has been cleared after this message.
        self.context_cleared = context_cleared
        # Indicates whether the message is copied from a shared conversation.
        self.from_share = from_share
        # The message ID.
        self.id = id
        # The message metadata.
        self.metadata = metadata
        # The type.
        self.object = object
        # The role.
        self.role = role
        # The username of the user who shared the message. This parameter has a value only when from_share is set to True.
        self.share_user_name = share_user_name
        # The message status.
        self.status = status
        # The trace ID.
        self.trace_id = trace_id
        # The update time.
        self.update_at = update_at
        # The user feedback type: LIKE | DISLIKE | CANCEL.
        self.user_feedback = user_feedback

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.context_cleared is not None:
            result['contextCleared'] = self.context_cleared

        if self.from_share is not None:
            result['fromShare'] = self.from_share

        if self.id is not None:
            result['id'] = self.id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.object is not None:
            result['object'] = self.object

        if self.role is not None:
            result['role'] = self.role

        if self.share_user_name is not None:
            result['shareUserName'] = self.share_user_name

        if self.status is not None:
            result['status'] = self.status

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        if self.update_at is not None:
            result['updateAt'] = self.update_at

        if self.user_feedback is not None:
            result['userFeedback'] = self.user_feedback

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('contextCleared') is not None:
            self.context_cleared = m.get('contextCleared')

        if m.get('fromShare') is not None:
            self.from_share = m.get('fromShare')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('shareUserName') is not None:
            self.share_user_name = m.get('shareUserName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        if m.get('updateAt') is not None:
            self.update_at = m.get('updateAt')

        if m.get('userFeedback') is not None:
            self.user_feedback = m.get('userFeedback')

        return self

