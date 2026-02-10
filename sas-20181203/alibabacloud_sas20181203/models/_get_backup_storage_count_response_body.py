# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetBackupStorageCountResponseBody(DaraModel):
    def __init__(
        self,
        backup_storage_count: main_models.GetBackupStorageCountResponseBodyBackupStorageCount = None,
        request_id: str = None,
    ):
        # The details about the anti-ransomware capacity.
        self.backup_storage_count = backup_storage_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.backup_storage_count:
            self.backup_storage_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_storage_count is not None:
            result['BackupStorageCount'] = self.backup_storage_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupStorageCount') is not None:
            temp_model = main_models.GetBackupStorageCountResponseBodyBackupStorageCount()
            self.backup_storage_count = temp_model.from_map(m.get('BackupStorageCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetBackupStorageCountResponseBodyBackupStorageCount(DaraModel):
    def __init__(
        self,
        buy_storage_byte: int = None,
        ecs_usage_storage_byte: int = None,
        overflow: int = None,
        uni_usage_storage_byte: int = None,
        usage_storage_byte: int = None,
    ):
        # The anti-ransomware capacity that you purchased. Unit: bytes.
        self.buy_storage_byte = buy_storage_byte
        # The storage capacity that is occupied by the backup data of your servers. Unit: bytes.
        self.ecs_usage_storage_byte = ecs_usage_storage_byte
        # Indicates whether the anti-ransomware capacity that is used exceeds the anti-ransomware capacity that you purchased. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.overflow = overflow
        # The storage capacity that is occupied by the backup data of your databases. Unit: bytes.
        self.uni_usage_storage_byte = uni_usage_storage_byte
        # The total anti-ransomware capacity that is used. Unit: bytes.
        self.usage_storage_byte = usage_storage_byte

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_storage_byte is not None:
            result['BuyStorageByte'] = self.buy_storage_byte

        if self.ecs_usage_storage_byte is not None:
            result['EcsUsageStorageByte'] = self.ecs_usage_storage_byte

        if self.overflow is not None:
            result['Overflow'] = self.overflow

        if self.uni_usage_storage_byte is not None:
            result['UniUsageStorageByte'] = self.uni_usage_storage_byte

        if self.usage_storage_byte is not None:
            result['UsageStorageByte'] = self.usage_storage_byte

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyStorageByte') is not None:
            self.buy_storage_byte = m.get('BuyStorageByte')

        if m.get('EcsUsageStorageByte') is not None:
            self.ecs_usage_storage_byte = m.get('EcsUsageStorageByte')

        if m.get('Overflow') is not None:
            self.overflow = m.get('Overflow')

        if m.get('UniUsageStorageByte') is not None:
            self.uni_usage_storage_byte = m.get('UniUsageStorageByte')

        if m.get('UsageStorageByte') is not None:
            self.usage_storage_byte = m.get('UsageStorageByte')

        return self

