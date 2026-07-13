# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProvidersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListIdentityProvidersResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.items = items
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListIdentityProvidersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIdentityProvidersResponseBodyItems(DaraModel):
    def __init__(
        self,
        identity_provider_type: str = None,
        instance_id: str = None,
        login_enabled: bool = None,
        status: str = None,
        sync_enabled: bool = None,
    ):
        self.identity_provider_type = identity_provider_type
        self.instance_id = instance_id
        self.login_enabled = login_enabled
        self.status = status
        self.sync_enabled = sync_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_enabled is not None:
            result['LoginEnabled'] = self.login_enabled

        if self.status is not None:
            result['Status'] = self.status

        if self.sync_enabled is not None:
            result['SyncEnabled'] = self.sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginEnabled') is not None:
            self.login_enabled = m.get('LoginEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SyncEnabled') is not None:
            self.sync_enabled = m.get('SyncEnabled')

        return self

