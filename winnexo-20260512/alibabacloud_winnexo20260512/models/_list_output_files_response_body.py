# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListOutputFilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListOutputFilesResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response status code.
        self.code = code
        # The output list.
        self.items = items
        # The prompt message.
        self.message = message
        # The current page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The request trace ID.
        self.request_id = request_id
        # The total number of outputs that match the specified conditions.
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

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListOutputFilesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListOutputFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        operating_object_name: str = None,
        output_id: str = None,
        output_items: List[main_models.ListOutputFilesResponseBodyItemsOutputItems] = None,
        output_type: str = None,
        output_type_display_name: str = None,
        skill_output_id: str = None,
        task_id: str = None,
    ):
        # The conversation ID.
        self.conversation_id = conversation_id
        # The creation time in ISO 8601 format.
        self.gmt_create = gmt_create
        # The update time in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # The output name.
        self.name = name
        # The name of the digital employee (operating object).
        self.operating_object_name = operating_object_name
        # The output ID.
        self.output_id = output_id
        # The output detail list.
        self.output_items = output_items
        # The output type: `conversation/skill/task`.
        self.output_type = output_type
        # The internationalized display name of the output type.
        self.output_type_display_name = output_type_display_name
        # The skill output ID.
        self.skill_output_id = skill_output_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.output_items:
            for v1 in self.output_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.output_id is not None:
            result['outputId'] = self.output_id

        result['outputItems'] = []
        if self.output_items is not None:
            for k1 in self.output_items:
                result['outputItems'].append(k1.to_map() if k1 else None)

        if self.output_type is not None:
            result['outputType'] = self.output_type

        if self.output_type_display_name is not None:
            result['outputTypeDisplayName'] = self.output_type_display_name

        if self.skill_output_id is not None:
            result['skillOutputId'] = self.skill_output_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('outputId') is not None:
            self.output_id = m.get('outputId')

        self.output_items = []
        if m.get('outputItems') is not None:
            for k1 in m.get('outputItems'):
                temp_model = main_models.ListOutputFilesResponseBodyItemsOutputItems()
                self.output_items.append(temp_model.from_map(k1))

        if m.get('outputType') is not None:
            self.output_type = m.get('outputType')

        if m.get('outputTypeDisplayName') is not None:
            self.output_type_display_name = m.get('outputTypeDisplayName')

        if m.get('skillOutputId') is not None:
            self.skill_output_id = m.get('skillOutputId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class ListOutputFilesResponseBodyItemsOutputItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        email_info: main_models.ListOutputFilesResponseBodyItemsOutputItemsEmailInfo = None,
        file_info: main_models.ListOutputFilesResponseBodyItemsOutputItemsFileInfo = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        item_name: str = None,
        item_type: str = None,
        item_type_display_name: str = None,
        message_id: str = None,
        output_item_id: str = None,
        share_enabled: bool = None,
        share_token: str = None,
        skill_output_id: str = None,
        slides_info: main_models.ListOutputFilesResponseBodyItemsOutputItemsSlidesInfo = None,
        task_execution_id: str = None,
    ):
        # The creation time in ISO 8601 format.
        self.create_time = create_time
        # The email information. This field is present when the output type is email.
        self.email_info = email_info
        # The file information. This field is present when the output type is file.
        self.file_info = file_info
        # The database creation time in ISO 8601 format.
        self.gmt_create = gmt_create
        # The database update time in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # The output name.
        self.item_name = item_name
        # The type of the output item. Valid values: ppt, html, document, picture, slides, video, audio, email, and others.
        self.item_type = item_type
        # The internationalized display name of the output detail type.
        self.item_type_display_name = item_type_display_name
        # The message ID.
        self.message_id = message_id
        # The output detail ID.
        self.output_item_id = output_item_id
        # Indicates whether sharing is enabled.
        self.share_enabled = share_enabled
        # The share token, which is present when sharing is enabled. You can use this token to access the public share preview API.
        self.share_token = share_token
        # The skill output ID.
        self.skill_output_id = skill_output_id
        # The slides information. This field is present when the output type is slides.
        self.slides_info = slides_info
        # The task execution ID.
        self.task_execution_id = task_execution_id

    def validate(self):
        if self.email_info:
            self.email_info.validate()
        if self.file_info:
            self.file_info.validate()
        if self.slides_info:
            self.slides_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.email_info is not None:
            result['emailInfo'] = self.email_info.to_map()

        if self.file_info is not None:
            result['fileInfo'] = self.file_info.to_map()

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.item_name is not None:
            result['itemName'] = self.item_name

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.item_type_display_name is not None:
            result['itemTypeDisplayName'] = self.item_type_display_name

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.output_item_id is not None:
            result['outputItemId'] = self.output_item_id

        if self.share_enabled is not None:
            result['shareEnabled'] = self.share_enabled

        if self.share_token is not None:
            result['shareToken'] = self.share_token

        if self.skill_output_id is not None:
            result['skillOutputId'] = self.skill_output_id

        if self.slides_info is not None:
            result['slidesInfo'] = self.slides_info.to_map()

        if self.task_execution_id is not None:
            result['taskExecutionId'] = self.task_execution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('emailInfo') is not None:
            temp_model = main_models.ListOutputFilesResponseBodyItemsOutputItemsEmailInfo()
            self.email_info = temp_model.from_map(m.get('emailInfo'))

        if m.get('fileInfo') is not None:
            temp_model = main_models.ListOutputFilesResponseBodyItemsOutputItemsFileInfo()
            self.file_info = temp_model.from_map(m.get('fileInfo'))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('itemTypeDisplayName') is not None:
            self.item_type_display_name = m.get('itemTypeDisplayName')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('outputItemId') is not None:
            self.output_item_id = m.get('outputItemId')

        if m.get('shareEnabled') is not None:
            self.share_enabled = m.get('shareEnabled')

        if m.get('shareToken') is not None:
            self.share_token = m.get('shareToken')

        if m.get('skillOutputId') is not None:
            self.skill_output_id = m.get('skillOutputId')

        if m.get('slidesInfo') is not None:
            temp_model = main_models.ListOutputFilesResponseBodyItemsOutputItemsSlidesInfo()
            self.slides_info = temp_model.from_map(m.get('slidesInfo'))

        if m.get('taskExecutionId') is not None:
            self.task_execution_id = m.get('taskExecutionId')

        return self

