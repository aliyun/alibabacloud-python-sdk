# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDefaultKeyInfoResponseBody(DaraModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        names: str = None,
        request_id: str = None,
    ):
        # The list of domain names.
        self.domain_list = domain_list
        # The company names.
        self.names = names
        # The ID of the request. The ID is a unique identifier that Alibaba Cloud generates for the request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.names is not None:
            result['Names'] = self.names

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

