# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class CreateAgentConversationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        initial_message: main_models.CreateAgentConversationRequestInitialMessage = None,
        title: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.initial_message = initial_message
        self.title = title

    def validate(self):
        if self.initial_message:
            self.initial_message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.initial_message is not None:
            result['initialMessage'] = self.initial_message.to_map()

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('initialMessage') is not None:
            temp_model = main_models.CreateAgentConversationRequestInitialMessage()
            self.initial_message = temp_model.from_map(m.get('initialMessage'))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class CreateAgentConversationRequestInitialMessage(DaraModel):
    def __init__(
        self,
        client_context: str = None,
        images: List[main_models.CreateAgentConversationRequestInitialMessageImages] = None,
        message: str = None,
        message_type: str = None,
        ticket_request_id: str = None,
    ):
        self.client_context = client_context
        self.images = images
        # This parameter is required.
        self.message = message
        self.message_type = message_type
        self.ticket_request_id = ticket_request_id

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_context is not None:
            result['clientContext'] = self.client_context

        result['images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['images'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.ticket_request_id is not None:
            result['ticketRequestId'] = self.ticket_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientContext') is not None:
            self.client_context = m.get('clientContext')

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.CreateAgentConversationRequestInitialMessageImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('ticketRequestId') is not None:
            self.ticket_request_id = m.get('ticketRequestId')

        return self

class CreateAgentConversationRequestInitialMessageImages(DaraModel):
    def __init__(
        self,
        data_base_64: str = None,
        media_type: str = None,
    ):
        # This parameter is required.
        self.data_base_64 = data_base_64
        # This parameter is required.
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_base_64 is not None:
            result['dataBase64'] = self.data_base_64

        if self.media_type is not None:
            result['mediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataBase64') is not None:
            self.data_base_64 = m.get('dataBase64')

        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')

        return self

