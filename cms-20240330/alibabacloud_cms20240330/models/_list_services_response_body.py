# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListServicesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[main_models.ListServicesResponseBodyServices] = None,
        total_count: int = None,
    ):
        # Maximum number of results to return, with a maximum value of 200
        self.max_results = max_results
        # Pagination token
        self.next_token = next_token
        # Request ID
        self.request_id = request_id
        # List of service information.
        self.services = services
        # Total count
        self.total_count = total_count

    def validate(self):
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['services'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.services = []
        if m.get('services') is not None:
            for k1 in m.get('services'):
                temp_model = main_models.ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListServicesResponseBodyServices(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        pid: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
        workspace: str = None,
    ):
        # Extended information.
        self.attributes = attributes
        # Creation time
        self.create_time = create_time
        # Service description, valid only when serviceType=RUM.
        self.description = description
        # Display name, valid only when serviceType=RUM.
        self.display_name = display_name
        # Historical compatible ARMS application ID
        self.pid = pid
        self.resource_group_id = resource_group_id
        # Service ID
        self.service_id = service_id
        # Service name
        self.service_name = service_name
        # Service status, valid only when serviceType=RUM.
        self.service_status = service_status
        # Service type
        self.service_type = service_type
        # Workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.pid is not None:
            result['pid'] = self.pid

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.service_status is not None:
            result['serviceStatus'] = self.service_status

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('pid') is not None:
            self.pid = m.get('pid')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

