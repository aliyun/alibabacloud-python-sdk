# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLogstoreStorageResponseBody(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        preserve: int = None,
        request_id: str = None,
        ttl: int = None,
        used: int = None,
        user_project: str = None,
    ):
        # The name of the dedicated Logstore that is used to store full logs of Security Center. The value is fixed as **sas-log**.
        self.logstore = logstore
        # The purchased log storage capacity, in GB.
        self.preserve = preserve
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of days during which logs can be retained. The value is fixed as **180**, which indicates that logs can be retained for 180 days.
        # 
        # >  You are not allowed to change the value of this parameter.
        self.ttl = ttl
        # The used log storage capacity, in GB.
        self.used = used
        # The name of the dedicated Project that is used to store full logs of Security Center.
        self.user_project = user_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.preserve is not None:
            result['Preserve'] = self.preserve

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.used is not None:
            result['Used'] = self.used

        if self.user_project is not None:
            result['UserProject'] = self.user_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Preserve') is not None:
            self.preserve = m.get('Preserve')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UserProject') is not None:
            self.user_project = m.get('UserProject')

        return self

