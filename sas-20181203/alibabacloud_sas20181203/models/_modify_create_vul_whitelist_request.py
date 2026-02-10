# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCreateVulWhitelistRequest(DaraModel):
    def __init__(
        self,
        reason: str = None,
        target_info: str = None,
        whitelist: str = None,
    ):
        # The reason why you add the vulnerability to the whitelist.
        self.reason = reason
        # The applicable scope of the whitelist. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: the type of the applicable scope. Valid values:
        # 
        #     *   **GroupId**: the ID of a server group.
        #     *   **Uuid**: the UUID of a server.
        # 
        # *   **uuids**: the UUIDs of servers. This field is of the string type.
        # 
        # *   **groupIds**: the IDs of server groups. This field is of the long type.
        # 
        # >  If you leave this parameter empty, the applicable scope is all servers. If you set the **type** field to **GroupId**, you must also specify the **groupIds** field. If you set the **type** field to **Uuid**, you must also specify the **uuids** field.
        self.target_info = target_info
        # The information about the vulnerability that you want to add to the whitelist. The value is a JSON string that contains the following fields:
        # 
        # *   **Status**: the status of the vulnerability.
        # 
        # *   **GmtLast**: the timestamp when the vulnerability was last detected. Unit: milliseconds.
        # 
        # *   **LaterCount**: the number of vulnerabilities that have the medium priority.
        # 
        # *   **AsapCount**: the number of vulnerabilities that have the high priority.
        # 
        # *   **Name**: the name of the vulnerability.
        # 
        # *   **Type**: the type of the vulnerability. Valid values:
        # 
        #     *   **cve**: Linux software vulnerability
        #     *   **sys**: Windows system vulnerability
        #     *   **cms**: Web-CMS vulnerability
        #     *   **app**: application vulnerability
        #     *   **emg**: urgent vulnerability
        # 
        # *   **Related**: the Common Vulnerabilities and Exposures (CVE) ID of the vulnerability.
        # 
        # *   **HandledCount**: the number of handled vulnerabilities.
        # 
        # *   **AliasName**: the alias of the vulnerability.
        # 
        # *   **RuleModifyTime**: the time when the vulnerability was last disclosed.
        # 
        # *   **NntfCount**: the number of vulnerabilities that have the low priority.
        # 
        # *   **TotalFixCount**: the total number of fixed vulnerabilities.
        # 
        # *   **Tags**: the tag that is added to the vulnerability.
        # 
        # >  You can call the [DescribeGroupedVul](~~DescribeGroupedVul~~) operation to query the information about the vulnerability that you want to add to the whitelist.
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
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.target_info is not None:
            result['TargetInfo'] = self.target_info

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('TargetInfo') is not None:
            self.target_info = m.get('TargetInfo')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

