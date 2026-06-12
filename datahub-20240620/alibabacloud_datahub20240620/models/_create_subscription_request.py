# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSubscriptionRequest(DaraModel):
    def __init__(
        self,
        application: str = None,
        comment: str = None,
        project_name: str = None,
        subscription_id: str = None,
        topic_name: str = None,
    ):
        # This parameter is required.
        self.application = application
        # This parameter is required.
        self.comment = comment
        # This parameter is required.
        self.project_name = project_name
        self.subscription_id = subscription_id
        # This parameter is required.
        self.topic_name = topic_name

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

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.subscription_id is not None:
            result['SubscriptionId'] = self.subscription_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SubscriptionId') is not None:
            self.subscription_id = m.get('SubscriptionId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

