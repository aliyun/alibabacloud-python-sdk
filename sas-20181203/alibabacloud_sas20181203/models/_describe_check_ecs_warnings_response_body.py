# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckEcsWarningsResponseBody(DaraModel):
    def __init__(
        self,
        can_try: str = None,
        request_id: str = None,
        sas_version: str = None,
        weak_password_count: str = None,
    ):
        # Indicates whether you use the free trial of Security Center. Valid values:
        # - **0**: no
        # - **1**: yes
        self.can_try = can_try
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The edition of Security Center that you use. Valid values:
        # 
        # *   **1**: Basic edition
        # *   **2** or **3**: Enterprise edition
        # *   **5**: Advanced edition
        # *   **6**: Anti-virus edition
        # 
        # >  Both the value 2 and the value 3 indicate the Enterprise edition.
        self.sas_version = sas_version
        # The number of weak passwords that can cause high risks to your assets.
        self.weak_password_count = weak_password_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_try is not None:
            result['CanTry'] = self.can_try

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sas_version is not None:
            result['SasVersion'] = self.sas_version

        if self.weak_password_count is not None:
            result['WeakPasswordCount'] = self.weak_password_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanTry') is not None:
            self.can_try = m.get('CanTry')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SasVersion') is not None:
            self.sas_version = m.get('SasVersion')

        if m.get('WeakPasswordCount') is not None:
            self.weak_password_count = m.get('WeakPasswordCount')

        return self

