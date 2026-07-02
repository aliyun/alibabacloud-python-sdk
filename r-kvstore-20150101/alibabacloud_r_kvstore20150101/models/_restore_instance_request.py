# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreInstanceRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        filter_key: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        security_token: str = None,
        time_shift: str = None,
    ):
        # The ID of the backup file. You can find backup file IDs by calling the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation.
        self.backup_id = backup_id
        # The keys to restore, which can be specified as a regular expression. To specify multiple keys, separate them with commas (,).
        # 
        # - If you do not specify this parameter, the entire instance is restored.
        # 
        # - If you specify this parameter, only the specified keys are restored. This feature is available only for instances that use the classic architecture.
        # 
        # > In a regular expression, the asterisk (`*`) matches the preceding element zero or more times. For example, if you set this parameter to `h.*llo`, strings such as `hllo` and `heeeello` are matched.
        self.filter_key = filter_key
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The restore point in time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format (UTC).
        # 
        # > This point in time cannot be earlier than the time when the Data Flashback feature was enabled.
        self.restore_time = restore_time
        # The restore method. Valid values:
        # 
        # - **0** (default): This value is deprecated.
        # 
        # - **1**: Restores data to a specific point in time. You can set this parameter to 1 only if the [Data Flashback](https://help.aliyun.com/document_detail/148479.html) feature is enabled for the instance. If you set this parameter to 1, you must also specify the **RestoreTime** parameter.
        self.restore_type = restore_type
        self.security_token = security_token
        # For instances that use the classic architecture, you can apply an offset to the expiration time of restored keys. This applies whether you restore the entire instance or only specific keys. The system calculates a key\\"s remaining time-to-live (TTL) at the specified flashback point in time and then adds this TTL to the `TimeShift` value to set the key\\"s new expiration time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format (UTC).
        # 
        # > - This feature adjusts the expiration time for top-level keys only. It does not apply to the expiration times of elements within Tair-specific data structures, such as fields in an exHash or secondary keys (Skeys) in a Time Series (TS) data structure.
        # >
        # > - The specified time must be later than `RestoreTime` and earlier than the task submission time.
        self.time_shift = time_shift

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.time_shift is not None:
            result['TimeShift'] = self.time_shift

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TimeShift') is not None:
            self.time_shift = m.get('TimeShift')

        return self

