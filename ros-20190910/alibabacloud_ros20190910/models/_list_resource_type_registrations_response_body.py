# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListResourceTypeRegistrationsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        registrations: List[main_models.ListResourceTypeRegistrationsResponseBodyRegistrations] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The registration records of the resource.
        self.registrations = registrations
        # The request ID.
        self.request_id = request_id
        # The total number of registration records.
        self.total_count = total_count

    def validate(self):
        if self.registrations:
            for v1 in self.registrations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        result['Registrations'] = []
        if self.registrations is not None:
            for k1 in self.registrations:
                result['Registrations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        self.registrations = []
        if m.get('Registrations') is not None:
            for k1 in m.get('Registrations'):
                temp_model = main_models.ListResourceTypeRegistrationsResponseBodyRegistrations()
                self.registrations.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourceTypeRegistrationsResponseBodyRegistrations(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        entity_type: str = None,
        registration_id: str = None,
        resource_type: str = None,
        status: str = None,
        status_reason: str = None,
        version_id: str = None,
    ):
        # The creation time. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The entity type. Only Module may be returned.
        self.entity_type = entity_type
        # The ID of the registration record.
        self.registration_id = registration_id
        # The resource type.
        self.resource_type = resource_type
        # The registration state. Valid values:
        # 
        # *   IN_PROGRESS: The registration is in progress.
        # *   COMPLETE: The registration is successful.
        # *   FAILED: The registration failed.
        self.status = status
        # The reason for the state.
        self.status_reason = status_reason
        # The version ID.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

