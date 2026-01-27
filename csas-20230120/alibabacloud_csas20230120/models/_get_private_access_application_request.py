# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPrivateAccessApplicationRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        # The ID of the office application. You can obtain the value by calling the following operations:
        # 
        # *   [ListPrivateAccessApplications](~~ListPrivateAccessApplications~~): queries office applications.
        # *   [CreatePrivateAccessApplication](~~CreatePrivateAccessApplication~~): creates an office application.
        # 
        # This parameter is required.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        return self

