# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListChatMessageContentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListChatMessageContentsResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        source_id: str = None,
        total: int = None,
    ):
        # The status code.
        self.code = code
        # Specifies whether there is a next page.
        self.has_more = has_more
        # The list of MCP cards.
        self.items = items
        # The description of the status code.
        self.message = message
        # The current page number.
        self.page = page
        # The maximum number of data records returned in this request.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The ID of the original project.
        self.source_id = source_id
        # The total number of records.
        self.total = total

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

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.total is not None:
            result['total'] = self.total

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
                temp_model = main_models.ListChatMessageContentsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListChatMessageContentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.ListChatMessageContentsResponseBodyItemsAttachments] = None,
        message_id: str = None,
        message_type: str = None,
        record_id: int = None,
        sender_id: str = None,
        sender_name: str = None,
        sent_at: str = None,
        text: str = None,
    ):
        # The content type. Valid values:
        # - 0: Text.
        # - 1: Image material.
        # - 2: Handwritten text.
        self.attachments = attachments
        # The ID of the message.
        self.message_id = message_id
        # The message type. Valid values:
        # - **MARKDOWN**: Markdown message.
        # - **ACTIONCARD**: Card message.
        # 
        # > Message buttons cannot be used in Markdown messages.
        self.message_type = message_type
        # The ID of the service record.
        self.record_id = record_id
        # The DingTalk ID of the customer service representative.
        self.sender_id = sender_id
        # The name of the message sender.
        self.sender_name = sender_name
        # The time when the message was sent.
        self.sent_at = sent_at
        # The batch text to be translated.
        self.text = text

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

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.record_id is not None:
            result['recordId'] = self.record_id

        if self.sender_id is not None:
            result['senderId'] = self.sender_id

        if self.sender_name is not None:
            result['senderName'] = self.sender_name

        if self.sent_at is not None:
            result['sentAt'] = self.sent_at

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.ListChatMessageContentsResponseBodyItemsAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')

        if m.get('senderId') is not None:
            self.sender_id = m.get('senderId')

        if m.get('senderName') is not None:
            self.sender_name = m.get('senderName')

        if m.get('sentAt') is not None:
            self.sent_at = m.get('sentAt')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class ListChatMessageContentsResponseBodyItemsAttachments(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        char_count: int = None,
        chunk_count: int = None,
        content: str = None,
        empty_reason: str = None,
        failure_code: str = None,
        failure_reason: str = None,
        file_name: str = None,
        found: bool = None,
        message_id: str = None,
        modality: str = None,
        status: str = None,
        truncated: bool = None,
    ):
        # The ID of the attachment.
        self.attachment_id = attachment_id
        # The total number of characters in the content.
        self.char_count = char_count
        # The number of chunks.
        self.chunk_count = chunk_count
        # The content of the user message.
        self.content = content
        # The reason why the content is empty.
        self.empty_reason = empty_reason
        # The failure code of the batch. Valid values:
        # - ARREARAGE: The account has an overdue payment.
        # - NO_TARGET: No valid inspection instance is available.
        # - TIMEOUT: The batch execution timed out.
        # - SYSTEM_ERROR: A system error occurred.
        # - ALL_INSTANCE_FAILED: All instance inspections failed.
        # 
        # This parameter is empty if the batch does not fail.
        self.failure_code = failure_code
        # The failure summary of the asynchronous task. This parameter is not returned if no failure information is available. You can use the taskId and requestId to troubleshoot the issue.
        self.failure_reason = failure_reason
        # The new file name. This parameter is optional. If you do not specify this parameter or specify an empty string, the original file name is retained.
        self.file_name = file_name
        # Specifies whether the standard package instance is found.
        self.found = found
        # The ID of the message.
        self.message_id = message_id
        # The type of the attachment.
        self.modality = modality
        # The status of the data source. Valid values:
        # - **1**: Online.
        # - **0**: Offline.
        self.status = status
        # Specifies whether the scan result is truncated.
        self.truncated = truncated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_id is not None:
            result['attachmentId'] = self.attachment_id

        if self.char_count is not None:
            result['charCount'] = self.char_count

        if self.chunk_count is not None:
            result['chunkCount'] = self.chunk_count

        if self.content is not None:
            result['content'] = self.content

        if self.empty_reason is not None:
            result['emptyReason'] = self.empty_reason

        if self.failure_code is not None:
            result['failureCode'] = self.failure_code

        if self.failure_reason is not None:
            result['failureReason'] = self.failure_reason

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.found is not None:
            result['found'] = self.found

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.modality is not None:
            result['modality'] = self.modality

        if self.status is not None:
            result['status'] = self.status

        if self.truncated is not None:
            result['truncated'] = self.truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachmentId') is not None:
            self.attachment_id = m.get('attachmentId')

        if m.get('charCount') is not None:
            self.char_count = m.get('charCount')

        if m.get('chunkCount') is not None:
            self.chunk_count = m.get('chunkCount')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('emptyReason') is not None:
            self.empty_reason = m.get('emptyReason')

        if m.get('failureCode') is not None:
            self.failure_code = m.get('failureCode')

        if m.get('failureReason') is not None:
            self.failure_reason = m.get('failureReason')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('found') is not None:
            self.found = m.get('found')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('modality') is not None:
            self.modality = m.get('modality')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('truncated') is not None:
            self.truncated = m.get('truncated')

        return self

