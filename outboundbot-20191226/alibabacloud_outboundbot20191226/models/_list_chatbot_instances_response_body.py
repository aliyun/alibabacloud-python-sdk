# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListChatbotInstancesResponseBody(DaraModel):
    def __init__(
        self,
        bots: List[main_models.ListChatbotInstancesResponseBodyBots] = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.bots = bots
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.bots:
            for v1 in self.bots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bots'] = []
        if self.bots is not None:
            for k1 in self.bots:
                result['Bots'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bots = []
        if m.get('Bots') is not None:
            for k1 in m.get('Bots'):
                temp_model = main_models.ListChatbotInstancesResponseBodyBots()
                self.bots.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListChatbotInstancesResponseBodyBots(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        create_time: str = None,
        instance_id: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        time_zone: str = None,
    ):
        self.avatar = avatar
        self.create_time = create_time
        self.instance_id = instance_id
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.language_code is not None:
            result['LanguageCode'] = self.language_code

        if self.name is not None:
            result['Name'] = self.name

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

