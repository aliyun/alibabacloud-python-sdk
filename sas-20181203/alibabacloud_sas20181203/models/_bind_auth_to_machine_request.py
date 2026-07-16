# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BindAuthToMachineRequest(DaraModel):
    def __init__(
        self,
        auth_version: int = None,
        auto_bind: int = None,
        bind: List[str] = None,
        bind_all: bool = None,
        criteria: str = None,
        is_pre_bind: int = None,
        logical_exp: str = None,
        ntm_version: str = None,
        pre_bind_order_id: int = None,
        resource_directory_account_id: int = None,
        un_bind: List[str] = None,
    ):
        # The authorization version of the asset. Valid values:
        # - **6**: Anti-virus Edition
        # - **5**: Advanced Edition
        # - **3**: Enterprise Edition
        # - **7**: Ultimate Edition
        # - **10**: Value-added Service Edition.
        self.auth_version = auth_version
        # Specifies whether to enable automatic binding. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.auto_bind = auto_bind
        # The UUIDs of the servers to bind.
        # 
        # > **Bind** and **UnBind** cannot both be empty.
        self.bind = bind
        # Specifies whether to bind all assets. Default value: **false**. Valid values:
        # 
        # - **true**: Bind all assets.
        # - **false**: Do not bind all assets.
        self.bind_all = bind_all
        # The search conditions for assets. This parameter is in JSON format. Note that the parameter values are case-sensitive.
        # > You can search for assets by instance ID, instance name, VPC ID, region, or public IP address. Call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported search conditions.
        self.criteria = criteria
        # Specifies whether this is a pre-binding operation. Valid values:
        # 
        # - **0**: No.
        # - **1**: Yes.
        # 
        # 
        # > After pre-binding is enabled, the corresponding authorization quota is automatically bound to the specified servers after the purchase is completed.
        self.is_pre_bind = is_pre_bind
        # The logical relationship among multiple search conditions. Default value: **OR**. Valid values:
        # - **OR**: The search conditions are evaluated with a logical OR.
        # - **AND**: The search conditions are evaluated with a logical AND.
        self.logical_exp = logical_exp
        # The order version associated with the pre-binding. Valid values:
        # 
        # - **level7**: Anti-virus Edition
        # - **level3**: Advanced Edition
        # - **level2**: Enterprise Edition
        # - **level8**: Ultimate Edition
        # - **level10**: Value-added service only.
        self.ntm_version = ntm_version
        # The order ID associated with the pre-binding.
        self.pre_bind_order_id = pre_bind_order_id
        # The ID of the member accounts in the resource folder (Alibaba Cloud account).
        # > Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The UUIDs of the servers to unbind.
        # > **Bind** and **UnBind** cannot both be empty.
        self.un_bind = un_bind

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.bind_all is not None:
            result['BindAll'] = self.bind_all

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.is_pre_bind is not None:
            result['IsPreBind'] = self.is_pre_bind

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.ntm_version is not None:
            result['NtmVersion'] = self.ntm_version

        if self.pre_bind_order_id is not None:
            result['PreBindOrderId'] = self.pre_bind_order_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.un_bind is not None:
            result['UnBind'] = self.un_bind

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('BindAll') is not None:
            self.bind_all = m.get('BindAll')

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('IsPreBind') is not None:
            self.is_pre_bind = m.get('IsPreBind')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('NtmVersion') is not None:
            self.ntm_version = m.get('NtmVersion')

        if m.get('PreBindOrderId') is not None:
            self.pre_bind_order_id = m.get('PreBindOrderId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('UnBind') is not None:
            self.un_bind = m.get('UnBind')

        return self

