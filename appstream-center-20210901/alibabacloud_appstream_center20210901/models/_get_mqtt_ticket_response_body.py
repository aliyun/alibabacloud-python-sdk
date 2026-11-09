# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMqttTicketResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        expire_time_stamp: str = None,
        message: str = None,
        mqtt_endpoint: str = None,
        mqtt_group_id: str = None,
        mqtt_instance_id: str = None,
        mqtt_password: str = None,
        mqtt_username: str = None,
        mqtt_vpcendpoint: str = None,
        request_id: str = None,
        success: str = None,
        topic_list: str = None,
    ):
        # The error code returned when the request fails. For example, `Client.Forbidden` indicates that the client is forbidden from establishing a connection.
        self.code = code
        # The expiration time of the MQTT connection password. It is returned as a string representing a UNIX timestamp in milliseconds.
        self.expire_time_stamp = expire_time_stamp
        # The error message returned when the request fails, which corresponds to the error code.
        self.message = message
        # The access endpoint for the MQTT client. Use the endpoint returned by this operation to establish a connection.
        self.mqtt_endpoint = mqtt_endpoint
        # The MQTT group ID, used to concatenate the MQTT ClientId.
        self.mqtt_group_id = mqtt_group_id
        # The MQTT instance ID, used for token authentication.
        self.mqtt_instance_id = mqtt_instance_id
        # The password used to establish an MQTT connection. It consists of publish and subscribe tokens in the format of `W|PublishToken|R|SubscribeToken`. Use the complete password returned by the operation. The desensitized examples in the documentation cannot be used for connections.
        self.mqtt_password = mqtt_password
        # The username used to establish an MQTT connection. The format is `Token|AccessKeyId|InstanceId`. AccessKeyId and InstanceId are identifiers used by the server to generate credentials. Use the complete username returned by the operation.
        self.mqtt_username = mqtt_username
        # The VPC access endpoint for MQTT, used by clients that meet the VPC network access requirements.
        self.mqtt_vpcendpoint = mqtt_vpcendpoint
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. `true` indicates success, and `false` indicates failure.
        self.success = success
        # The topic list. Each list element contains `topic` (the topic name), `type` (the topic type), and `permission` (the permission). The list returned by this operation includes topics for publishing, tenant subscription, device subscription, and system subscription. The publish permission is `W`, and the subscribe permission is `R`.
        self.topic_list = topic_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.expire_time_stamp is not None:
            result['ExpireTimeStamp'] = self.expire_time_stamp

        if self.message is not None:
            result['Message'] = self.message

        if self.mqtt_endpoint is not None:
            result['MqttEndpoint'] = self.mqtt_endpoint

        if self.mqtt_group_id is not None:
            result['MqttGroupId'] = self.mqtt_group_id

        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id

        if self.mqtt_password is not None:
            result['MqttPassword'] = self.mqtt_password

        if self.mqtt_username is not None:
            result['MqttUsername'] = self.mqtt_username

        if self.mqtt_vpcendpoint is not None:
            result['MqttVPCEndpoint'] = self.mqtt_vpcendpoint

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.topic_list is not None:
            result['TopicList'] = self.topic_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExpireTimeStamp') is not None:
            self.expire_time_stamp = m.get('ExpireTimeStamp')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MqttEndpoint') is not None:
            self.mqtt_endpoint = m.get('MqttEndpoint')

        if m.get('MqttGroupId') is not None:
            self.mqtt_group_id = m.get('MqttGroupId')

        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')

        if m.get('MqttPassword') is not None:
            self.mqtt_password = m.get('MqttPassword')

        if m.get('MqttUsername') is not None:
            self.mqtt_username = m.get('MqttUsername')

        if m.get('MqttVPCEndpoint') is not None:
            self.mqtt_vpcendpoint = m.get('MqttVPCEndpoint')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TopicList') is not None:
            self.topic_list = m.get('TopicList')

        return self

