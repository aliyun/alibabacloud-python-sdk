# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class GetSubscriptionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSubscriptionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSubscriptionResponseBodyData(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        endpoint: str = None,
        event_list: List[main_models.GetSubscriptionResponseBodyDataEventList] = None,
        instance_id: str = None,
        mq_instance_id: str = None,
        mq_type: str = None,
        password: str = None,
        producer_id: str = None,
        topic: str = None,
        user_name: str = None,
    ):
        self.disabled = disabled
        self.endpoint = endpoint
        self.event_list = event_list
        self.instance_id = instance_id
        self.mq_instance_id = mq_instance_id
        self.mq_type = mq_type
        self.password = password
        self.producer_id = producer_id
        self.topic = topic
        self.user_name = user_name

    def validate(self):
        if self.event_list:
            for v1 in self.event_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mq_instance_id is not None:
            result['MqInstanceId'] = self.mq_instance_id

        if self.mq_type is not None:
            result['MqType'] = self.mq_type

        if self.password is not None:
            result['Password'] = self.password

        if self.producer_id is not None:
            result['ProducerId'] = self.producer_id

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.GetSubscriptionResponseBodyDataEventList()
                self.event_list.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MqInstanceId') is not None:
            self.mq_instance_id = m.get('MqInstanceId')

        if m.get('MqType') is not None:
            self.mq_type = m.get('MqType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProducerId') is not None:
            self.producer_id = m.get('ProducerId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class GetSubscriptionResponseBodyDataEventList(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        display_name: str = None,
        name: str = None,
    ):
        self.disabled = disabled
        self.display_name = display_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

