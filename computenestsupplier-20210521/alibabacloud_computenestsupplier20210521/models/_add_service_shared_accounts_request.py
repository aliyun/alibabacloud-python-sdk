# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class AddServiceSharedAccountsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_id: str = None,
        shared_accounts: List[main_models.AddServiceSharedAccountsRequestSharedAccounts] = None,
        type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The shared account and permissions of the service.
        # 
        # This parameter is required.
        self.shared_accounts = shared_accounts
        # The share type of the service. Default value: SharedAccount. Valid values:
        # 
        # *   SharedAccount: The service is shared by multiple accounts.
        # *   Reseller: The service is distributed.
        self.type = type

    def validate(self):
        if self.shared_accounts:
            for v1 in self.shared_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        result['SharedAccounts'] = []
        if self.shared_accounts is not None:
            for k1 in self.shared_accounts:
                result['SharedAccounts'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        self.shared_accounts = []
        if m.get('SharedAccounts') is not None:
            for k1 in m.get('SharedAccounts'):
                temp_model = main_models.AddServiceSharedAccountsRequestSharedAccounts()
                self.shared_accounts.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self



class AddServiceSharedAccountsRequestSharedAccounts(DaraModel):
    def __init__(
        self,
        permission: str = None,
        user_ali_uid: str = None,
    ):
        # The permissions on the service. Valid values:
        # 
        # *   Deployable: Permissions to deploy the service.
        # *   Accessible: Permissions to access the service.
        # 
        # This parameter is required.
        self.permission = permission
        # The Alibaba Cloud account ID of the user.
        # 
        # This parameter is required.
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission is not None:
            result['Permission'] = self.permission

        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')

        return self

