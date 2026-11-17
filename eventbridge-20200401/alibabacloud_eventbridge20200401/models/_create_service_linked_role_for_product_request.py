# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleForProductRequest(DaraModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        # The name of the cloud service or the name of the service-linked role associated with the cloud service.
        # 
        # - AliyunServiceRoleForEventBridgeSendToFC: Performs event delivery to Function Compute.
        # - AliyunServiceRoleForEventBridgeSendToSMS: Performs event delivery as text messages to Alibaba Cloud Short Message Service.
        # - AliyunServiceRoleForEventBridgeSendToDirectMail: Performs event delivery as emails to Alibaba Cloud Direct Mail.
        # - AliyunServiceRoleForEventBridgeSourceRocketMQ: Integrates consumed messages from Message Queue for RocketMQ instances into EventBridge.
        # - AliyunServiceRoleForEventBridgeSourceMNS: Integrates Alibaba Cloud Message Service (MNS) into EventBridge.
        # - AliyunServiceRoleForEventBridgeConnectVPC: Allows EventBridge to access your VPC.
        # - AliyunServiceRoleForEventBridgeSourceActionTrail: Retrieves operation records from ActionTrail as event sources.
        # - AliyunServiceRoleForEventBridgeSourceRabbitMQ: Integrates Message Queue for RabbitMQ instances into EventBridge.
        # - AliyunServiceRoleForEventBridgeSendToRabbitMQ: Performs event delivery of EventBridge events to Message Queue for RabbitMQ instances.
        # - AliyunServiceRoleForEventBridgeSendToRocketMQ: Performs event delivery of EventBridge events to Message Queue for RocketMQ instances.
        # - AliyunServiceRoleForEventBridgeSourceCMS: Integrates Alibaba Cloud monitoring (CMS) into EventBridge.
        # - AliyunServiceRoleForEventBridgeSendToKafka: Performs event delivery of EventBridge events to Message Queue for Apache Kafka clusters.
        # - AliyunServiceRoleForEventBridgeSourceKafka: Integrates Message Queue for Apache Kafka into EventBridge.
        # - AliyunServiceRoleForEventBridgeSendToRDS: Performs event delivery of EventBridge events to Relational Database Service (RDS) instances.
        # - AliyunServiceRoleForEventBridgeSendToSAE: Performs event delivery of EventBridge events to Serverless App DPI engine (SAE) applications.
        # - AliyunServiceRoleForEventBridgeSourceMqtt: Integrates Micro MSMQ for MQTT into EventBridge.
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

