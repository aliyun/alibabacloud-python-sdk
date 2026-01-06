# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateRunResponseBody(DaraModel):
    def __init__(
        self,
        messages: List[main_models.CreateRunResponseBodyMessages] = None,
        request_id: str = None,
        run: main_models.CreateRunResponseBodyRun = None,
    ):
        self.messages = messages
        self.request_id = request_id
        self.run = run

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.run:
            self.run.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run is not None:
            result['run'] = self.run.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.CreateRunResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('run') is not None:
            temp_model = main_models.CreateRunResponseBodyRun()
            self.run = temp_model.from_map(m.get('run'))

        return self

class CreateRunResponseBodyRun(DaraModel):
    def __init__(
        self,
        cancelled_at: int = None,
        completed_at: int = None,
        create_at: int = None,
        expires_at: int = None,
        failed_at: int = None,
        id: str = None,
        last_error_msg: str = None,
        started_at: int = None,
        status: str = None,
        thread_id: str = None,
    ):
        self.cancelled_at = cancelled_at
        self.completed_at = completed_at
        self.create_at = create_at
        self.expires_at = expires_at
        self.failed_at = failed_at
        self.id = id
        self.last_error_msg = last_error_msg
        self.started_at = started_at
        self.status = status
        self.thread_id = thread_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled_at is not None:
            result['cancelledAt'] = self.cancelled_at

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.create_at is not None:
            result['createAt'] = self.create_at

        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.failed_at is not None:
            result['failedAt'] = self.failed_at

        if self.id is not None:
            result['id'] = self.id

        if self.last_error_msg is not None:
            result['lastErrorMsg'] = self.last_error_msg

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancelledAt') is not None:
            self.cancelled_at = m.get('cancelledAt')

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('createAt') is not None:
            self.create_at = m.get('createAt')

        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastErrorMsg') is not None:
            self.last_error_msg = m.get('lastErrorMsg')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        return self

