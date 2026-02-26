# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetMultiAccountDeliveryChannelResponseBody(DaraModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: main_models.GetMultiAccountDeliveryChannelResponseBodyDeliveryChannelFilter = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        request_id: str = None,
        resource_change_delivery: main_models.GetMultiAccountDeliveryChannelResponseBodyResourceChangeDelivery = None,
        resource_snapshot_delivery: main_models.GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDelivery = None,
    ):
        # The description of the delivery channel.
        self.delivery_channel_description = delivery_channel_description
        # The effective scope of the delivery channel.
        self.delivery_channel_filter = delivery_channel_filter
        # The ID of the delivery channel.
        self.delivery_channel_id = delivery_channel_id
        # The name of the delivery channel.
        self.delivery_channel_name = delivery_channel_name
        # The request ID.
        self.request_id = request_id
        # The delivery of resource configuration changes.
        self.resource_change_delivery = resource_change_delivery
        # The configurations of scheduled delivery of resource snapshots.
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

        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id

        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
            temp_model = main_models.GetMultiAccountDeliveryChannelResponseBodyDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m.get('DeliveryChannelFilter'))

        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')

        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceChangeDelivery') is not None:
            temp_model = main_models.GetMultiAccountDeliveryChannelResponseBodyResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m.get('ResourceChangeDelivery'))

        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = main_models.GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m.get('ResourceSnapshotDelivery'))

        return self

class GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDelivery(DaraModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        enabled: str = None,
        sls_properties: main_models.GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        # The custom expression.
        self.custom_expression = custom_expression
        # The delivery time.
        self.delivery_time = delivery_time
        # Indicates whether to enable the scheduled delivery of resource snapshots. Valid values:
        # 
        # - true
        # 
        # - false
        self.enabled = enabled
        # The SLS configuration.
        self.sls_properties = sls_properties
        # The ARN of the delivery destination.
        self.target_arn = target_arn
        # The type of the delivery destination.
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

        if self.enabled is not None:
            result['Enabled'] = self.enabled

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

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('SlsProperties') is not None:
            temp_model = main_models.GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m.get('SlsProperties'))

        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties(DaraModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        # The ARN of the OSS bucket to which oversized data is delivered.
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

class GetMultiAccountDeliveryChannelResponseBodyResourceChangeDelivery(DaraModel):
    def __init__(
        self,
        enabled: str = None,
        sls_properties: main_models.GetMultiAccountDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        # Indicates whether to deliver resource configuration changes. Valid values:
        # 
        # - true
        # 
        # - false
        self.enabled = enabled
        # The Simple Log Service (SLS) configuration.
        self.sls_properties = sls_properties
        # The ARN of the delivery destination.
        self.target_arn = target_arn
        # The type of the delivery destination.
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()

        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('SlsProperties') is not None:
            temp_model = main_models.GetMultiAccountDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m.get('SlsProperties'))

        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class GetMultiAccountDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties(DaraModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        # The ARN of the Object Storage Service (OSS) bucket to which oversized data is delivered.
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

class GetMultiAccountDeliveryChannelResponseBodyDeliveryChannelFilter(DaraModel):
    def __init__(
        self,
        account_scopes: List[str] = None,
        resource_types: List[str] = None,
    ):
        # The accounts within the delivery scope.
        self.account_scopes = account_scopes
        # The types of delivered resources.
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_scopes is not None:
            result['AccountScopes'] = self.account_scopes

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopes') is not None:
            self.account_scopes = m.get('AccountScopes')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        return self

