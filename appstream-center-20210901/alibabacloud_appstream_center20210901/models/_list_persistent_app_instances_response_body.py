# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListPersistentAppInstancesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        persistent_app_instance_models: List[main_models.ListPersistentAppInstancesResponseBodyPersistentAppInstanceModels] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The app instances of the persistent session type.
        self.persistent_app_instance_models = persistent_app_instance_models
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.persistent_app_instance_models:
            for v1 in self.persistent_app_instance_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PersistentAppInstanceModels'] = []
        if self.persistent_app_instance_models is not None:
            for k1 in self.persistent_app_instance_models:
                result['PersistentAppInstanceModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.persistent_app_instance_models = []
        if m.get('PersistentAppInstanceModels') is not None:
            for k1 in m.get('PersistentAppInstanceModels'):
                temp_model = main_models.ListPersistentAppInstancesResponseBodyPersistentAppInstanceModels()
                self.persistent_app_instance_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPersistentAppInstancesResponseBodyPersistentAppInstanceModels(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        app_instance_persistent_name: str = None,
        app_instance_persistent_status: str = None,
        app_instance_status: str = None,
        authorized_users: List[str] = None,
        gmt_create: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the app instance.
        self.app_instance_id = app_instance_id
        # The ID of the app instance of the persistent session type.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The name of the app instance of the persistent session type.
        self.app_instance_persistent_name = app_instance_persistent_name
        # The status of the app instance of the persistent session type.
        # 
        # Valid values:
        # 
        # *   STARTING
        # *   RUNNING
        # *   STOPPED
        # *   UNAVAILABLE
        # *   DELETING
        # *   PENDING
        # *   STOPPING
        # *   DELETED
        # *   REBUILDING
        self.app_instance_persistent_status = app_instance_persistent_status
        # The status of the app instance.
        # 
        # Valid values:
        # 
        # *   INIT: The app instance is being initialized.
        # *   STARTING: The app instance is being started.
        # *   CLOSING: The app instance is being stopped.
        # *   CLOSED: The app instance is closed.
        # *   RUNNING: The app instance is running.
        # *   idle: The app instance is idle.
        # *   BOUND: The app instance is bound to an app instance group.
        # *   UNAVAILABLE: The app instance is unavailable.
        # *   DELETED: The app instance is deleted.
        self.app_instance_status = app_instance_status
        # The authorized users.
        self.authorized_users = authorized_users
        # The time when the app instance was created.
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.app_instance_persistent_name is not None:
            result['AppInstancePersistentName'] = self.app_instance_persistent_name

        if self.app_instance_persistent_status is not None:
            result['AppInstancePersistentStatus'] = self.app_instance_persistent_status

        if self.app_instance_status is not None:
            result['AppInstanceStatus'] = self.app_instance_status

        if self.authorized_users is not None:
            result['AuthorizedUsers'] = self.authorized_users

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('AppInstancePersistentName') is not None:
            self.app_instance_persistent_name = m.get('AppInstancePersistentName')

        if m.get('AppInstancePersistentStatus') is not None:
            self.app_instance_persistent_status = m.get('AppInstancePersistentStatus')

        if m.get('AppInstanceStatus') is not None:
            self.app_instance_status = m.get('AppInstanceStatus')

        if m.get('AuthorizedUsers') is not None:
            self.authorized_users = m.get('AuthorizedUsers')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        return self

