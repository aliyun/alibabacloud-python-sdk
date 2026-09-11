# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListAliDingGroupMessagesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListAliDingGroupMessagesResponseBodyItems] = None,
        message: str = None,
        next_time: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # Indicates whether more pages are available.
        self.has_more = has_more
        # The file information.
        self.items = items
        # The description of the status code.
        self.message = message
        # The time when the next plan is scheduled.
        self.next_time = next_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.next_time is not None:
            result['nextTime'] = self.next_time

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListAliDingGroupMessagesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListAliDingGroupMessagesResponseBodyItems(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.ListAliDingGroupMessagesResponseBodyItemsAttachments] = None,
        content: str = None,
        create_time: str = None,
        message_id: str = None,
        message_type: str = None,
        sender_id: str = None,
        sender_name: str = None,
    ):
        # The comment attachments.
        self.attachments = attachments
        # The returned content.
        self.content = content
        # The creation time in ISO 8601 format.
        self.create_time = create_time
        # The message ID.
        self.message_id = message_id
        # The message type. Valid values:
        # - **MARKDOWN**: Markdown message.
        # - **ACTIONCARD**: card message.
        # 
        # > Markdown messages do not support message buttons.
        self.message_type = message_type
        # The DingTalk ID of the business-side customer service representative.
        self.sender_id = sender_id
        # The name of the message sender.
        self.sender_name = sender_name

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
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

        if self.content is not None:
            result['content'] = self.content

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.sender_id is not None:
            result['senderId'] = self.sender_id

        if self.sender_name is not None:
            result['senderName'] = self.sender_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.ListAliDingGroupMessagesResponseBodyItemsAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('senderId') is not None:
            self.sender_id = m.get('senderId')

        if m.get('senderName') is not None:
            self.sender_name = m.get('senderName')

        return self

class ListAliDingGroupMessagesResponseBodyItemsAttachments(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        attachment_type: str = None,
        duration_ms: int = None,
        file_name: str = None,
        file_size: int = None,
        height: int = None,
        mime_type: str = None,
        width: int = None,
    ):
        # The attachment ID.
        self.attachment_id = attachment_id
        # The attachment type.
        self.attachment_type = attachment_type
        # The execution duration of the asynchronous task.
        self.duration_ms = duration_ms
        # The new file name. This parameter is optional. If you do not specify this parameter or set it to an empty string, the original file name is retained.
        self.file_name = file_name
        # The file size, in **bytes**.
        self.file_size = file_size
        # The thumbnail height, in pixels.
        self.height = height
        # The media type. The file name extension is in uppercase, such as XLS, DOC, DOCX, PDF, or XLSX.
        self.mime_type = mime_type
        # The image width, in pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_id is not None:
            result['attachmentId'] = self.attachment_id

        if self.attachment_type is not None:
            result['attachmentType'] = self.attachment_type

        if self.duration_ms is not None:
            result['durationMs'] = self.duration_ms

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.height is not None:
            result['height'] = self.height

        if self.mime_type is not None:
            result['mimeType'] = self.mime_type

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachmentId') is not None:
            self.attachment_id = m.get('attachmentId')

        if m.get('attachmentType') is not None:
            self.attachment_type = m.get('attachmentType')

        if m.get('durationMs') is not None:
            self.duration_ms = m.get('durationMs')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('mimeType') is not None:
            self.mime_type = m.get('mimeType')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

