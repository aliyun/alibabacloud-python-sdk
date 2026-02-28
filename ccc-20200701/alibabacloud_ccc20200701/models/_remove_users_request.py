# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveUsersRequest(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        force: bool = None,
        instance_id: str = None,
        notification_email: str = None,
        user_id_list: str = None,
    ):
        self.file_path = file_path
        self.force = force
        # This parameter is required.
        self.instance_id = instance_id
        self.notification_email = notification_email
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.force is not None:
            result['Force'] = self.force

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.notification_email is not None:
            result['NotificationEmail'] = self.notification_email

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NotificationEmail') is not None:
            self.notification_email = m.get('NotificationEmail')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

