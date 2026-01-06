# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleForProductRequest(DaraModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        # The name of the cloud service or the name of the service-linked role with which the cloud service is associated. Valid values:
        # 
        # *   AliyunServiceRoleForEventBridgeSendToFC: allows EventBridge to deliver events to Function Compute.
        # *   AliyunServiceRoleForEventBridgeSendToSMS: allows EventBridge to deliver events to Short Message Service (SMS).
        # *   AliyunServiceRoleForEventBridgeSendToDirectMail: allows EventBridge to deliver events to Direct Mail.
        # *   AliyunServiceRoleForEventBridgeSourceRocketMQ: allows EventBridge to integrate with ApsaraMQ for RocketMQ.
        # *   AliyunServiceRoleForEventBridgeSourceMNS: allows EventBridge to integrate with Simple Message Queue (SMQ, formerly MNS).
        # *   AliyunServiceRoleForEventBridgeConnectVPC: allows EventBridge to access virtual private clouds (VPCs).
        # *   AliyunServiceRoleForEventBridgeSourceActionTrail: allows EventBridge to integrate with ActionTrail.
        # *   AliyunServiceRoleForEventBridgeSourceRabbitMQ: allows EventBridge to integrate with ApsaraMQ for RabbitMQ.
        # *   AliyunServiceRoleForEventBridgeSendToRabbitMQ: allows EventBridge to deliver events to ApsaraMQ for RabbitMQ.
        # *   AliyunServiceRoleForEventBridgeSendToRocketMQ: allows EventBridge to deliver events to ApsaraMQ for RocketMQ.
        # *   AliyunServiceRoleForEventBridgeSourceCMS: allow EventBridge to integrate with CloudMonitor.
        # *   AliyunServiceRoleForEventBridgeSendToKafka: allows EventBridge to deliver events to ApsaraMQ for Kafka.
        # *   AliyunServiceRoleForEventBridgeSourceKafka: allows EventBridge to integrate with ApsaraMQ for Kafka.
        # *   AliyunServiceRoleForEventBridgeSendToRDS: allows EventBridge to deliver events to ApsaraDB RDS.
        # *   AliyunServiceRoleForEventBridgeSendToSAE: allows EventBridge to deliver events to Serverless App Engine (SAE).
        # *   AliyunServiceRoleForEventBridgeSourceMqtt: allows EventBridge to integrate with ApsaraMQ for MQTT.
        # *   AliyunServiceRoleForEventBridgeSourceSLS: allows EventBridge to integrate with Simple Log Service.
        # 
        # This parameter is required.
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_name is not None:
            result['ProductName'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        return self

