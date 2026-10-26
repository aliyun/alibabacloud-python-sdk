# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class SendAgentConversationMessageRequest(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.SendAgentConversationMessageRequestAttachments] = None,
        client_context: str = None,
        images: List[main_models.SendAgentConversationMessageRequestImages] = None,
        message: str = None,
        message_type: str = None,
        ticket_request_id: str = None,
    ):
        self.attachments = attachments
        self.client_context = client_context
        self.images = images
        # This parameter is required.
        self.message = message
        self.message_type = message_type
        self.ticket_request_id = ticket_request_id

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['attachments'].append(k1.to_map() if k1 else None)

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
        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.SendAgentConversationMessageRequestAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('clientContext') is not None:
            self.client_context = m.get('clientContext')

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.SendAgentConversationMessageRequestImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('ticketRequestId') is not None:
            self.ticket_request_id = m.get('ticketRequestId')

        return self

class SendAgentConversationMessageRequestImages(DaraModel):
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

class SendAgentConversationMessageRequestAttachments(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        kept_lines: int = None,
        kind: str = None,
        sandbox_path: str = None,
        size_bytes: int = None,
        time_range_end: str = None,
        time_range_start: str = None,
        total_lines: int = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        self.kept_lines = kept_lines
        # This parameter is required.
        self.kind = kind
        # This parameter is required.
        self.sandbox_path = sandbox_path
        # This parameter is required.
        self.size_bytes = size_bytes
        self.time_range_end = time_range_end
        self.time_range_start = time_range_start
        self.total_lines = total_lines

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.kept_lines is not None:
            result['keptLines'] = self.kept_lines

        if self.kind is not None:
            result['kind'] = self.kind

        if self.sandbox_path is not None:
            result['sandboxPath'] = self.sandbox_path

        if self.size_bytes is not None:
            result['sizeBytes'] = self.size_bytes

        if self.time_range_end is not None:
            result['timeRangeEnd'] = self.time_range_end

        if self.time_range_start is not None:
            result['timeRangeStart'] = self.time_range_start

        if self.total_lines is not None:
            result['totalLines'] = self.total_lines

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('keptLines') is not None:
            self.kept_lines = m.get('keptLines')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('sandboxPath') is not None:
            self.sandbox_path = m.get('sandboxPath')

        if m.get('sizeBytes') is not None:
            self.size_bytes = m.get('sizeBytes')

        if m.get('timeRangeEnd') is not None:
            self.time_range_end = m.get('timeRangeEnd')

        if m.get('timeRangeStart') is not None:
            self.time_range_start = m.get('timeRangeStart')

        if m.get('totalLines') is not None:
            self.total_lines = m.get('totalLines')

        return self

