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
        # The ID of the backup file for the instance. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to query the ID.
        self.backup_id = backup_id
        # The keys to restore. Regular expressions are supported. Separate multiple values with commas (,).
        # - If you do not specify this parameter, the entire instance is restored.
        # - If you specify this parameter, only the specified keys are restored. This feature is supported only by classic architecture instances.
        # > For example, in a regular expression, an asterisk (`*`) matches the preceding subexpression zero or more times. If you set this parameter to `h.*llo`, the system matches strings such as `hllo` and `heeeello`.
        self.filter_key = filter_key
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z format. The time must be in UTC.
        # > The point in time cannot be earlier than the time when the data flashback feature is enabled.
        self.restore_time = restore_time
        # The restoration type. Valid values:
        # * **0** (default): This value is deprecated.
        # * **1**: Restores data to a specified point in time. You can specify this value only when the [data flashback](https://help.aliyun.com/document_detail/148479.html) feature is enabled for the instance. If you specify this value, you must also specify the **RestoreTime** parameter.
        self.restore_type = restore_type
        self.security_token = security_token
        # When you restore a classic architecture instance, you can apply an offset to the expiration time of keys regardless of whether you choose to restore full data or specified keys. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The instance calculates the remaining expiration duration of the keys at the specified flashback point in time, starting from the specified expiration offset point in time.
        # > * This feature supports offsetting the expiration time only at the key level. It does not support offsetting the internal expiration time of keys in Tair-developed data structures, such as the fields in exHash and the skeys in TS.
        # > * The point in time cannot be earlier than the specified flashback point in time or later than the time when the restoration task is submitted.
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

