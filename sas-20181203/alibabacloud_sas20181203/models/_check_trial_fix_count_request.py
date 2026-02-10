# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CheckTrialFixCountRequest(DaraModel):
    def __init__(
        self,
        info: str = None,
        type: str = None,
        uuids: List[str] = None,
        vul_names: List[str] = None,
    ):
        # The information about the vulnerability. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **name**: the name of the vulnerability.
        # 
        # *   **uuid**: the UUID of the server on which the vulnerability is detected.
        # 
        # *   **tag**: the tag that is added to the vulnerability. Valid values:
        # 
        #     *   **oval**: Linux software vulnerability.
        #     *   **system**: Windows system vulnerability.
        #     *   **cms**: Web-CMS vulnerability.
        # 
        # >  You must specify a value for Info or values for VulNames and Uuids to identify a vulnerability.
        self.info = info
        # The type of the vulnerability that you want to fix. Valid values:
        # 
        # *   **cve**: Linux software vulnerability.
        # *   **sys**: Windows system vulnerability.
        # *   **cms**: Web-CMS vulnerability.
        # 
        # This parameter is required.
        self.type = type
        # The UUIDs of the servers.
        self.uuids = uuids
        # The names of the vulnerabilities.
        self.vul_names = vul_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.type is not None:
            result['Type'] = self.type

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.vul_names is not None:
            result['VulNames'] = self.vul_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('VulNames') is not None:
            self.vul_names = m.get('VulNames')

        return self

