# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCreateVulWhitelistRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        reason: str = None,
        resource_directory_account_id: int = None,
        target_info: str = None,
        whitelist: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Different requests must use different tokens. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The reason for adding the vulnerability to the whitelist.
        self.reason = reason
        self.resource_directory_account_id = resource_directory_account_id
        # The scope in which the whitelist takes effect. The value is a JSON string that contains the following fields:
        # - **type**: The scope type. Valid values:
        #     - **GroupId**: server group
        #     - **Uuid**: host asset
        # - **uuids**: The collection of host asset UUIDs. The field type is String.
        # - **groupIds**: The collection of server group IDs. The field type is Long.
        # > If this parameter is left empty, the whitelist takes effect on all hosts. If **type** is set to **GroupId**, **groupIds** cannot be empty. If **type** is set to **Uuid**, **uuids** cannot be empty.
        self.target_info = target_info
        # The information about the vulnerability to add to the whitelist. The value is a JSON string that contains the following fields:
        # 
        # - **Status**: The vulnerability status.
        # - **GmtLast**: The timestamp when the vulnerability was last detected. Unit: milliseconds.
        # - **LaterCount**: The number of medium-priority vulnerabilities.
        # - **AsapCount**: The number of high-priority vulnerabilities.
        # - **Name**: The vulnerability name.
        # - **Type**: The vulnerability type. Valid values:
        # 
        #     - **cve**: Linux software vulnerability
        #     - **sys**: Windows system vulnerability
        #     - **cms**: Web-CMS vulnerability
        #     - **app**: application vulnerability
        #     - **emg**: emergency vulnerability
        # 
        # - **Related**: The CVE ID of the vulnerability.
        # - **HandledCount**: The number of handled vulnerabilities.
        # - **AliasName**: The alias of the vulnerability.
        # - **RuleModifyTime**: The time when the vulnerability was last published.
        # - **NntfCount**: The number of low-priority vulnerabilities.
        # - **TotalFixCount**: The total number of fixed vulnerabilities.
        # - **Tags**: The vulnerability tags.
        # 
        # > You can call the [DescribeGroupedVul](~~DescribeGroupedVul~~) operation to obtain the vulnerability information to add to the whitelist.
        # 
        # This parameter is required.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.target_info is not None:
            result['TargetInfo'] = self.target_info

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('TargetInfo') is not None:
            self.target_info = m.get('TargetInfo')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

