# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListConsumerConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListConsumerConnectionsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned error code.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListConsumerConnectionsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListConsumerConnectionsResponseBodyData(DaraModel):
    def __init__(
        self,
        connections: List[main_models.ListConsumerConnectionsResponseBodyDataConnections] = None,
        consumer_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client connection list
        self.connections = connections
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        self.region_id = region_id

    def validate(self):
        if self.connections:
            for v1 in self.connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['connections'] = []
        if self.connections is not None:
            for k1 in self.connections:
                result['connections'].append(k1.to_map() if k1 else None)

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('connections') is not None:
            for k1 in m.get('connections'):
                temp_model = main_models.ListConsumerConnectionsResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k1))

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class ListConsumerConnectionsResponseBodyDataConnections(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        egress_ip: str = None,
        hostname: str = None,
        language: str = None,
        message_model: str = None,
        version: str = None,
    ):
        # The ID of the client.
        self.client_id = client_id
        # Host IP/Public IP
        self.egress_ip = egress_ip
        # The `hostname` of the cloud-native box.
        self.hostname = hostname
        # The language of the client.
        self.language = language
        # Consumption Mode
        # - BROADCASTING
        # - CLUSTERING
        self.message_model = message_model
        # The version of the client.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.egress_ip is not None:
            result['egressIp'] = self.egress_ip

        if self.hostname is not None:
            result['hostname'] = self.hostname

        if self.language is not None:
            result['language'] = self.language

        if self.message_model is not None:
            result['messageModel'] = self.message_model

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('egressIp') is not None:
            self.egress_ip = m.get('egressIp')

        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

