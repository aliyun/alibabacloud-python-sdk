# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveIpInfoResponseBody(DaraModel):
    def __init__(
        self,
        isp: str = None,
        isp_ename: str = None,
        region: str = None,
        region_ename: str = None,
        request_id: str = None,
    ):
        # The Chinese name of the ISP.
        self.isp = isp
        # The English name of the Internet service provider (ISP).
        self.isp_ename = isp_ename
        # The Chinese name of the region.
        self.region = region
        # The English name of the region.
        self.region_ename = region_ename
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isp is not None:
            result['ISP'] = self.isp

        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename

        if self.region is not None:
            result['Region'] = self.region

        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

