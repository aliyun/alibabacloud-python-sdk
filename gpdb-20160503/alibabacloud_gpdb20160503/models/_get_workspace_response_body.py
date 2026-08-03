# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        apikeys: List[main_models.GetWorkspaceResponseBodyApikeys] = None,
        create_time: str = None,
        request_id: str = None,
        services: List[main_models.GetWorkspaceResponseBodyServices] = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The list of workspace API keys.
        self.apikeys = apikeys
        # The creation time.
        self.create_time = create_time
        # The request ID.
        self.request_id = request_id
        # The list of service details.
        self.services = services
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name

    def validate(self):
        if self.apikeys:
            for v1 in self.apikeys:
                 if v1:
                    v1.validate()
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Apikeys'] = []
        if self.apikeys is not None:
            for k1 in self.apikeys:
                result['Apikeys'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apikeys = []
        if m.get('Apikeys') is not None:
            for k1 in m.get('Apikeys'):
                temp_model = main_models.GetWorkspaceResponseBodyApikeys()
                self.apikeys.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.GetWorkspaceResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class GetWorkspaceResponseBodyServices(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        cu: str = None,
        expire_time: str = None,
        pay_type: str = None,
        service_id: str = None,
        service_name: str = None,
        service_type: str = None,
        status: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The compute resource.
        self.cu = cu
        # The expiration time.
        self.expire_time = expire_time
        # The billing type. Valid values:
        # 
        # - **POSTPAY**: pay-as-you-go.
        # - **PREPAY**: subscription.
        # 
        # > - If this parameter is not specified, the default value is pay-as-you-go.
        # > - In subscription billing mode, a discount is available when you purchase a duration of one year or longer. Select a billing type as needed.
        self.pay_type = pay_type
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The service type. Valid values:
        # 
        # - **memory**
        # - **drama**
        self.service_type = service_type
        # The service status. Valid values:
        # - creating: being created.
        # - active: running.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetWorkspaceResponseBodyApikeys(DaraModel):
    def __init__(
        self,
        auth_services: List[main_models.GetWorkspaceResponseBodyApikeysAuthServices] = None,
        create_time: str = None,
        description: str = None,
        key_id: str = None,
        key_name: str = None,
        key_prefix: str = None,
    ):
        # The service ID.
        self.auth_services = auth_services
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # The ID of the API key.
        self.key_id = key_id
        # The name of the API key.
        self.key_name = key_name
        # The prefix of the API key.
        self.key_prefix = key_prefix

    def validate(self):
        if self.auth_services:
            for v1 in self.auth_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthServices'] = []
        if self.auth_services is not None:
            for k1 in self.auth_services:
                result['AuthServices'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_services = []
        if m.get('AuthServices') is not None:
            for k1 in m.get('AuthServices'):
                temp_model = main_models.GetWorkspaceResponseBodyApikeysAuthServices()
                self.auth_services.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')

        return self

class GetWorkspaceResponseBodyApikeysAuthServices(DaraModel):
    def __init__(
        self,
        service_id: str = None,
        service_type: str = None,
    ):
        # The service ID.
        self.service_id = service_id
        # The service type. Valid values:
        # 
        # - memory
        # - drama
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

