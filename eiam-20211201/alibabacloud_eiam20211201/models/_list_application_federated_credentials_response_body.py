# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationFederatedCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        application_federated_credentials: List[main_models.ListApplicationFederatedCredentialsResponseBodyApplicationFederatedCredentials] = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.application_federated_credentials = application_federated_credentials
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        # 本次调用返回的查询凭证（Token）值，用于上一次翻页查询。
        self.previous_token = previous_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.application_federated_credentials:
            for v1 in self.application_federated_credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationFederatedCredentials'] = []
        if self.application_federated_credentials is not None:
            for k1 in self.application_federated_credentials:
                result['ApplicationFederatedCredentials'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_federated_credentials = []
        if m.get('ApplicationFederatedCredentials') is not None:
            for k1 in m.get('ApplicationFederatedCredentials'):
                temp_model = main_models.ListApplicationFederatedCredentialsResponseBodyApplicationFederatedCredentials()
                self.application_federated_credentials.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationFederatedCredentialsResponseBodyApplicationFederatedCredentials(DaraModel):
    def __init__(
        self,
        application_federated_credential_id: str = None,
        application_federated_credential_name: str = None,
        application_federated_credential_type: str = None,
        application_id: str = None,
        create_time: int = None,
        description: str = None,
        federated_credential_provider_id: str = None,
        instance_id: str = None,
        last_used_time: int = None,
        status: str = None,
        update_time: int = None,
    ):
        # 应用联邦凭证ID
        self.application_federated_credential_id = application_federated_credential_id
        # 应用联邦凭证名称
        self.application_federated_credential_name = application_federated_credential_name
        # 应用联邦凭证类型
        self.application_federated_credential_type = application_federated_credential_type
        # 应用ID
        self.application_id = application_id
        # 创建时间
        self.create_time = create_time
        # 应用联邦凭证描述
        self.description = description
        # 应用联邦凭证提供者ID
        self.federated_credential_provider_id = federated_credential_provider_id
        # EAIM 实例ID
        self.instance_id = instance_id
        # 最近使用时间
        self.last_used_time = last_used_time
        # 应用联邦凭证状态
        self.status = status
        # 更新时间
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_federated_credential_id is not None:
            result['ApplicationFederatedCredentialId'] = self.application_federated_credential_id

        if self.application_federated_credential_name is not None:
            result['ApplicationFederatedCredentialName'] = self.application_federated_credential_name

        if self.application_federated_credential_type is not None:
            result['ApplicationFederatedCredentialType'] = self.application_federated_credential_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.federated_credential_provider_id is not None:
            result['FederatedCredentialProviderId'] = self.federated_credential_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredentialId') is not None:
            self.application_federated_credential_id = m.get('ApplicationFederatedCredentialId')

        if m.get('ApplicationFederatedCredentialName') is not None:
            self.application_federated_credential_name = m.get('ApplicationFederatedCredentialName')

        if m.get('ApplicationFederatedCredentialType') is not None:
            self.application_federated_credential_type = m.get('ApplicationFederatedCredentialType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederatedCredentialProviderId') is not None:
            self.federated_credential_provider_id = m.get('FederatedCredentialProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

