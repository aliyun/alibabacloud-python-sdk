# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataValue(DaraModel):
    def __init__(
        self,
        master_uid: int = None,
        c_instance_id: str = None,
        access_key: str = None,
        user_name: str = None,
        password: str = None,
        deleted: int = None,
        create_timestamp: int = None,
        remark: str = None,
    ):
        # The Alibaba Cloud account ID or Resource Access Management (RAM) user to which the AccessKey pair that is used to create the static username and password belongs.
        self.master_uid = master_uid
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.c_instance_id = c_instance_id
        # The AccessKey ID that is used to create the static username and password.
        self.access_key = access_key
        # The static username.
        self.user_name = user_name
        # The static password.
        self.password = password
        # The timestamp that indicates when the static username and password were deleted. Unit: milliseconds.
        self.deleted = deleted
        # The timestamp that indicates when the static username and password were created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_uid is not None:
            result['masterUid'] = self.master_uid

        if self.c_instance_id is not None:
            result['cInstanceId'] = self.c_instance_id

        if self.access_key is not None:
            result['accessKey'] = self.access_key

        if self.user_name is not None:
            result['userName'] = self.user_name

        if self.password is not None:
            result['password'] = self.password

        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('masterUid') is not None:
            self.master_uid = m.get('masterUid')

        if m.get('cInstanceId') is not None:
            self.c_instance_id = m.get('cInstanceId')

        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

