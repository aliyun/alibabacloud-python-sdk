# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDeviceAutoUpgradePolicyRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        duration: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        serial_number: str = None,
        smart_agid: str = None,
        time_zone: str = None,
        upgrade_type: str = None,
        version_type: str = None,
    ):
        # The time when upgrades start. Valid values: Set the parameter in a cron expression.
        # 
        # For example, you can use `0 0 4 1/1 * ?` to specify 04:00:00 (UTC+8) on the first day of each month.
        self.cron_expression = cron_expression
        # The time period during which upgrades are performed. Valid values: **30 to 120**.
        # 
        # Unit: minutes.
        self.duration = duration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.serial_number = serial_number
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The time zone. Valid values:
        # 
        # **Asia/Shanghai**: UTC+8 (Beijing)
        # 
        # **Asia/Hong_Kong**: UTC+8 (Hong Kong)
        # 
        # **Asia/Tokyo**: UTC+9 (Tokyo)
        # 
        # **Australia/Sydney**: UTC+10 (Sydney)
        # 
        # **Asia/Kuala_Lumpur**: UTC+8 (Kuala Lumpur)
        # 
        # **Europe/Berli**: UTC+1 (Berlin)
        # 
        # **Asia/Singapore**: UTC+8 (Singapore)
        # 
        # **Asia/Jakarta**: UTC+7 (Jakarta)
        self.time_zone = time_zone
        # The update type. Valid values:
        # 
        # *   **scheduled**: scheduled upgrade.
        # *   **boot**: automatic upgrade upon device startup.
        # *   **manual**: manual upgrade.
        # 
        # This parameter is required.
        self.upgrade_type = upgrade_type
        # The type of software for which you want to modify the upgrade policy. Valid values:
        # 
        # *   **Device**: The operating system run by the SAG device.
        # *   **Dpi**: The signature database used by the SAG device.
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        if self.version_type is not None:
            result['VersionType'] = self.version_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')

        return self

