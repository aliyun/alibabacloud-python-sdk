# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetUserProvisioningStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning_statistics: main_models.GetUserProvisioningStatisticsResponseBodyUserProvisioningStatistics = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics of the RAM user provisioning.
        self.user_provisioning_statistics = user_provisioning_statistics

    def validate(self):
        if self.user_provisioning_statistics:
            self.user_provisioning_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_provisioning_statistics is not None:
            result['UserProvisioningStatistics'] = self.user_provisioning_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserProvisioningStatistics') is not None:
            temp_model = main_models.GetUserProvisioningStatisticsResponseBodyUserProvisioningStatistics()
            self.user_provisioning_statistics = temp_model.from_map(m.get('UserProvisioningStatistics'))

        return self

class GetUserProvisioningStatisticsResponseBodyUserProvisioningStatistics(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        entity_id: str = None,
        failed_event_count: int = None,
        latest_async_time: str = None,
        owner_pk: str = None,
        type: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The entity ID, which is the ID of the RAM user provisioning.
        self.entity_id = entity_id
        # The number of failed RAM user provisioning events that are associated with the RAM user provisioning.
        self.failed_event_count = failed_event_count
        # The time when the RAM user provisioning was last performed.
        self.latest_async_time = latest_async_time
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The entity type. The value is fixed as `User Provisioning`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.failed_event_count is not None:
            result['FailedEventCount'] = self.failed_event_count

        if self.latest_async_time is not None:
            result['LatestAsyncTime'] = self.latest_async_time

        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('FailedEventCount') is not None:
            self.failed_event_count = m.get('FailedEventCount')

        if m.get('LatestAsyncTime') is not None:
            self.latest_async_time = m.get('LatestAsyncTime')

        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

