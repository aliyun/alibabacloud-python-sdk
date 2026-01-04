# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectorResponseBody(DaraModel):
    def __init__(
        self,
        column_fields: str = None,
        config: str = None,
        connector_id: str = None,
        create_time: str = None,
        creator: str = None,
        done_time: str = None,
        project_name: str = None,
        request_id: str = None,
        state: str = None,
        subscription_id: str = None,
        success: bool = None,
        topic_name: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.column_fields = column_fields
        self.config = config
        self.connector_id = connector_id
        self.create_time = create_time
        self.creator = creator
        self.done_time = done_time
        self.project_name = project_name
        self.request_id = request_id
        self.state = state
        self.subscription_id = subscription_id
        self.success = success
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
        if self.column_fields is not None:
            result['ColumnFields'] = self.column_fields

        if self.config is not None:
            result['Config'] = self.config

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.done_time is not None:
            result['DoneTime'] = self.done_time

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        if self.subscription_id is not None:
            result['SubscriptionId'] = self.subscription_id

        if self.success is not None:
            result['Success'] = self.success

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnFields') is not None:
            self.column_fields = m.get('ColumnFields')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DoneTime') is not None:
            self.done_time = m.get('DoneTime')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SubscriptionId') is not None:
            self.subscription_id = m.get('SubscriptionId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

