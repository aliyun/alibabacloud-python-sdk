# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class CreateQualityCheckTaskRequest(DaraModel):
    def __init__(
        self,
        conversation_list: main_models.CreateQualityCheckTaskRequestConversationList = None,
        gmt_service: str = None,
        meta_data: Dict[str, str] = None,
        quality_group: List[str] = None,
        request_id: str = None,
        scene_code: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.conversation_list = conversation_list
        # This parameter is required.
        self.gmt_service = gmt_service
        self.meta_data = meta_data
        self.quality_group = quality_group
        # This parameter is required.
        self.request_id = request_id
        self.scene_code = scene_code
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.conversation_list:
            self.conversation_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_list is not None:
            result['conversationList'] = self.conversation_list.to_map()

        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service

        if self.meta_data is not None:
            result['metaData'] = self.meta_data

        if self.quality_group is not None:
            result['qualityGroup'] = self.quality_group

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scene_code is not None:
            result['sceneCode'] = self.scene_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationList') is not None:
            temp_model = main_models.CreateQualityCheckTaskRequestConversationList()
            self.conversation_list = temp_model.from_map(m.get('conversationList'))

        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')

        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')

        if m.get('qualityGroup') is not None:
            self.quality_group = m.get('qualityGroup')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sceneCode') is not None:
            self.scene_code = m.get('sceneCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateQualityCheckTaskRequestConversationList(DaraModel):
    def __init__(
        self,
        call_type: str = None,
        customer_id: str = None,
        customer_name: str = None,
        customer_service_id: str = None,
        customer_service_name: str = None,
        dialogue_list: List[main_models.CreateQualityCheckTaskRequestConversationListDialogueList] = None,
        gmt_service: str = None,
    ):
        self.call_type = call_type
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_service_id = customer_service_id
        self.customer_service_name = customer_service_name
        # This parameter is required.
        self.dialogue_list = dialogue_list
        self.gmt_service = gmt_service

    def validate(self):
        if self.dialogue_list:
            for v1 in self.dialogue_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_type is not None:
            result['callType'] = self.call_type

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_name is not None:
            result['customerName'] = self.customer_name

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_name is not None:
            result['customerServiceName'] = self.customer_service_name

        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['dialogueList'].append(k1.to_map() if k1 else None)

        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callType') is not None:
            self.call_type = m.get('callType')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceName') is not None:
            self.customer_service_name = m.get('customerServiceName')

        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k1 in m.get('dialogueList'):
                temp_model = main_models.CreateQualityCheckTaskRequestConversationListDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')

        return self

class CreateQualityCheckTaskRequestConversationListDialogueList(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        role: str = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        # This parameter is required.
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        # This parameter is required.
        self.role = role
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['begin'] = self.begin

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.content is not None:
            result['content'] = self.content

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type

        if self.end is not None:
            result['end'] = self.end

        if self.role is not None:
            result['role'] = self.role

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

