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
        # The version of the delivery settings on which this modification is based. Call GetDataStorage first and pass the original value of Data.DeliverySettings.ConfigurationVersion. Example 1 only demonstrates the format and cannot be used as a fixed version. This parameter is required when modifying the global switch, account selection, automatic inclusion settings, or specified member delivery. If the version is missing or has changed, the OperationDenied.CentralizedDeliveryConfigChanged error is returned. In this case, re-query the data and then submit the request.
        self.configuration_version = configuration_version
        # The region where logs are stored.
        self.data_storage_region_id = data_storage_region_id
        # The global delivery switch for log management. This switch is not available for configuration. Valid values:
        # - enable: Enables all delivery.
        # - disable: Disables all delivery.
        self.delivery_status = delivery_status
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # Note: This parameter is actually required. If it is not specified, the API returns a 400 error: \\"The specified Lang can not be empty.\\" Specify zh or en.
        self.lang = lang
        # The global switch for multi-account centralized delivery. A value of true indicates that centralized delivery from members to the current account is enabled. A value of false indicates that centralized delivery from members to the current account is disabled. When disabled, the account selection and automatic inclusion settings are retained, and the original log type switches for the current account are independently retained. When this parameter is specified, you must also specify ConfigurationVersion and TargetProject, and omit DataStorageRegionId and DeliveryStatus. If this parameter is omitted, the storage region modification process is used. Enabling this switch for the first time initializes the account scope for log types and the automatic inclusion settings.
        self.multi_account_delivery_enabled = multi_account_delivery_enabled
        # The region of the data management center for threat analysis. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland.
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the member whose perspective the administrator switches to.
        self.role_for = role_for
        # The name of the current Simple Log Service project for log delivery. First invoke GetDataStorage and pass the original value of Data.DeliverySettings.TargetProject. This parameter is used to verify the target of this modification, not to specify a new project. This parameter is required when modifying the global switch, account selection, automatic inclusion settings, or specified member delivery. If this parameter is missing or differs from the current target, the OperationDenied.CentralizedDeliveryConfigChanged error is returned. Replace the account UID and region in the example with the query results.
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

