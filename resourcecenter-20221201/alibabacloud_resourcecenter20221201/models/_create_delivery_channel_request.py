# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class CreateDeliveryChannelRequest(DaraModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: main_models.CreateDeliveryChannelRequestDeliveryChannelFilter = None,
        delivery_channel_name: str = None,
        resource_change_delivery: main_models.CreateDeliveryChannelRequestResourceChangeDelivery = None,
        resource_snapshot_delivery: main_models.CreateDeliveryChannelRequestResourceSnapshotDelivery = None,
    ):
        # The description of the delivery channel.
        self.delivery_channel_description = delivery_channel_description
        # The effective scope of the delivery channel.
        # 
        # This parameter is required.
        self.delivery_channel_filter = delivery_channel_filter
        # The name of the delivery channel.
        # 
        # This parameter is required.
        self.delivery_channel_name = delivery_channel_name
        # The delivery of resource configuration changes.
        self.resource_change_delivery = resource_change_delivery
        # The scheduled delivery of resource snapshots.
        self.resource_snapshot_delivery = resource_snapshot_delivery

    def validate(self):
        if self.delivery_channel_filter:
            self.delivery_channel_filter.validate()
        if self.resource_change_delivery:
            self.resource_change_delivery.validate()
        if self.resource_snapshot_delivery:
            self.resource_snapshot_delivery.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description

        if self.delivery_channel_filter is not None:
            result['DeliveryChannelFilter'] = self.delivery_channel_filter.to_map()

        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name

        if self.resource_change_delivery is not None:
            result['ResourceChangeDelivery'] = self.resource_change_delivery.to_map()

        if self.resource_snapshot_delivery is not None:
            result['ResourceSnapshotDelivery'] = self.resource_snapshot_delivery.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')

        if m.get('DeliveryChannelFilter') is not None:
            temp_model = main_models.CreateDeliveryChannelRequestDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m.get('DeliveryChannelFilter'))

        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')

        if m.get('ResourceChangeDelivery') is not None:
            temp_model = main_models.CreateDeliveryChannelRequestResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m.get('ResourceChangeDelivery'))

        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = main_models.CreateDeliveryChannelRequestResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m.get('ResourceSnapshotDelivery'))

        return self

class CreateDeliveryChannelRequestResourceSnapshotDelivery(DaraModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        sls_properties: main_models.CreateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        # The custom expression.
        self.custom_expression = custom_expression
        # The delivery time.
        self.delivery_time = delivery_time
        # The SLS configurations.
        self.sls_properties = sls_properties
        # The Alibaba Cloud Resource Name (ARN) of the destination. Valid values:
        # 
        # - If you set `TargetType` to `OSS`, set `TargetArn` to the ARN of an Object Storage Service (OSS) bucket that has the `resourcecenter-` prefix. Example: `acs:oss:cn-hangzhou:191142248777****:resourcecenter-oss`.
        # 
        # - If you set `TargetType` to `SLS`, set `TargetArn` to the ARN of a Simple Log Service (SLS) Logstore that has the `resourcecenter-` prefix. Example: `acs:log:cn-hangzhou: 191142248777****:project/delivery/logstore/resourcecenter-sls`.
        self.target_arn = target_arn
        # The type of the destination. Valid values:
        # 
        # - For standard scheduled delivery, set this parameter to `OSS`.
        # 
        # - For custom scheduled delivery, set this parameter to `OSS` or `SLS`.
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_expression is not None:
            result['CustomExpression'] = self.custom_expression

        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time

        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()

        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExpression') is not None:
            self.custom_expression = m.get('CustomExpression')

        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')

        if m.get('SlsProperties') is not None:
            temp_model = main_models.CreateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m.get('SlsProperties'))

        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class CreateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties(DaraModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        # The ARN of the destination OSS bucket for oversized files.
        # 
        # If the size of a resource configuration change event exceeds 1 MB, the event is delivered as an OSS object. Set this parameter to the ARN of an OSS bucket that has the `resourcecenter-` prefix.
        # 
        # > This parameter is valid only for custom scheduled delivery. You do not need to specify this parameter for standard scheduled delivery.
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')

        return self

class CreateDeliveryChannelRequestResourceChangeDelivery(DaraModel):
    def __init__(
        self,
        sls_properties: main_models.CreateDeliveryChannelRequestResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        # The SLS configurations.
        self.sls_properties = sls_properties
        # The ARN of the destination. Valid values:
        # 
        # - If you set `TargetType` to `OSS`, set `TargetArn` to the ARN of an OSS bucket that has the `resourcecenter-` prefix.
        # 
        # - If you set `TargetType` to `SLS`, set `TargetArn` to the ARN of an SLS Logstore that has the `resourcecenter-` prefix.
        self.target_arn = target_arn
        # The type of the destination.
        # 
        # Valid value: `SLS`.
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()

        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProperties') is not None:
            temp_model = main_models.CreateDeliveryChannelRequestResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m.get('SlsProperties'))

        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class CreateDeliveryChannelRequestResourceChangeDeliverySlsProperties(DaraModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        # The ARN of the destination OSS bucket for oversized files.
        # 
        # If the size of a resource configuration change event exceeds 1 MB, the event is delivered as an OSS object. Set this parameter to the ARN of an OSS bucket that has the `resourcecenter-` prefix.
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')

        return self

class CreateDeliveryChannelRequestDeliveryChannelFilter(DaraModel):
    def __init__(
        self,
        resource_types: List[str] = None,
    ):
        # The list of resource types to be delivered.
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        return self