class CreateRunResponseBodyMessages(DaraModel):
    def __init__(
        self,
        content: main_models.CreateRunResponseBodyMessagesContent = None,
        content_desc: str = None,
        content_struct: main_models.CreateRunResponseBodyMessagesContentStruct = None,
        create_at: int = None,
        id: str = None,
        role: str = None,
        run_id: str = None,
        thread_id: str = None,
    ):
        self.content = content
        self.content_desc = content_desc
        self.content_struct = content_struct
        self.create_at = create_at
        self.id = id
        self.role = role
        self.run_id = run_id
        self.thread_id = thread_id

    def validate(self):
        if self.content:
            self.content.validate()
        if self.content_struct:
            self.content_struct.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content.to_map()

        if self.content_desc is not None:
            result['contentDesc'] = self.content_desc

        if self.content_struct is not None:
            result['contentStruct'] = self.content_struct.to_map()

        if self.create_at is not None:
            result['createAt'] = self.create_at

        if self.id is not None:
            result['id'] = self.id

        if self.role is not None:
            result['role'] = self.role

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContent()
            self.content = temp_model.from_map(m.get('content'))

        if m.get('contentDesc') is not None:
            self.content_desc = m.get('contentDesc')

        if m.get('contentStruct') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStruct()
            self.content_struct = temp_model.from_map(m.get('contentStruct'))

        if m.get('createAt') is not None:
            self.create_at = m.get('createAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        return self

class CreateRunResponseBodyMessagesContentStruct(DaraModel):
    def __init__(
        self,
        parts: List[main_models.CreateRunResponseBodyMessagesContentStructParts] = None,
    ):
        self.parts = parts

    def validate(self):
        if self.parts:
            for v1 in self.parts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['parts'] = []
        if self.parts is not None:
            for k1 in self.parts:
                result['parts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parts = []
        if m.get('parts') is not None:
            for k1 in m.get('parts'):
                temp_model = main_models.CreateRunResponseBodyMessagesContentStructParts()
                self.parts.append(temp_model.from_map(k1))

        return self

class CreateRunResponseBodyMessagesContentStructParts(DaraModel):
    def __init__(
        self,
        append: bool = None,
        data_part: main_models.CreateRunResponseBodyMessagesContentStructPartsDataPart = None,
        finish: bool = None,
        part_desc: str = None,
        part_id: str = None,
        reason_part: main_models.CreateRunResponseBodyMessagesContentStructPartsReasonPart = None,
        recommend_part: main_models.CreateRunResponseBodyMessagesContentStructPartsRecommendPart = None,
        reference_part: main_models.CreateRunResponseBodyMessagesContentStructPartsReferencePart = None,
        text_part: main_models.CreateRunResponseBodyMessagesContentStructPartsTextPart = None,
        type: str = None,
    ):
        self.append = append
        self.data_part = data_part
        self.finish = finish
        self.part_desc = part_desc
        self.part_id = part_id
        self.reason_part = reason_part
        self.recommend_part = recommend_part
        self.reference_part = reference_part
        self.text_part = text_part
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.data_part:
            self.data_part.validate()
        if self.reason_part:
            self.reason_part.validate()
        if self.recommend_part:
            self.recommend_part.validate()
        if self.reference_part:
            self.reference_part.validate()
        if self.text_part:
            self.text_part.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.append is not None:
            result['append'] = self.append

        if self.data_part is not None:
            result['dataPart'] = self.data_part.to_map()

        if self.finish is not None:
            result['finish'] = self.finish

        if self.part_desc is not None:
            result['partDesc'] = self.part_desc

        if self.part_id is not None:
            result['partId'] = self.part_id

        if self.reason_part is not None:
            result['reasonPart'] = self.reason_part.to_map()

        if self.recommend_part is not None:
            result['recommendPart'] = self.recommend_part.to_map()

        if self.reference_part is not None:
            result['referencePart'] = self.reference_part.to_map()

        if self.text_part is not None:
            result['textPart'] = self.text_part.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('append') is not None:
            self.append = m.get('append')

        if m.get('dataPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructPartsDataPart()
            self.data_part = temp_model.from_map(m.get('dataPart'))

        if m.get('finish') is not None:
            self.finish = m.get('finish')

        if m.get('partDesc') is not None:
            self.part_desc = m.get('partDesc')

        if m.get('partId') is not None:
            self.part_id = m.get('partId')

        if m.get('reasonPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructPartsReasonPart()
            self.reason_part = temp_model.from_map(m.get('reasonPart'))

        if m.get('recommendPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructPartsRecommendPart()
            self.recommend_part = temp_model.from_map(m.get('recommendPart'))

        if m.get('referencePart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructPartsReferencePart()
            self.reference_part = temp_model.from_map(m.get('referencePart'))

        if m.get('textPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructPartsTextPart()
            self.text_part = temp_model.from_map(m.get('textPart'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateRunResponseBodyMessagesContentStructPartsTextPart(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class CreateRunResponseBodyMessagesContentStructPartsReferencePart(DaraModel):
    def __init__(
        self,
        references: List[main_models.CreateRunResponseBodyMessagesContentStructPartsReferencePartReferences] = None,
    ):
        self.references = references

    def validate(self):
        if self.references:
            for v1 in self.references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['references'] = []
        if self.references is not None:
            for k1 in self.references:
                result['references'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.references = []
        if m.get('references') is not None:
            for k1 in m.get('references'):
                temp_model = main_models.CreateRunResponseBodyMessagesContentStructPartsReferencePartReferences()
                self.references.append(temp_model.from_map(k1))

        return self

class CreateRunResponseBodyMessagesContentStructPartsReferencePartReferences(DaraModel):
    def __init__(
        self,
        index: str = None,
        name: str = None,
        source_code: str = None,
        source_icon: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.index = index
        self.name = name
        self.source_code = source_code
        self.source_icon = source_icon
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index

        if self.name is not None:
            result['name'] = self.name

        if self.source_code is not None:
            result['sourceCode'] = self.source_code

        if self.source_icon is not None:
            result['sourceIcon'] = self.source_icon

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceCode') is not None:
            self.source_code = m.get('sourceCode')

        if m.get('sourceIcon') is not None:
            self.source_icon = m.get('sourceIcon')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class CreateRunResponseBodyMessagesContentStructPartsRecommendPart(DaraModel):
    def __init__(
        self,
        recommends: List[main_models.CreateRunResponseBodyMessagesContentStructPartsRecommendPartRecommends] = None,
    ):
        self.recommends = recommends

    def validate(self):
        if self.recommends:
            for v1 in self.recommends:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['recommends'] = []
        if self.recommends is not None:
            for k1 in self.recommends:
                result['recommends'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recommends = []
        if m.get('recommends') is not None:
            for k1 in m.get('recommends'):
                temp_model = main_models.CreateRunResponseBodyMessagesContentStructPartsRecommendPartRecommends()
                self.recommends.append(temp_model.from_map(k1))

        return self

class CreateRunResponseBodyMessagesContentStructPartsRecommendPartRecommends(DaraModel):
    def __init__(
        self,
        mobile_url: str = None,
        text: str = None,
        url: str = None,
    ):
        self.mobile_url = mobile_url
        self.text = text
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url

        if self.text is not None:
            result['text'] = self.text

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class CreateRunResponseBodyMessagesContentStructPartsReasonPart(DaraModel):
    def __init__(
        self,
        reason: str = None,
    ):
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

class CreateRunResponseBodyMessagesContentStructPartsDataPart(DaraModel):
    def __init__(
        self,
        data: Any = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        return self

class CreateRunResponseBodyMessagesContent(DaraModel):
    def __init__(
        self,
        card_callback: main_models.CreateRunResponseBodyMessagesContentCardCallback = None,
        ding_card: main_models.CreateRunResponseBodyMessagesContentDingCard = None,
        ding_normal_card: main_models.CreateRunResponseBodyMessagesContentDingNormalCard = None,
        markdown: main_models.CreateRunResponseBodyMessagesContentMarkdown = None,
        struct_view: main_models.CreateRunResponseBodyMessagesContentStructView = None,
        text: main_models.CreateRunResponseBodyMessagesContentText = None,
        type: str = None,
    ):
        self.card_callback = card_callback
        self.ding_card = ding_card
        self.ding_normal_card = ding_normal_card
        self.markdown = markdown
        self.struct_view = struct_view
        self.text = text
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.card_callback:
            self.card_callback.validate()
        if self.ding_card:
            self.ding_card.validate()
        if self.ding_normal_card:
            self.ding_normal_card.validate()
        if self.markdown:
            self.markdown.validate()
        if self.struct_view:
            self.struct_view.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_callback is not None:
            result['cardCallback'] = self.card_callback.to_map()

        if self.ding_card is not None:
            result['dingCard'] = self.ding_card.to_map()

        if self.ding_normal_card is not None:
            result['dingNormalCard'] = self.ding_normal_card.to_map()

        if self.markdown is not None:
            result['markdown'] = self.markdown.to_map()

        if self.struct_view is not None:
            result['structView'] = self.struct_view.to_map()

        if self.text is not None:
            result['text'] = self.text.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardCallback') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentCardCallback()
            self.card_callback = temp_model.from_map(m.get('cardCallback'))

        if m.get('dingCard') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentDingCard()
            self.ding_card = temp_model.from_map(m.get('dingCard'))

        if m.get('dingNormalCard') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentDingNormalCard()
            self.ding_normal_card = temp_model.from_map(m.get('dingNormalCard'))

        if m.get('markdown') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentMarkdown()
            self.markdown = temp_model.from_map(m.get('markdown'))

        if m.get('structView') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructView()
            self.struct_view = temp_model.from_map(m.get('structView'))

        if m.get('text') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentText()
            self.text = temp_model.from_map(m.get('text'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateRunResponseBodyMessagesContentText(DaraModel):
    def __init__(
        self,
        value: str = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateRunResponseBodyMessagesContentStructView(DaraModel):
    def __init__(
        self,
        parts: List[main_models.CreateRunResponseBodyMessagesContentStructViewParts] = None,
    ):
        self.parts = parts

    def validate(self):
        if self.parts:
            for v1 in self.parts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['parts'] = []
        if self.parts is not None:
            for k1 in self.parts:
                result['parts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parts = []
        if m.get('parts') is not None:
            for k1 in m.get('parts'):
                temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewParts()
                self.parts.append(temp_model.from_map(k1))

        return self

class CreateRunResponseBodyMessagesContentStructViewParts(DaraModel):
    def __init__(
        self,
        append: bool = None,
        data_part: main_models.CreateRunResponseBodyMessagesContentStructViewPartsDataPart = None,
        finish: bool = None,
        part_desc: str = None,
        part_id: str = None,
        reason_part: main_models.CreateRunResponseBodyMessagesContentStructViewPartsReasonPart = None,
        recommend_part: main_models.CreateRunResponseBodyMessagesContentStructViewPartsRecommendPart = None,
        reference_part: main_models.CreateRunResponseBodyMessagesContentStructViewPartsReferencePart = None,
        text_part: main_models.CreateRunResponseBodyMessagesContentStructViewPartsTextPart = None,
        type: str = None,
    ):
        self.append = append
        self.data_part = data_part
        self.finish = finish
        self.part_desc = part_desc
        self.part_id = part_id
        self.reason_part = reason_part
        self.recommend_part = recommend_part
        self.reference_part = reference_part
        self.text_part = text_part
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.data_part:
            self.data_part.validate()
        if self.reason_part:
            self.reason_part.validate()
        if self.recommend_part:
            self.recommend_part.validate()
        if self.reference_part:
            self.reference_part.validate()
        if self.text_part:
            self.text_part.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.append is not None:
            result['append'] = self.append

        if self.data_part is not None:
            result['dataPart'] = self.data_part.to_map()

        if self.finish is not None:
            result['finish'] = self.finish

        if self.part_desc is not None:
            result['partDesc'] = self.part_desc

        if self.part_id is not None:
            result['partId'] = self.part_id

        if self.reason_part is not None:
            result['reasonPart'] = self.reason_part.to_map()

        if self.recommend_part is not None:
            result['recommendPart'] = self.recommend_part.to_map()

        if self.reference_part is not None:
            result['referencePart'] = self.reference_part.to_map()

        if self.text_part is not None:
            result['textPart'] = self.text_part.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('append') is not None:
            self.append = m.get('append')

        if m.get('dataPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewPartsDataPart()
            self.data_part = temp_model.from_map(m.get('dataPart'))

        if m.get('finish') is not None:
            self.finish = m.get('finish')

        if m.get('partDesc') is not None:
            self.part_desc = m.get('partDesc')

        if m.get('partId') is not None:
            self.part_id = m.get('partId')

        if m.get('reasonPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewPartsReasonPart()
            self.reason_part = temp_model.from_map(m.get('reasonPart'))

        if m.get('recommendPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewPartsRecommendPart()
            self.recommend_part = temp_model.from_map(m.get('recommendPart'))

        if m.get('referencePart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewPartsReferencePart()
            self.reference_part = temp_model.from_map(m.get('referencePart'))

        if m.get('textPart') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewPartsTextPart()
            self.text_part = temp_model.from_map(m.get('textPart'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateRunResponseBodyMessagesContentStructViewPartsTextPart(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class CreateRunResponseBodyMessagesContentStructViewPartsReferencePart(DaraModel):
    def __init__(
        self,
        references: List[main_models.CreateRunResponseBodyMessagesContentStructViewPartsReferencePartReferences] = None,
    ):
        self.references = references

    def validate(self):
        if self.references:
            for v1 in self.references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['references'] = []
        if self.references is not None:
            for k1 in self.references:
                result['references'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.references = []
        if m.get('references') is not None:
            for k1 in m.get('references'):
                temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewPartsReferencePartReferences()
                self.references.append(temp_model.from_map(k1))

        return self

class CreateRunResponseBodyMessagesContentStructViewPartsReferencePartReferences(DaraModel):
    def __init__(
        self,
        index: str = None,
        name: str = None,
        source_code: str = None,
        source_icon: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.index = index
        self.name = name
        self.source_code = source_code
        self.source_icon = source_icon
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index

        if self.name is not None:
            result['name'] = self.name

        if self.source_code is not None:
            result['sourceCode'] = self.source_code

        if self.source_icon is not None:
            result['sourceIcon'] = self.source_icon

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceCode') is not None:
            self.source_code = m.get('sourceCode')

        if m.get('sourceIcon') is not None:
            self.source_icon = m.get('sourceIcon')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class CreateRunResponseBodyMessagesContentStructViewPartsRecommendPart(DaraModel):
    def __init__(
        self,
        recommends: List[main_models.CreateRunResponseBodyMessagesContentStructViewPartsRecommendPartRecommends] = None,
    ):
        self.recommends = recommends

    def validate(self):
        if self.recommends:
            for v1 in self.recommends:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['recommends'] = []
        if self.recommends is not None:
            for k1 in self.recommends:
                result['recommends'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recommends = []
        if m.get('recommends') is not None:
            for k1 in m.get('recommends'):
                temp_model = main_models.CreateRunResponseBodyMessagesContentStructViewPartsRecommendPartRecommends()
                self.recommends.append(temp_model.from_map(k1))

        return self

class CreateRunResponseBodyMessagesContentStructViewPartsRecommendPartRecommends(DaraModel):
    def __init__(
        self,
        mobile_url: str = None,
        text: str = None,
        url: str = None,
    ):
        self.mobile_url = mobile_url
        self.text = text
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url

        if self.text is not None:
            result['text'] = self.text

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class CreateRunResponseBodyMessagesContentStructViewPartsReasonPart(DaraModel):
    def __init__(
        self,
        reason: str = None,
    ):
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

class CreateRunResponseBodyMessagesContentStructViewPartsDataPart(DaraModel):
    def __init__(
        self,
        data: Any = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        return self

class CreateRunResponseBodyMessagesContentMarkdown(DaraModel):
    def __init__(
        self,
        value: str = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateRunResponseBodyMessagesContentDingNormalCard(DaraModel):
    def __init__(
        self,
        card_data: main_models.CreateRunResponseBodyMessagesContentDingNormalCardCardData = None,
        card_template_id: str = None,
        card_update_options: main_models.CreateRunResponseBodyMessagesContentDingNormalCardCardUpdateOptions = None,
        dynamic_data_source_configs: List[main_models.CreateRunResponseBodyMessagesContentDingNormalCardDynamicDataSourceConfigs] = None,
        private_data: Dict[str, dict] = None,
    ):
        self.card_data = card_data
        self.card_template_id = card_template_id
        self.card_update_options = card_update_options
        self.dynamic_data_source_configs = dynamic_data_source_configs
        self.private_data = private_data

    def validate(self):
        if self.card_data:
            self.card_data.validate()
        if self.card_update_options:
            self.card_update_options.validate()
        if self.dynamic_data_source_configs:
            for v1 in self.dynamic_data_source_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_data is not None:
            result['cardData'] = self.card_data.to_map()

        if self.card_template_id is not None:
            result['cardTemplateId'] = self.card_template_id

        if self.card_update_options is not None:
            result['cardUpdateOptions'] = self.card_update_options.to_map()

        result['dynamicDataSourceConfigs'] = []
        if self.dynamic_data_source_configs is not None:
            for k1 in self.dynamic_data_source_configs:
                result['dynamicDataSourceConfigs'].append(k1.to_map() if k1 else None)

        if self.private_data is not None:
            result['privateData'] = self.private_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardData') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentDingNormalCardCardData()
            self.card_data = temp_model.from_map(m.get('cardData'))

        if m.get('cardTemplateId') is not None:
            self.card_template_id = m.get('cardTemplateId')

        if m.get('cardUpdateOptions') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentDingNormalCardCardUpdateOptions()
            self.card_update_options = temp_model.from_map(m.get('cardUpdateOptions'))

        self.dynamic_data_source_configs = []
        if m.get('dynamicDataSourceConfigs') is not None:
            for k1 in m.get('dynamicDataSourceConfigs'):
                temp_model = main_models.CreateRunResponseBodyMessagesContentDingNormalCardDynamicDataSourceConfigs()
                self.dynamic_data_source_configs.append(temp_model.from_map(k1))

        if m.get('privateData') is not None:
            self.private_data = m.get('privateData')

        return self

class CreateRunResponseBodyMessagesContentDingNormalCardDynamicDataSourceConfigs(DaraModel):
    def __init__(
        self,
        const_params: Dict[str, Any] = None,
        dynamic_data_source_id: str = None,
        pull_config: main_models.CreateRunResponseBodyMessagesContentDingNormalCardDynamicDataSourceConfigsPullConfig = None,
    ):
        self.const_params = const_params
        self.dynamic_data_source_id = dynamic_data_source_id
        self.pull_config = pull_config

    def validate(self):
        if self.pull_config:
            self.pull_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.const_params is not None:
            result['constParams'] = self.const_params

        if self.dynamic_data_source_id is not None:
            result['dynamicDataSourceId'] = self.dynamic_data_source_id

        if self.pull_config is not None:
            result['pullConfig'] = self.pull_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('constParams') is not None:
            self.const_params = m.get('constParams')

        if m.get('dynamicDataSourceId') is not None:
            self.dynamic_data_source_id = m.get('dynamicDataSourceId')

        if m.get('pullConfig') is not None:
            temp_model = main_models.CreateRunResponseBodyMessagesContentDingNormalCardDynamicDataSourceConfigsPullConfig()
            self.pull_config = temp_model.from_map(m.get('pullConfig'))

        return self

class CreateRunResponseBodyMessagesContentDingNormalCardDynamicDataSourceConfigsPullConfig(DaraModel):
    def __init__(
        self,
        interval: int = None,
        pull_strategy: str = None,
        time_unit: str = None,
    ):
        self.interval = interval
        self.pull_strategy = pull_strategy
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['interval'] = self.interval

        if self.pull_strategy is not None:
            result['pullStrategy'] = self.pull_strategy

        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('pullStrategy') is not None:
            self.pull_strategy = m.get('pullStrategy')

        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')

        return self

class CreateRunResponseBodyMessagesContentDingNormalCardCardUpdateOptions(DaraModel):
    def __init__(
        self,
        update_card_data_by_key: bool = None,
        update_private_data_by_key: bool = None,
    ):
        self.update_card_data_by_key = update_card_data_by_key
        self.update_private_data_by_key = update_private_data_by_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.update_card_data_by_key is not None:
            result['updateCardDataByKey'] = self.update_card_data_by_key

        if self.update_private_data_by_key is not None:
            result['updatePrivateDataByKey'] = self.update_private_data_by_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('updateCardDataByKey') is not None:
            self.update_card_data_by_key = m.get('updateCardDataByKey')

        if m.get('updatePrivateDataByKey') is not None:
            self.update_private_data_by_key = m.get('updatePrivateDataByKey')

        return self

class CreateRunResponseBodyMessagesContentDingNormalCardCardData(DaraModel):
    def __init__(
        self,
        card_param_map: Any = None,
    ):
        self.card_param_map = card_param_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_param_map is not None:
            result['cardParamMap'] = self.card_param_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardParamMap') is not None:
            self.card_param_map = m.get('cardParamMap')

        return self

class CreateRunResponseBodyMessagesContentDingCard(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        finished: bool = None,
        template_id: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.content_type = content_type
        self.finished = finished
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.finished is not None:
            result['finished'] = self.finished

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('finished') is not None:
            self.finished = m.get('finished')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

class CreateRunResponseBodyMessagesContentCardCallback(DaraModel):
    def __init__(
        self,
        content: str = None,
        related_message_id: str = None,
    ):
        self.content = content
        self.related_message_id = related_message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.related_message_id is not None:
            result['relatedMessageId'] = self.related_message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('relatedMessageId') is not None:
            self.related_message_id = m.get('relatedMessageId')

        return self

