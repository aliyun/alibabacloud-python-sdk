# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetVpcAccessResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_access_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the VPC access authorization.
        self.vpc_access_id = vpc_access_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpc_access_id is not None:
            result['VpcAccessId'] = self.vpc_access_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VpcAccessId') is not None:
            self.vpc_access_id = m.get('VpcAccessId')

        return self

