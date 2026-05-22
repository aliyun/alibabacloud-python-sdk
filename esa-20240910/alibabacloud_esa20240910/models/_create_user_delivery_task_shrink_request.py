# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserDeliveryTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        details: str = None,
        discard_rate: float = None,
        field_name: str = None,
        filter_ver: str = None,
        http_delivery_shrink: str = None,
        kafka_delivery_shrink: str = None,
        oss_delivery_shrink: str = None,
        s_3delivery_shrink: str = None,
        sls_delivery_shrink: str = None,
        task_name: str = None,
    ):
        # The log category. Valid values:
        # 
        # *   dcdn_log_access_l1 (default): access logs.
        # *   dcdn_log_er: Edge Routine logs.
        # *   dcdn_log_waf: firewall logs.
        # *   dcdn_log_ipa: TCP/UDP proxy logs.
        # 
        # This parameter is required.
        self.business_type = business_type
        # The data center. Valid values:
        # 
        # *   cn: the Chinese mainland.
        # *   sg: outside the Chinese mainland.
        self.data_center = data_center
        # The destination of the delivery. Valid values:
        # 
        # 1.  sls: Alibaba Cloud SLS.
        # 2.  http: HTTP server.
        # 3.  aws3: Amazon S3.
        # 4.  oss: Alibaba Cloud OSS.
        # 5.  kafka: Kafka.
        # 6.  aws3cmpt: S3-compatible storage service.
        # 
        # This parameter is required.
        self.delivery_type = delivery_type
        self.details = details
        # The discard rate. Default value: 0.
        self.discard_rate = discard_rate
        # The log field. If you specify multiple fields, separate them with commas (,).
        # 
        # This parameter is required.
        self.field_name = field_name
        self.filter_ver = filter_ver
        # The configurations for delivery to an HTTP server.
        self.http_delivery_shrink = http_delivery_shrink
        # The configurations for delivery to Kafka.
        self.kafka_delivery_shrink = kafka_delivery_shrink
        # The configurations for delivery to OSS.
        self.oss_delivery_shrink = oss_delivery_shrink
        # The configurations for delivery to Amazon S3 or an S3-compatible service.
        self.s_3delivery_shrink = s_3delivery_shrink
        # The configurations for delivery to SLS.
        self.sls_delivery_shrink = sls_delivery_shrink
        # The task name.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.details is not None:
            result['Details'] = self.details

        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.filter_ver is not None:
            result['FilterVer'] = self.filter_ver

        if self.http_delivery_shrink is not None:
            result['HttpDelivery'] = self.http_delivery_shrink

        if self.kafka_delivery_shrink is not None:
            result['KafkaDelivery'] = self.kafka_delivery_shrink

        if self.oss_delivery_shrink is not None:
            result['OssDelivery'] = self.oss_delivery_shrink

        if self.s_3delivery_shrink is not None:
            result['S3Delivery'] = self.s_3delivery_shrink

        if self.sls_delivery_shrink is not None:
            result['SlsDelivery'] = self.sls_delivery_shrink

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FilterVer') is not None:
            self.filter_ver = m.get('FilterVer')

        if m.get('HttpDelivery') is not None:
            self.http_delivery_shrink = m.get('HttpDelivery')

        if m.get('KafkaDelivery') is not None:
            self.kafka_delivery_shrink = m.get('KafkaDelivery')

        if m.get('OssDelivery') is not None:
            self.oss_delivery_shrink = m.get('OssDelivery')

        if m.get('S3Delivery') is not None:
            self.s_3delivery_shrink = m.get('S3Delivery')

        if m.get('SlsDelivery') is not None:
            self.sls_delivery_shrink = m.get('SlsDelivery')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

