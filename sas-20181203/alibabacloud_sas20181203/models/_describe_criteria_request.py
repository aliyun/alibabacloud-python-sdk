# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCriteriaRequest(DaraModel):
    def __init__(
        self,
        machine_types: str = None,
        resource_directory_account_id: int = None,
        support_auto_tag: bool = None,
        value: str = None,
    ):
        # The Asset Type to query. Valid values:
        # 
        # - **ecs**: queries all ECS servers.
        self.machine_types = machine_types
        # The ID of the Alibaba Cloud account of the member accounts in the resource folder.
        # >Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether the fuzzy query field supports automatic matching. Default value: **false**. Valid values:
        # 
        # - **true**: Supported.
        # - **false**: Not supported.
        self.support_auto_tag = support_auto_tag
        # The fuzzy match value entered when querying assets.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.support_auto_tag is not None:
            result['SupportAutoTag'] = self.support_auto_tag

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SupportAutoTag') is not None:
            self.support_auto_tag = m.get('SupportAutoTag')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

