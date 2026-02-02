# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SinkMQTTParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mqtt_5user_property: main_models.SinkMQTTParametersMqtt5UserProperty = None,
        parent_topic: str = None,
        payload: main_models.SinkMQTTParametersPayload = None,
        sub_topic: main_models.SinkMQTTParametersSubTopic = None,
    ):
        self.instance_id = instance_id
        self.mqtt_5user_property = mqtt_5user_property
        self.parent_topic = parent_topic
        self.payload = payload
        self.sub_topic = sub_topic

    def validate(self):
        if self.mqtt_5user_property:
            self.mqtt_5user_property.validate()
        if self.payload:
            self.payload.validate()
        if self.sub_topic:
            self.sub_topic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mqtt_5user_property is not None:
            result['Mqtt5UserProperty'] = self.mqtt_5user_property.to_map()

        if self.parent_topic is not None:
            result['ParentTopic'] = self.parent_topic

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.sub_topic is not None:
            result['SubTopic'] = self.sub_topic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mqtt5UserProperty') is not None:
            temp_model = main_models.SinkMQTTParametersMqtt5UserProperty()
            self.mqtt_5user_property = temp_model.from_map(m.get('Mqtt5UserProperty'))

        if m.get('ParentTopic') is not None:
            self.parent_topic = m.get('ParentTopic')

        if m.get('Payload') is not None:
            temp_model = main_models.SinkMQTTParametersPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('SubTopic') is not None:
            temp_model = main_models.SinkMQTTParametersSubTopic()
            self.sub_topic = temp_model.from_map(m.get('SubTopic'))

        return self

class SinkMQTTParametersSubTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkMQTTParametersPayload(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkMQTTParametersMqtt5UserProperty(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

