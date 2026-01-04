# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionIspsResponseBody(DaraModel):
    def __init__(
        self,
        isps: List[main_models.DescribeRegionIspsResponseBodyIsps] = None,
        request_id: str = None,
    ):
        # The list of ISPs.
        self.isps = isps
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.isps:
            for v1 in self.isps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Isps'] = []
        if self.isps is not None:
            for k1 in self.isps:
                result['Isps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isps = []
        if m.get('Isps') is not None:
            for k1 in m.get('Isps'):
                temp_model = main_models.DescribeRegionIspsResponseBodyIsps()
                self.isps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionIspsResponseBodyIsps(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The code of the ISP.
        self.code = code
        # The name of the ISP.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

