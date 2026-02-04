# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnStagingIpResponseBody(DaraModel):
    def __init__(
        self,
        ipv4s: main_models.DescribeDcdnStagingIpResponseBodyIPV4s = None,
        request_id: str = None,
    ):
        self.ipv4s = ipv4s
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ipv4s:
            self.ipv4s.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv4s is not None:
            result['IPV4s'] = self.ipv4s.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4s') is not None:
            temp_model = main_models.DescribeDcdnStagingIpResponseBodyIPV4s()
            self.ipv4s = temp_model.from_map(m.get('IPV4s'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnStagingIpResponseBodyIPV4s(DaraModel):
    def __init__(
        self,
        ipv4: List[str] = None,
    ):
        self.ipv4 = ipv4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')

        return self

