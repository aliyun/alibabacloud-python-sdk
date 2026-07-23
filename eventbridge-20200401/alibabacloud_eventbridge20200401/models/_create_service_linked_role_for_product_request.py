# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleForProductRequest(DaraModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        # The name of the cloud service or the service-linked role (SLR) that is associated with the service.
        # 
        # - AliyunServiceRoleForEventBridgeSendToFC: Delivers events to Function Compute (FC).
        # 
        # - AliyunServiceRoleForEventBridgeSendToSMS: Delivers events as text messages to Short Message Service (SMS).
        # 
        # - AliyunServiceRoleForEventBridgeSendToDirectMail: Delivers events as emails to Alibaba Cloud DirectMail.
        # 
        # - AliyunServiceRoleForEventBridgeSourceRocketMQ: Integrates messages from ApsaraMQ for RocketMQ instances into EventBridge.
        # 
        # - AliyunServiceRoleForEventBridgeSourceMNS: Integrates Message Service (MNS) into EventBridge.
        # 
        # - AliyunServiceRoleForEventBridgeConnectVPC: Lets EventBridge access your Virtual Private Cloud (VPC) network.
        # 
        # - AliyunServiceRoleForEventBridgeSourceActionTrail: Uses operation records from ActionTrail as event sources.
        # 
        # - AliyunServiceRoleForEventBridgeSourceRabbitMQ: Integrates ApsaraMQ for RabbitMQ instances into EventBridge.
        # 
        # - AliyunServiceRoleForEventBridgeSendToRabbitMQ: Delivers EventBridge events to ApsaraMQ for RabbitMQ instances.
        # 
        # - AliyunServiceRoleForEventBridgeSendToRocketMQ: Delivers EventBridge events to ApsaraMQ for RocketMQ instances.
        # 
        # - AliyunServiceRoleForEventBridgeSourceCMS: Integrates CloudMonitor (CMS) into EventBridge.
        # 
        # - AliyunServiceRoleForEventBridgeSendToKafka: Delivers EventBridge events to ApsaraMQ for Kafka clusters.
        # 
        # - AliyunServiceRoleForEventBridgeSourceKafka: Integrates ApsaraMQ for Kafka into EventBridge.
        # 
        # - AliyunServiceRoleForEventBridgeSendToRDS: Delivers EventBridge events to Relational Database Service (RDS) instances.
        # 
        # - AliyunServiceRoleForEventBridgeSendToSAE: Delivers EventBridge events to Serverless App Engine (SAE) applications.
        # 
        # - AliyunServiceRoleForEventBridgeSourceMqtt: Integrates ApsaraMQ for MQTT into EventBridge.
        # 
        # - AliyunServiceRoleForEventBridgeSourceSLS: Integrates Simple Log Service (SLS) into EventBridge.
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

