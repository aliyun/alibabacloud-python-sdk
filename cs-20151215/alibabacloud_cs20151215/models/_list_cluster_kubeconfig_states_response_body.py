# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListClusterKubeconfigStatesResponseBody(DaraModel):
    def __init__(
        self,
        page: main_models.ListClusterKubeconfigStatesResponseBodyPage = None,
        states: List[main_models.ListClusterKubeconfigStatesResponseBodyStates] = None,
    ):
        # The pagination information.
        self.page = page
        # The status list of the kubeconfig files associated with the cluster.
        self.states = states

    def validate(self):
        if self.page:
            self.page.validate()
        if self.states:
            for v1 in self.states:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page.to_map()

        result['states'] = []
        if self.states is not None:
            for k1 in self.states:
                result['states'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            temp_model = main_models.ListClusterKubeconfigStatesResponseBodyPage()
            self.page = temp_model.from_map(m.get('page'))

        self.states = []
        if m.get('states') is not None:
            for k1 in m.get('states'):
                temp_model = main_models.ListClusterKubeconfigStatesResponseBodyStates()
                self.states.append(temp_model.from_map(k1))

        return self

class ListClusterKubeconfigStatesResponseBodyStates(DaraModel):
    def __init__(
        self,
        account_display_name: str = None,
        account_id: str = None,
        account_name: str = None,
        account_state: str = None,
        account_type: str = None,
        cert_expire_time: str = None,
        cert_state: str = None,
        revokable: bool = None,
    ):
        # The displayed name or role name of the RAM user.
        self.account_display_name = account_display_name
        # The ID of an Alibaba Cloud account, RAM user, or RAM role.
        self.account_id = account_id
        # The logon name or role name of the RAM user.
        self.account_name = account_name
        # The status of the account.
        # 
        # *   Active: The account is active.
        # *   InActive: The account is locked.
        # *   Deleted: The account is deleted.
        self.account_state = account_state
        # The type of the account.
        # 
        # *   RootAccount: Alibaba Cloud account.
        # *   RamUser: RAM user.
        # *   RamRole: RAM role.
        self.account_type = account_type
        # The expiration time of the client certificate for the kubeconfig file.
        self.cert_expire_time = cert_expire_time
        # The status of the client certificate for the kubeconfig file.
        # 
        # *   Unexpired: The certificate is not expired.
        # *   Expired: The certificate is expired.
        # *   Unknown: The status of the certificate is unknown.
        self.cert_state = cert_state
        # Indicates whether the client certificate for the kubeconfig file can be revoked.
        self.revokable = revokable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_display_name is not None:
            result['account_display_name'] = self.account_display_name

        if self.account_id is not None:
            result['account_id'] = self.account_id

        if self.account_name is not None:
            result['account_name'] = self.account_name

        if self.account_state is not None:
            result['account_state'] = self.account_state

        if self.account_type is not None:
            result['account_type'] = self.account_type

        if self.cert_expire_time is not None:
            result['cert_expire_time'] = self.cert_expire_time

        if self.cert_state is not None:
            result['cert_state'] = self.cert_state

        if self.revokable is not None:
            result['revokable'] = self.revokable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account_display_name') is not None:
            self.account_display_name = m.get('account_display_name')

        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')

        if m.get('account_name') is not None:
            self.account_name = m.get('account_name')

        if m.get('account_state') is not None:
            self.account_state = m.get('account_state')

        if m.get('account_type') is not None:
            self.account_type = m.get('account_type')

        if m.get('cert_expire_time') is not None:
            self.cert_expire_time = m.get('cert_expire_time')

        if m.get('cert_state') is not None:
            self.cert_state = m.get('cert_state')

        if m.get('revokable') is not None:
            self.revokable = m.get('revokable')

        return self

class ListClusterKubeconfigStatesResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

