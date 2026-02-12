# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsTopicSubDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsTopicSubDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsTopicSubDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsTopicSubDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        subscription_data_list: main_models.OnsTopicSubDetailResponseBodyDataSubscriptionDataList = None,
        topic: str = None,
    ):
        self.subscription_data_list = subscription_data_list
        # The topic name.
        self.topic = topic

    def validate(self):
        if self.subscription_data_list:
            self.subscription_data_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subscription_data_list is not None:
            result['SubscriptionDataList'] = self.subscription_data_list.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscriptionDataList') is not None:
            temp_model = main_models.OnsTopicSubDetailResponseBodyDataSubscriptionDataList()
            self.subscription_data_list = temp_model.from_map(m.get('SubscriptionDataList'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class OnsTopicSubDetailResponseBodyDataSubscriptionDataList(DaraModel):
    def __init__(
        self,
        subscription_data_list: List[main_models.OnsTopicSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList] = None,
    ):
        self.subscription_data_list = subscription_data_list

    def validate(self):
        if self.subscription_data_list:
            for v1 in self.subscription_data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubscriptionDataList'] = []
        if self.subscription_data_list is not None:
            for k1 in self.subscription_data_list:
                result['SubscriptionDataList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_data_list = []
        if m.get('SubscriptionDataList') is not None:
            for k1 in m.get('SubscriptionDataList'):
                temp_model = main_models.OnsTopicSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList()
                self.subscription_data_list.append(temp_model.from_map(k1))

        return self

class OnsTopicSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        message_model: str = None,
        online: str = None,
        sub_string: str = None,
    ):
        self.group_id = group_id
        self.message_model = message_model
        self.online = online
        self.sub_string = sub_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.message_model is not None:
            result['MessageModel'] = self.message_model

        if self.online is not None:
            result['Online'] = self.online

        if self.sub_string is not None:
            result['SubString'] = self.sub_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MessageModel') is not None:
            self.message_model = m.get('MessageModel')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('SubString') is not None:
            self.sub_string = m.get('SubString')

        return self

