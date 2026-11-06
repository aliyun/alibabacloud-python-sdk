# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataStorageRequest(DaraModel):
    def __init__(
        self,
        configuration_version: int = None,
        data_storage_region_id: str = None,
        delivery_status: str = None,
        lang: str = None,
        multi_account_delivery_enabled: bool = None,
        region_id: str = None,
        role_for: int = None,
        target_project: str = None,
    ):
        # The configuration version obtained from the query when modifying multi-account delivery.
        self.configuration_version = configuration_version
        # The region for log storage.
        self.data_storage_region_id = data_storage_region_id
        # The global delivery switch for log management. This parameter is not available for configuration. Valid values:
        # - enable: Enables all delivery.
        # - disable: Disables all delivery.
        self.delivery_status = delivery_status
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # Note: This parameter is required. If you do not specify this parameter, the API returns a 400 error: "The specified Lang can not be empty." Specify zh or en.
        self.lang = lang
        # The global switch for multi-account centralized delivery. If this parameter is omitted, the original storage update behavior is maintained. Do not mix this parameter with the storage region or the original delivery status.
        self.multi_account_delivery_enabled = multi_account_delivery_enabled
        # The region where the data management center for threat analysis is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland.
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # The current target project obtained from the query when modifying multi-account delivery.
        self.target_project = target_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_version is not None:
            result['ConfigurationVersion'] = self.configuration_version

        if self.data_storage_region_id is not None:
            result['DataStorageRegionId'] = self.data_storage_region_id

        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.multi_account_delivery_enabled is not None:
            result['MultiAccountDeliveryEnabled'] = self.multi_account_delivery_enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.target_project is not None:
            result['TargetProject'] = self.target_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationVersion') is not None:
            self.configuration_version = m.get('ConfigurationVersion')

        if m.get('DataStorageRegionId') is not None:
            self.data_storage_region_id = m.get('DataStorageRegionId')

        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MultiAccountDeliveryEnabled') is not None:
            self.multi_account_delivery_enabled = m.get('MultiAccountDeliveryEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('TargetProject') is not None:
            self.target_project = m.get('TargetProject')

        return self

