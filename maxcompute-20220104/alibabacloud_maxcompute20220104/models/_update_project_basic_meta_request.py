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
        # The description of the project.
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
        # Specifies whether to allow full table scans in the project. A full table scan consumes a large amount of resources. To improve processing efficiency, this feature is disabled by default.
        self.allow_full_scan = allow_full_scan
        # Specifies whether to enable the Decimal data type of MaxCompute V2.0 for the project.
        self.enable_decimal_2 = enable_decimal_2
        self.enable_dr = enable_dr
        # Specifies whether to enable resource group-based routing for Data Transmission Service.
        # 
        # - true: Data transmission tasks submitted in the project use the attached Data Transmission Service resource group by default.
        # 
        # - false: Data transmission tasks submitted in the project use the shared Data Transmission Service resource group by default.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The number of days to retain backup data. During this period, you can restore the current version to any backup version.
        # The value must be an integer from 0 to 30. The default value is 1. A value of 0 disables the backup feature.
        self.retention_days = retention_days
        # The maximum consumption threshold for a single SQL job.
        # Unit: Scanned data (GB) × Complexity.
        self.sql_metering_max = sql_metering_max
        # The lifecycle properties of the table.
        self.table_lifecycle = table_lifecycle
        # The time zone of the project. This is the `odps.sql.timezone` property.
        self.timezone = timezone
        # The <props="intl">[Data Transmission Service](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/overview-of-dts) resource group attached to the project.
        # 
        # - Default (shared Data Transmission Service resource group): The project is not allowed to use a subscription Data Transmission Service resource group. Regardless of the value of the default Data Transmission Service resource group, data transmission tasks submitted in the project automatically use the Default resource group.
        # 
        # - Subscription Data Transmission Service resource group: The project is allowed to use a subscription Data Transmission Service resource group.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # 
        # - **1**: Edition 1.0
        # 
        # - **2**: Edition 2.0
        # 
        # - **hive**: Hive-compatible edition
        # 
        # For more information about the differences between the data type editions, see <props="intl">[Data type editions](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/data-type-editions).
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
        # 
        # - **mandatory**: The Lifecycle clause is required. You must set a lifecycle for the table.
        # 
        # - **optional**: The Lifecycle clause is optional when you create a table. If you do not set a lifecycle for the table, the table never expires.
        # 
        # - **inherit**: If you do not set a lifecycle for the table when you create it, the lifecycle of the table is the value of odps.table.lifecycle.value.
        self.type = type
        # The lifecycle of the table in days. The value must be an integer from 1 to 37231. The default value is 37231.
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
        # The encryption algorithm. The key supports algorithms such as AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Specifies whether to enable data encryption for the project. For more information about data encryption, see
        # <props="intl">[Storage encryption](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The type of key used for data encryption. This can be the default MaxCompute key or a Bring-Your-Own-Key (BYOK). The default MaxCompute key is created within MaxCompute.
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

