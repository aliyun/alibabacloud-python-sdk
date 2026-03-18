# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRdStatusResponseBody(DaraModel):
    def __init__(
        self,
        current_uid: str = None,
        current_uid_type: str = None,
        enabled: bool = None,
        local_enable: bool = None,
        master_uid: str = None,
        remote_enable: bool = None,
        request_id: str = None,
        root_uid: str = None,
        service_principal_enabled: bool = None,
    ):
        # The Alibaba Cloud account ID of the current account.
        self.current_uid = current_uid
        # The type of the Alibaba Cloud account. Valid values:
        # 
        # *   **MasterAccount**: management account.
        # *   **DelegatedAdminAccount**: delegated administrator account.
        # *   **MemberAccount**: member.
        self.current_uid_type = current_uid_type
        # Indicates whether the multi-account management feature is enabled for Anti-DDoS Origin.
        self.enabled = enabled
        # Indicates whether the multi-account management feature is enabled for the current account in Anti-DDoS Origin.
        self.local_enable = local_enable
        # The Alibaba Cloud account ID of the management account in the resource directory.
        self.master_uid = master_uid
        # Indicates whether Resource Directory is enabled in the [Resource Management console](https://resourcemanager.console.aliyun.com).
        self.remote_enable = remote_enable
        # The request ID.
        self.request_id = request_id
        # The Alibaba Cloud account ID of the management account for which the multi-account management feature is enabled in Anti-DDoS Origin.
        self.root_uid = root_uid
        # Indicates whether the trusted service is enabled.
        self.service_principal_enabled = service_principal_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_uid is not None:
            result['CurrentUid'] = self.current_uid

        if self.current_uid_type is not None:
            result['CurrentUidType'] = self.current_uid_type

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.local_enable is not None:
            result['LocalEnable'] = self.local_enable

        if self.master_uid is not None:
            result['MasterUid'] = self.master_uid

        if self.remote_enable is not None:
            result['RemoteEnable'] = self.remote_enable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_uid is not None:
            result['RootUid'] = self.root_uid

        if self.service_principal_enabled is not None:
            result['ServicePrincipalEnabled'] = self.service_principal_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentUid') is not None:
            self.current_uid = m.get('CurrentUid')

        if m.get('CurrentUidType') is not None:
            self.current_uid_type = m.get('CurrentUidType')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('LocalEnable') is not None:
            self.local_enable = m.get('LocalEnable')

        if m.get('MasterUid') is not None:
            self.master_uid = m.get('MasterUid')

        if m.get('RemoteEnable') is not None:
            self.remote_enable = m.get('RemoteEnable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootUid') is not None:
            self.root_uid = m.get('RootUid')

        if m.get('ServicePrincipalEnabled') is not None:
            self.service_principal_enabled = m.get('ServicePrincipalEnabled')

        return self

