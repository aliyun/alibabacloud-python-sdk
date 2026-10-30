# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleForProductRequest(DaraModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        # The name of the Alibaba Cloud service or the name of the service-linked role associated with the service. Valid values:
        # - AliyunServiceRoleForEventBridgeSendToFC: Performs event delivery to Function Compute.
        # - AliyunServiceRoleForEventBridgeSendToSMS: Performs event delivery as text messages to Short Message Service.
        # - AliyunServiceRoleForEventBridgeSendToDirectMail: Performs event delivery as emails to Direct Mail.
        # - AliyunServiceRoleForEventBridgeSourceRocketMQ: Integrates consumed messages from MSMQ RocketMQ instances into EventBridge.
        # - AliyunServiceRoleForEventBridgeSourceMNS: Integrates Simple Message Queue (formerly MNS) into EventBridge.
        # - AliyunServiceRoleForEventBridgeConnectVPC: Allows EventBridge to access your VPC.
        # - AliyunServiceRoleForEventBridgeSourceActionTrail: Retrieves operation records from ActionTrail as event sources.
        # - AliyunServiceRoleForEventBridgeSourceRabbitMQ: Integrates MSMQ RabbitMQ instances into EventBridge.
        # - AliyunServiceRoleForEventBridgeSendToRabbitMQ: Performs event delivery of EventBridge events to MSMQ RabbitMQ instances.
        # - AliyunServiceRoleForEventBridgeSendToRocketMQ: Performs event delivery of EventBridge events to MSMQ RocketMQ instances.
        # - AliyunServiceRoleForEventBridgeSourceCMS: Integrates Alibaba Cloud monitoring (CMS) into EventBridge.
        # - AliyunServiceRoleForEventBridgeSendToKafka: Performs event delivery of EventBridge events to Message Queue for Apache Kafka clusters.
        # - AliyunServiceRoleForEventBridgeSourceKafka: Integrates Message Queue for Apache Kafka into EventBridge.
        # - AliyunServiceRoleForEventBridgeSendToRDS: Performs event delivery of EventBridge events to Relational Database Service (RDS) instances.
        # - AliyunServiceRoleForEventBridgeSendToSAE: Performs event delivery of EventBridge events to Serverless App DPI engine (SAE) applications.
        # - AliyunServiceRoleForEventBridgeSourceMqtt: Integrates MSMQ MQTT into EventBridge.
        # - AliyunServiceRoleForEventBridgeSourceSLS: Integrates Simple Log Service into EventBridge.
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

