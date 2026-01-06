# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SinkRabbitMQMsgSyncParameters(DaraModel):
    def __init__(
        self,
        body: main_models.SinkRabbitMQMsgSyncParametersBody = None,
        endpoint: str = None,
        exchange: main_models.SinkRabbitMQMsgSyncParametersExchange = None,
        instance_id: str = None,
        instance_type: str = None,
        max_hops: str = None,
        message_id: main_models.SinkRabbitMQMsgSyncParametersMessageId = None,
        network_type: str = None,
        password: str = None,
        properties: main_models.SinkRabbitMQMsgSyncParametersProperties = None,
        routing_key: main_models.SinkRabbitMQMsgSyncParametersRoutingKey = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_ids: str = None,
        virtual_host_name: str = None,
        vpc_id: str = None,
    ):
        self.body = body
        self.endpoint = endpoint
        self.exchange = exchange
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.max_hops = max_hops
        self.message_id = message_id
        self.network_type = network_type
        self.password = password
        self.properties = properties
        self.routing_key = routing_key
        self.security_group_id = security_group_id
        self.username = username
        self.v_switch_ids = v_switch_ids
        self.virtual_host_name = virtual_host_name
        self.vpc_id = vpc_id

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.routing_key:
            self.routing_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_hops is not None:
            result['MaxHops'] = self.max_hops

        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.password is not None:
            result['Password'] = self.password

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.username is not None:
            result['Username'] = self.username

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Exchange') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParametersExchange()
            self.exchange = temp_model.from_map(m.get('Exchange'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxHops') is not None:
            self.max_hops = m.get('MaxHops')

        if m.get('MessageId') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Properties') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('RoutingKey') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParametersRoutingKey()
            self.routing_key = temp_model.from_map(m.get('RoutingKey'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class SinkRabbitMQMsgSyncParametersRoutingKey(DaraModel):
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

class SinkRabbitMQMsgSyncParametersProperties(DaraModel):
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

class SinkRabbitMQMsgSyncParametersMessageId(DaraModel):
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

class SinkRabbitMQMsgSyncParametersExchange(DaraModel):
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

class SinkRabbitMQMsgSyncParametersBody(DaraModel):
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

