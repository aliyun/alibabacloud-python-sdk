# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_datahub20240620 import models as main_models
from darabonba.model import DaraModel

class ListSubscriptionsResponseBody(DaraModel):
    def __init__(
        self,
        list: main_models.ListSubscriptionsResponseBodyList = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.list = list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list is not None:
            result['List'] = self.list.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = main_models.ListSubscriptionsResponseBodyList()
            self.list = temp_model.from_map(m.get('List'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSubscriptionsResponseBodyList(DaraModel):
    def __init__(
        self,
        subscription: List[main_models.ListSubscriptionsResponseBodyListSubscription] = None,
    ):
        self.subscription = subscription

    def validate(self):
        if self.subscription:
            for v1 in self.subscription:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Subscription'] = []
        if self.subscription is not None:
            for k1 in self.subscription:
                result['Subscription'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription = []
        if m.get('Subscription') is not None:
            for k1 in m.get('Subscription'):
                temp_model = main_models.ListSubscriptionsResponseBodyListSubscription()
                self.subscription.append(temp_model.from_map(k1))

        return self

class ListSubscriptionsResponseBodyListSubscription(DaraModel):
    def __init__(
        self,
        application: str = None,
        comment: str = None,
        create_time: int = None,
        creator: str = None,
        project_name: str = None,
        state: int = None,
        subscription_id: str = None,
        topic_name: str = None,
        type: str = None,
        update_time: int = None,
    ):
        self.application = application
        self.comment = comment
        self.create_time = create_time
        self.creator = creator
        self.project_name = project_name
        self.state = state
        self.subscription_id = subscription_id
        self.topic_name = topic_name
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.state is not None:
            result['State'] = self.state

        if self.subscription_id is not None:
            result['SubscriptionId'] = self.subscription_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SubscriptionId') is not None:
            self.subscription_id = m.get('SubscriptionId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

