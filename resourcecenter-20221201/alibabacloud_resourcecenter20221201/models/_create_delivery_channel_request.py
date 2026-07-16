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
        # The configurations for delivery of resource configuration change events.
        self.resource_change_delivery = resource_change_delivery
        # The configurations for delivery of scheduled resource snapshots.
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
        # The Simple Log Service configurations.
        self.sls_properties = sls_properties
        # The Alibaba Cloud Resource Name (ARN) of the delivery destination.
        # 
        # *   If you set `TargetType` to `OSS`, you must set `TargetArn` to the ARN of a bucket whose name is prefixed with resourcecenter-.
        # *   If you set `TargetType` to `SLS`, you must set `TargetArn` to the ARN of a Logstore whose name is prefixed with resourcecenter-.
        self.target_arn = target_arn
        # The type of the delivery destination.
        # 
        # Valid values:
        # 
        # *   `OSS` for standard delivery
        # *   `OSS` or `SLS` for custom delivery
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
        # The ARN of the destination to which large files are delivered.
        # 
        # *   If the size of a resource configuration change event exceeds 1 MB, the event is delivered as an OSS object.
        # *   You need to set this parameter to the ARN of a bucket whose name is prefixed with resourcecenter-.
        # *   This parameter takes effect only if you use custom delivery for scheduled resource snapshots. You do not need to configure this parameter if you use standard delivery for scheduled resource snapshots.
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
        # The Simple Log Service configurations.
        self.sls_properties = sls_properties
        # The ARN of the delivery destination.
        # 
        # *   If you set `TargetType` to `OSS`, you must set `TargetArn` to the ARN of a bucket whose name is prefixed with resourcecenter-.
        # *   If you set `TargetType` to `SLS`, you must set `TargetArn` to the ARN of a Logstore whose name is prefixed with resourcecenter-.
        self.target_arn = target_arn
        # The type of the delivery destination.
        # 
        # Valid values:
        # 
        # *   `SLS`
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
        # The ARN of the destination to which large files are delivered.
        # 
        # *   If the size of a resource configuration change event exceeds 1 MB, the event is delivered as an OSS object.
        # *   You need to set this parameter to the ARN of a bucket whose name is prefixed with resourcecenter-.
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
        # An array of effective resource types for the delivery channel.
        # 
        # *   Example: ["ACS::VPC::VPC", "ACS::ECS::Instance"].
        # *   If you want to deliver items of all resource types supported by Resource Center, set this parameter to ["ALL"].
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

