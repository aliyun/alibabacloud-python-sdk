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
        # The ID of the backup file. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html)operation to query the IDs of backup files.
        self.backup_id = backup_id
        # The key that you want to restore. You can specify multiple keys. Separate multiple keys with commas (,). Regular expressions are supported.
        # 
        # *   If you do not specify this parameter, the entire instance is restored.
        # *   If you specify this parameter, only the involved keys are restored. Only classic instances support this feature.
        # 
        # >  In a regular expression, an asterisk (`*`) matches zero or more occurrences of a subexpression that occurs before. For example, if you set this parameter to `h.*llo`, strings such as `hllo` and `heeeello` are matched.
        self.filter_key = filter_key
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # >  The point in time cannot be earlier than the point in time when the data flashback feature is enabled.
        self.restore_time = restore_time
        # The restoration mode. Valid values:
        # 
        # *   **0** (default): The parameter is invalid.
        # *   **1**: restores data to a specified point in time. You can specify this value only if the [data flashback](https://help.aliyun.com/document_detail/148479.html) feature is enabled for the instance. If you specify this value, you also need to set the **RestoreTime** parameter.
        self.restore_type = restore_type
        self.security_token = security_token
        # When you restore a classic instance, regardless of whether you choose to restore all data or specific keys, you can apply an offset to the expiration time of the keys. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. A key expires after the remaining validity period of the key elapses based on the expiration offset time point.
        # 
        # > 
        # 
        # *   This feature applies only to keys and does not work on elements in the self-developed data structures of Tair, such as fields in exHash and skeys in TairTS.
        # 
        # *   This time point must be between the specified flashback time point and the submission time of the data restoration task.
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

