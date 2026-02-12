# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsDLQMessagePageQueryByGroupIdResponseBody(DaraModel):
    def __init__(
        self,
        msg_found_do: main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo = None,
        request_id: str = None,
    ):
        # The information about dead-letter messages that are queried.
        self.msg_found_do = msg_found_do
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.msg_found_do:
            self.msg_found_do.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg_found_do is not None:
            result['MsgFoundDo'] = self.msg_found_do.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgFoundDo') is not None:
            temp_model = main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo()
            self.msg_found_do = temp_model.from_map(m.get('MsgFoundDo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        max_page_count: int = None,
        msg_found_list: main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList = None,
        task_id: str = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The total number of returned pages.
        self.max_page_count = max_page_count
        self.msg_found_list = msg_found_list
        # The ID of the query task. The first time you call this operation to query the dead-letter messages that are sent to a specified consumer group within a specified time range, this parameter is returned. You can use the task ID to query the details of dead-letter messages on other returned pages.
        self.task_id = task_id

    def validate(self):
        if self.msg_found_list:
            self.msg_found_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.max_page_count is not None:
            result['MaxPageCount'] = self.max_page_count

        if self.msg_found_list is not None:
            result['MsgFoundList'] = self.msg_found_list.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MaxPageCount') is not None:
            self.max_page_count = m.get('MaxPageCount')

        if m.get('MsgFoundList') is not None:
            temp_model = main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList()
            self.msg_found_list = temp_model.from_map(m.get('MsgFoundList'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList(DaraModel):
    def __init__(
        self,
        ons_rest_message_do: List[main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo] = None,
    ):
        self.ons_rest_message_do = ons_rest_message_do

    def validate(self):
        if self.ons_rest_message_do:
            for v1 in self.ons_rest_message_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OnsRestMessageDo'] = []
        if self.ons_rest_message_do is not None:
            for k1 in self.ons_rest_message_do:
                result['OnsRestMessageDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ons_rest_message_do = []
        if m.get('OnsRestMessageDo') is not None:
            for k1 in m.get('OnsRestMessageDo'):
                temp_model = main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo()
                self.ons_rest_message_do.append(temp_model.from_map(k1))

        return self

class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo(DaraModel):
    def __init__(
        self,
        body_crc: int = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        self.body_crc = body_crc
        self.born_host = born_host
        self.born_timestamp = born_timestamp
        self.instance_id = instance_id
        self.msg_id = msg_id
        self.property_list = property_list
        self.reconsume_times = reconsume_times
        self.store_host = store_host
        self.store_size = store_size
        self.store_timestamp = store_timestamp
        self.topic = topic

    def validate(self):
        if self.property_list:
            self.property_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc

        if self.born_host is not None:
            result['BornHost'] = self.born_host

        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.property_list is not None:
            result['PropertyList'] = self.property_list.to_map()

        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times

        if self.store_host is not None:
            result['StoreHost'] = self.store_host

        if self.store_size is not None:
            result['StoreSize'] = self.store_size

        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')

        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')

        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('PropertyList') is not None:
            temp_model = main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList()
            self.property_list = temp_model.from_map(m.get('PropertyList'))

        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')

        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')

        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')

        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList(DaraModel):
    def __init__(
        self,
        message_property: List[main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty] = None,
    ):
        self.message_property = message_property

    def validate(self):
        if self.message_property:
            for v1 in self.message_property:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MessageProperty'] = []
        if self.message_property is not None:
            for k1 in self.message_property:
                result['MessageProperty'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_property = []
        if m.get('MessageProperty') is not None:
            for k1 in m.get('MessageProperty'):
                temp_model = main_models.OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty()
                self.message_property.append(temp_model.from_map(k1))

        return self

class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

