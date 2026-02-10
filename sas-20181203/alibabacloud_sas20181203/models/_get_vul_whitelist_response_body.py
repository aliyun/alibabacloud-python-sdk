# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetVulWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vul_whitelist: main_models.GetVulWhitelistResponseBodyVulWhitelist = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the whitelist.
        self.vul_whitelist = vul_whitelist

    def validate(self):
        if self.vul_whitelist:
            self.vul_whitelist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vul_whitelist is not None:
            result['VulWhitelist'] = self.vul_whitelist.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VulWhitelist') is not None:
            temp_model = main_models.GetVulWhitelistResponseBodyVulWhitelist()
            self.vul_whitelist = temp_model.from_map(m.get('VulWhitelist'))

        return self

class GetVulWhitelistResponseBodyVulWhitelist(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        id: int = None,
        name: str = None,
        reason: str = None,
        target: str = None,
        type: str = None,
        whitelist: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The ID of the whitelist.
        self.id = id
        # The name of the vulnerability.
        self.name = name
        # The reason why the vulnerability is added to the whitelist.
        self.reason = reason
        # The application scope of the rule. The value is a JSON string that contains the following fields:
        # 
        # *   **type**: the type of the assets to which the rule is applied. Valid values:
        # 
        #     *   **Uuid**: server
        #     *   **GroupId**: server group
        # 
        # *   **groupIds**: the ID of the server group
        # 
        # *   **uuids**: the UUID of the server
        # 
        # > If this parameter is empty, the rule is applied to all types of assets.
        self.target = target
        # The type of the vulnerability.
        self.type = type
        # The information about the vulnerability that is added to the whitelist. The value is a JSON string that contains the following fields:
        # 
        # *   **Name**: the name of the vulnerability.
        # 
        # *   **Type**: the type of the vulnerability. Valid values:
        # 
        #     *   **cve**: Linux software vulnerability
        #     *   **sys**: Windows system vulnerability
        #     *   **cms**: Web-CMS vulnerability
        #     *   **app**: application vulnerability
        #     *   **emg**: urgent vulnerabilities
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
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

