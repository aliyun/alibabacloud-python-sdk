# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateImageCacheRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateImageCacheRequestBody = None,
        client_token: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The business parameters for creating an image cache.
        # 
        # This parameter is required.
        self.body = body
        # This parameter is required and cannot be empty. It is reserved to be compatible with the API. Currently, it does not provide the ability to deduplicate requests or recover the original result based on this field. If a timeout occurs or the result is unconfirmed, query the query cache status first before deciding whether to recommit.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The product entry region, which is determined by the selected region endpoint.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The current routed workspace. The server verifies the account, region, and resource ownership. This parameter cannot be omitted or used to access other workspaces.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateImageCacheRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateImageCacheRequestBody(DaraModel):
    def __init__(
        self,
        access_internet: bool = None,
        access_vpc: bool = None,
        acr_instance_id: str = None,
        namespace: str = None,
        repository: str = None,
        tag: str = None,
    ):
        # Specifies whether to allow the current source reading and transfer to use the public network. At least one of this parameter and accessVpc must be set to true. The server verifies the access conditions of the current workspace.
        # 
        # This parameter is required.
        self.access_internet = access_internet
        # Specifies whether to allow the current source reading and transfer to use a VPC. At least one of this parameter and accessInternet must be set to true. The server parses the trusted network of the current workspace and does not modify the agent runtime network.
        # 
        # This parameter is required.
        self.access_vpc = access_vpc
        # The ID of the source ACR Enterprise instance.
        # 
        # This parameter is required.
        self.acr_instance_id = acr_instance_id
        # The namespace of the source ACR.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the repository under the namespace. Do not include the namespace repeatedly.
        # 
        # This parameter is required.
        self.repository = repository
        # The selected tag of the source image.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_internet is not None:
            result['accessInternet'] = self.access_internet

        if self.access_vpc is not None:
            result['accessVpc'] = self.access_vpc

        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.repository is not None:
            result['repository'] = self.repository

        if self.tag is not None:
            result['tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessInternet') is not None:
            self.access_internet = m.get('accessInternet')

        if m.get('accessVpc') is not None:
            self.access_vpc = m.get('accessVpc')

        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('repository') is not None:
            self.repository = m.get('repository')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        return self

