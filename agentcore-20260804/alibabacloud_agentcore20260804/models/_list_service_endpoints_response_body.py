# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListServiceEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListServiceEndpointsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of service endpoints.
        self.items = items
        # The maximum number of records per page that takes effect for this query.
        self.max_results = max_results
        # The response message. An error description is returned if the request fails.
        self.message = message
        # The pagination token for the next page. This value is empty if no more pages exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of service endpoints that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListServiceEndpointsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListServiceEndpointsResponseBodyItems(DaraModel):
    def __init__(
        self,
        access_urls: List[main_models.ListServiceEndpointsResponseBodyItemsAccessUrls] = None,
        authentication: main_models.ListServiceEndpointsResponseBodyItemsAuthentication = None,
        created_at: str = None,
        endpoint_type: str = None,
        name: str = None,
        region_id: str = None,
        service_endpoint_id: str = None,
        status: str = None,
        status_reason: str = None,
        target: main_models.ListServiceEndpointsResponseBodyItemsTarget = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The list of access URLs for the service endpoint.
        self.access_urls = access_urls
        # The authentication configuration of the service endpoint.
        self.authentication = authentication
        # The creation time in UTC, formatted according to RFC 3339.
        self.created_at = created_at
        # The service endpoint type. DEFAULT indicates a default endpoint created and maintained by the platform. NAMED indicates a named endpoint explicitly created by the user.
        self.endpoint_type = endpoint_type
        # The service endpoint name. The name is unique within the workspace and is 1 to 128 characters in length.
        self.name = name
        # The region ID where the service endpoint is located.
        self.region_id = region_id
        # The service endpoint ID.
        self.service_endpoint_id = service_endpoint_id
        # The service endpoint status. Valid values: CREATING, READY, UPDATING, DEGRADED, DISABLED, DELETING.
        self.status = status
        # The reason for the service endpoint status. A specific reason is returned when the status is abnormal.
        self.status_reason = status_reason
        # The target routing configuration of the service endpoint.
        self.target = target
        # The last modification time in UTC, formatted according to RFC 3339.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.access_urls:
            for v1 in self.access_urls:
                 if v1:
                    v1.validate()
        if self.authentication:
            self.authentication.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['accessUrls'] = []
        if self.access_urls is not None:
            for k1 in self.access_urls:
                result['accessUrls'].append(k1.to_map() if k1 else None)

        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.endpoint_type is not None:
            result['endpointType'] = self.endpoint_type

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.target is not None:
            result['target'] = self.target.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_urls = []
        if m.get('accessUrls') is not None:
            for k1 in m.get('accessUrls'):
                temp_model = main_models.ListServiceEndpointsResponseBodyItemsAccessUrls()
                self.access_urls.append(temp_model.from_map(k1))

        if m.get('authentication') is not None:
            temp_model = main_models.ListServiceEndpointsResponseBodyItemsAuthentication()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('endpointType') is not None:
            self.endpoint_type = m.get('endpointType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('target') is not None:
            temp_model = main_models.ListServiceEndpointsResponseBodyItemsTarget()
            self.target = temp_model.from_map(m.get('target'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListServiceEndpointsResponseBodyItemsTarget(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        collaboration_component: str = None,
        resource_binding_id: str = None,
        target_type: str = None,
    ):
        # The target agent ID. This parameter is returned when the target type is AGENT_VERSION.
        self.agent_id = agent_id
        # The target agent version number. This parameter is returned when the target type is AGENT_VERSION.
        self.agent_version = agent_version
        # The collaboration component type. This parameter is returned when the target type is TEAM_COLLABORATION.
        self.collaboration_component = collaboration_component
        # The workspace resource binding ID associated with the target collaboration component. This parameter is returned when the target type is TEAM_COLLABORATION.
        self.resource_binding_id = resource_binding_id
        # The target type. Valid values: AGENT_VERSION, TEAM_COLLABORATION.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.collaboration_component is not None:
            result['collaborationComponent'] = self.collaboration_component

        if self.resource_binding_id is not None:
            result['resourceBindingId'] = self.resource_binding_id

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('collaborationComponent') is not None:
            self.collaboration_component = m.get('collaborationComponent')

        if m.get('resourceBindingId') is not None:
            self.resource_binding_id = m.get('resourceBindingId')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

class ListServiceEndpointsResponseBodyItemsAuthentication(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The authentication method. NONE indicates that no authentication is required. API_KEY indicates that authentication is performed by passing an API key through the x-api-key request header.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListServiceEndpointsResponseBodyItemsAccessUrls(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        status: str = None,
        status_reason: str = None,
        url: str = None,
    ):
        # The access URL type. Valid values: INTERNET, VPC.
        self.access_type = access_type
        # The access URL status. Valid values: CREATING, READY, DEGRADED.
        self.status = status
        # The reason for the access URL status. A specific reason is returned when the status is abnormal.
        self.status_reason = status_reason
        # The access URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['accessType'] = self.access_type

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessType') is not None:
            self.access_type = m.get('accessType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

