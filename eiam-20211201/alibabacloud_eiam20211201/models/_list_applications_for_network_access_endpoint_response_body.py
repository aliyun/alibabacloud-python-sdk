# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsForNetworkAccessEndpointResponseBody(DaraModel):
    def __init__(
        self,
        applications_for_network_access_endpoint: List[main_models.ListApplicationsForNetworkAccessEndpointResponseBodyApplicationsForNetworkAccessEndpoint] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.applications_for_network_access_endpoint = applications_for_network_access_endpoint
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.applications_for_network_access_endpoint:
            for v1 in self.applications_for_network_access_endpoint:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationsForNetworkAccessEndpoint'] = []
        if self.applications_for_network_access_endpoint is not None:
            for k1 in self.applications_for_network_access_endpoint:
                result['ApplicationsForNetworkAccessEndpoint'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications_for_network_access_endpoint = []
        if m.get('ApplicationsForNetworkAccessEndpoint') is not None:
            for k1 in m.get('ApplicationsForNetworkAccessEndpoint'):
                temp_model = main_models.ListApplicationsForNetworkAccessEndpointResponseBodyApplicationsForNetworkAccessEndpoint()
                self.applications_for_network_access_endpoint.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationsForNetworkAccessEndpointResponseBodyApplicationsForNetworkAccessEndpoint(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        instance_id: str = None,
    ):
        # 应用ID。
        self.application_id = application_id
        # 应用名称。
        self.application_name = application_name
        # IDaaS EIAM 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

