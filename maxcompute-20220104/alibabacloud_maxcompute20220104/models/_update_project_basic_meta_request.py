# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class UpdateProjectBasicMetaRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        properties: main_models.UpdateProjectBasicMetaRequestProperties = None,
    ):
        # The project description.
        self.comment = comment
        # The basic properties of the project.
        self.properties = properties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.properties is not None:
            result['properties'] = self.properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('properties') is not None:
            temp_model = main_models.UpdateProjectBasicMetaRequestProperties()
            self.properties = temp_model.from_map(m.get('properties'))

        return self

class UpdateProjectBasicMetaRequestProperties(DaraModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        enable_decimal_2: bool = None,
        enable_dr: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: main_models.UpdateProjectBasicMetaRequestPropertiesEncryption = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        table_lifecycle: main_models.UpdateProjectBasicMetaRequestPropertiesTableLifecycle = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Indicates whether a full table scan is allowed in the project. A full table scan occupies a large number of resources, which reduces data processing efficiency. By default, the full table scan feature is disabled.
        self.allow_full_scan = allow_full_scan
        # Indicates whether the DECIMAL type of the MaxCompute V2.0 data type edition is enabled.
        self.enable_decimal_2 = enable_decimal_2
        self.enable_dr = enable_dr
        # Indicates whether the routing of the Tunnel resource group is enabled.
        # 
        # - true: The data transfer tasks that are submitted by the project by default use the Tunnel resource group that is bound to the project.
        # - false: The data transfer tasks that are submitted by the project by default use the Tunnel shared resource group.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The retention period for backup data. Unit: days. During the retention period, you can restore data of the version in use to the backup data of any version. Valid values: [0,30]. Default value: 1. The value 0 indicates that the backup feature is disabled.
        self.retention_days = retention_days
        # The maximum consumption threshold of a single SQL statement. Formula: Amount of scanned data (GB) × Complexity.
        self.sql_metering_max = sql_metering_max
        # The table lifecycle properties.
        self.table_lifecycle = table_lifecycle
        # The time zone that is used by your project. The time zone is the same as the time zone specified by `odps.sql.timezone` .
        self.timezone = timezone
        # The <props="china">[Data Transmission Service](https://help.aliyun.com/zh/maxcompute/user-guide/overview-of-dts)
        # <props="intl">[Data Transmission Service](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/overview-of-dts) resource group that is bound to the project.
        # 
        # - Default resource group: The Tunnel shared resource group is used. You cannot use the subscription-based Tunnel resource group for the project. The default resource group is automatically used by the Tunnel service of your project, regardless of the parameter setting.
        # - Subscription-based Tunnel resource group: You can use the subscription-based Tunnel resource group for the project.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # 
        # - *1*: MaxCompute V1.0 data type edition
        # - *2*: MaxCompute V2.0 data type edition
        # - *hive*: Hive-compatible data type edition
        # For more information about the differences among the three data type editions, see <props="china">[Data Type Versions](https://help.aliyun.com/zh/maxcompute/user-guide/data-type-editions)
        # <props="intl">[Data Type Versions](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/data-type-editions).
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan

        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2

        if self.enable_dr is not None:
            result['enableDr'] = self.enable_dr

        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route

        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()

        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days

        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max

        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota

        if self.type_system is not None:
            result['typeSystem'] = self.type_system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')

        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')

        if m.get('enableDr') is not None:
            self.enable_dr = m.get('enableDr')

        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')

        if m.get('encryption') is not None:
            temp_model = main_models.UpdateProjectBasicMetaRequestPropertiesEncryption()
            self.encryption = temp_model.from_map(m.get('encryption'))

        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')

        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')

        if m.get('tableLifecycle') is not None:
            temp_model = main_models.UpdateProjectBasicMetaRequestPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m.get('tableLifecycle'))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')

        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')

        return self

class UpdateProjectBasicMetaRequestPropertiesTableLifecycle(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The lifecycle type. Valid values:
        # - *mandatory*: The lifecycle clause is required in a table creation statement.
        # - *optional*: The lifecycle clause is optional in a table creation statement. If you do not configure a lifecycle for a table, the table does not expire.
        # - *inherit*: If you do not configure a lifecycle for a table when you create the table, the value of the odps.table.lifecycle.value parameter is used as the table lifecycle by default.
        self.type = type
        # The table lifecycle. Unit: days. Valid values: 1 to 37231. Default value: 37231.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class UpdateProjectBasicMetaRequestPropertiesEncryption(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The data encryption algorithm that is supported by the key. Valid values: AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Indicates whether the data encryption feature needs to be enabled for the project. For more information about data encryption, see
        # <props="china">[Storage Encryption](https://help.aliyun.com/zh/maxcompute/security-and-compliance/storage-encryption)
        # <props="intl">[Storage Encryption](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The type of key that is used for data encryption. You can select MaxCompute Default Key or Bring Your Own Key (BYOK) as the key type. If you select MaxCompute Default Key, the default key that is created by MaxCompute is used.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm

        if self.enable is not None:
            result['enable'] = self.enable

        if self.key is not None:
            result['key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('key') is not None:
            self.key = m.get('key')

        return self