class ListOutputFilesResponseBodyItemsOutputItemsSlidesInfo(DaraModel):
    def __init__(
        self,
        completed_slides: int = None,
        ppt_id: str = None,
        ppt_name: str = None,
        total_slides: int = None,
    ):
        # The number of completed slides.
        self.completed_slides = completed_slides
        # PPT ID
        self.ppt_id = ppt_id
        # The PPT name.
        self.ppt_name = ppt_name
        # The total number of slides.
        self.total_slides = total_slides

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_slides is not None:
            result['completedSlides'] = self.completed_slides

        if self.ppt_id is not None:
            result['pptId'] = self.ppt_id

        if self.ppt_name is not None:
            result['pptName'] = self.ppt_name

        if self.total_slides is not None:
            result['totalSlides'] = self.total_slides

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedSlides') is not None:
            self.completed_slides = m.get('completedSlides')

        if m.get('pptId') is not None:
            self.ppt_id = m.get('pptId')

        if m.get('pptName') is not None:
            self.ppt_name = m.get('pptName')

        if m.get('totalSlides') is not None:
            self.total_slides = m.get('totalSlides')

        return self

class ListOutputFilesResponseBodyItemsOutputItemsFileInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        path: str = None,
        type: str = None,
    ):
        # The file description.
        self.description = description
        # The file name.
        self.name = name
        # The file path (OSS object key).
        self.path = path
        # The file type, such as .pdf or .md.
        self.type = type

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

        if self.path is not None:
            result['path'] = self.path

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListOutputFilesResponseBodyItemsOutputItemsEmailInfo(DaraModel):
    def __init__(
        self,
        body: str = None,
        content_type: str = None,
        recipients: List[str] = None,
        subject: str = None,
    ):
        # The email body.
        self.body = body
        # The content type, such as MARKDOWN/JSONML/HTML.
        self.content_type = content_type
        # The recipient list.
        self.recipients = recipients
        # The email subject.
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.recipients is not None:
            result['recipients'] = self.recipients

        if self.subject is not None:
            result['subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('recipients') is not None:
            self.recipients = m.get('recipients')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        return self

