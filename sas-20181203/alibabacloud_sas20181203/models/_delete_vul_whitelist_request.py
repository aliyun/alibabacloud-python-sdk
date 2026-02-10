# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVulWhitelistRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        whitelist: str = None,
    ):
        # The ID of the whitelist.
        # 
        # >  To delete a vulnerability whitelist, you must provide the ID of the whitelist. You can call the [DescribeVulWhitelist](~~DescribeVulWhitelist~~) operation to query the IDs of whitelists.
        self.id = id
        # The information about the whitelist. The value is a JSON string that contains the following fields:
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
        # *   **AliasName**: the alias of the vulnerability.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

