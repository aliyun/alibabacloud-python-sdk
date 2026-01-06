# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetTicketResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: main_models.GetTicketResponseBodyCreator = None,
        custom_fields: str = None,
        open_conversation_id: str = None,
        open_ticket_id: str = None,
        processor: main_models.GetTicketResponseBodyProcessor = None,
        request_id: str = None,
        scene: str = None,
        scene_context: str = None,
        stage: str = None,
        takers: List[main_models.GetTicketResponseBodyTakers] = None,
        template: main_models.GetTicketResponseBodyTemplate = None,
        title: str = None,
        update_time: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.custom_fields = custom_fields
        self.open_conversation_id = open_conversation_id
        self.open_ticket_id = open_ticket_id
        self.processor = processor
        self.request_id = request_id
        self.scene = scene
        self.scene_context = scene_context
        self.stage = stage
        self.takers = takers
        self.template = template
        self.title = title
        self.update_time = update_time
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.processor:
            self.processor.validate()
        if self.takers:
            for v1 in self.takers:
                 if v1:
                    v1.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator is not None:
            result['creator'] = self.creator.to_map()

        if self.custom_fields is not None:
            result['customFields'] = self.custom_fields

        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id

        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id

        if self.processor is not None:
            result['processor'] = self.processor.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scene is not None:
            result['scene'] = self.scene

        if self.scene_context is not None:
            result['sceneContext'] = self.scene_context

        if self.stage is not None:
            result['stage'] = self.stage

        result['takers'] = []
        if self.takers is not None:
            for k1 in self.takers:
                result['takers'].append(k1.to_map() if k1 else None)

        if self.template is not None:
            result['template'] = self.template.to_map()

        if self.title is not None:
            result['title'] = self.title

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creator') is not None:
            temp_model = main_models.GetTicketResponseBodyCreator()
            self.creator = temp_model.from_map(m.get('creator'))

        if m.get('customFields') is not None:
            self.custom_fields = m.get('customFields')

        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')

        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')

        if m.get('processor') is not None:
            temp_model = main_models.GetTicketResponseBodyProcessor()
            self.processor = temp_model.from_map(m.get('processor'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('sceneContext') is not None:
            self.scene_context = m.get('sceneContext')

        if m.get('stage') is not None:
            self.stage = m.get('stage')

        self.takers = []
        if m.get('takers') is not None:
            for k1 in m.get('takers'):
                temp_model = main_models.GetTicketResponseBodyTakers()
                self.takers.append(temp_model.from_map(k1))

        if m.get('template') is not None:
            temp_model = main_models.GetTicketResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('template'))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetTicketResponseBodyTemplate(DaraModel):
    def __init__(
        self,
        open_template_biz_id: str = None,
        open_template_id: str = None,
        template_name: str = None,
    ):
        # OpenTemplateBizId
        self.open_template_biz_id = open_template_biz_id
        # OpenTemplateBizId
        self.open_template_id = open_template_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_template_biz_id is not None:
            result['OpenTemplateBizId'] = self.open_template_biz_id

        if self.open_template_id is not None:
            result['OpenTemplateId'] = self.open_template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenTemplateBizId') is not None:
            self.open_template_biz_id = m.get('OpenTemplateBizId')

        if m.get('OpenTemplateId') is not None:
            self.open_template_id = m.get('OpenTemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetTicketResponseBodyTakers(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.union_id is not None:
            result['UnionId'] = self.union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')

        return self

class GetTicketResponseBodyProcessor(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.union_id is not None:
            result['UnionId'] = self.union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')

        return self

class GetTicketResponseBodyCreator(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.union_id is not None:
            result['UnionId'] = self.union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')

        return self

