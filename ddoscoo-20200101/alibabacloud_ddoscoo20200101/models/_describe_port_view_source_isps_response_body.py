# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePortViewSourceIspsResponseBody(DaraModel):
    def __init__(
        self,
        isps: List[main_models.DescribePortViewSourceIspsResponseBodyIsps] = None,
        request_id: str = None,
    ):
        # An array that consists of the details of the ISP.
        self.isps = isps
        # The ID of the request.
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
                temp_model = main_models.DescribePortViewSourceIspsResponseBodyIsps()
                self.isps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortViewSourceIspsResponseBodyIsps(DaraModel):
    def __init__(
        self,
        count: int = None,
        isp_id: str = None,
    ):
        # The total number of requests that are sent from the ISP.
        # 
        # > This parameter does not indicate the accurate number of requests. You can use this parameter to calculate the proportion of requests from different ISPs.
        self.count = count
        # The ID of the ISP. For more information, see the ISP codes table.
        self.isp_id = isp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.isp_id is not None:
            result['IspId'] = self.isp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')

        return self

