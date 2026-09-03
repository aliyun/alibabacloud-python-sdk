# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.model import DaraModel

class Aps(DaraModel):
    def __init__(
        self,
        alert: main_models.Alert = None,
        attributes: str = None,
        attributes_type: str = None,
        badge: str = None,
        category: str = None,
        content_available: int = None,
        content_state: str = None,
        dismissal_date: int = None,
        event: str = None,
        interruption_level: str = None,
        mutable_content: int = None,
        sound: str = None,
        thread_id: str = None,
        timestamp: int = None,
    ):
        self.alert = alert
        self.attributes = attributes
        self.attributes_type = attributes_type
        self.badge = badge
        self.category = category
        self.content_available = content_available
        self.content_state = content_state
        self.dismissal_date = dismissal_date
        self.event = event
        self.interruption_level = interruption_level
        self.mutable_content = mutable_content
        self.sound = sound
        self.thread_id = thread_id
        self.timestamp = timestamp

    def validate(self):
        if self.alert:
            self.alert.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert is not None:
            result['alert'] = self.alert.to_map()

        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.attributes_type is not None:
            result['attributesType'] = self.attributes_type

        if self.badge is not None:
            result['badge'] = self.badge

        if self.category is not None:
            result['category'] = self.category

        if self.content_available is not None:
            result['contentAvailable'] = self.content_available

        if self.content_state is not None:
            result['contentState'] = self.content_state

        if self.dismissal_date is not None:
            result['dismissalDate'] = self.dismissal_date

        if self.event is not None:
            result['event'] = self.event

        if self.interruption_level is not None:
            result['interruptionLevel'] = self.interruption_level

        if self.mutable_content is not None:
            result['mutableContent'] = self.mutable_content

        if self.sound is not None:
            result['sound'] = self.sound

        if self.thread_id is not None:
            result['threadID'] = self.thread_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alert') is not None:
            temp_model = main_models.Alert()
            self.alert = temp_model.from_map(m.get('alert'))

        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('attributesType') is not None:
            self.attributes_type = m.get('attributesType')

        if m.get('badge') is not None:
            self.badge = m.get('badge')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('contentAvailable') is not None:
            self.content_available = m.get('contentAvailable')

        if m.get('contentState') is not None:
            self.content_state = m.get('contentState')

        if m.get('dismissalDate') is not None:
            self.dismissal_date = m.get('dismissalDate')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('interruptionLevel') is not None:
            self.interruption_level = m.get('interruptionLevel')

        if m.get('mutableContent') is not None:
            self.mutable_content = m.get('mutableContent')

        if m.get('sound') is not None:
            self.sound = m.get('sound')

        if m.get('threadID') is not None:
            self.thread_id = m.get('threadID')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

