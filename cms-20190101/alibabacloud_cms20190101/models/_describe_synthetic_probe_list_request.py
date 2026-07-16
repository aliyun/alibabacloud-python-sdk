# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSyntheticProbeListRequest(DaraModel):
    def __init__(
        self,
        city: str = None,
        idc_probe: bool = None,
        ipv_4: bool = None,
        ipv_6: bool = None,
        isp: str = None,
        lm_probe: bool = None,
        mb_probe: bool = None,
        region_id: str = None,
        view_all: bool = None,
    ):
        # The name or ID of the city where the carrier detection point is located.
        self.city = city
        # Specifies whether to return only detection points in data centers.
        self.idc_probe = idc_probe
        # Specifies whether to return only IPv4 detection points.
        self.ipv_4 = ipv_4
        # Specifies whether to return only IPv6 detection points.
        self.ipv_6 = ipv_6
        # The name or ID of the carrier.
        self.isp = isp
        # Specifies whether to return only last-mile detection points.
        self.lm_probe = lm_probe
        # Specifies whether to return only mobile detection points.
        self.mb_probe = mb_probe
        self.region_id = region_id
        # Specifies whether to return all detection points. Valid values:
        # 
        # - false (default): Returns the detection points that are available to you.
        # 
        # - true: Returns all detection points.
        self.view_all = view_all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.idc_probe is not None:
            result['IdcProbe'] = self.idc_probe

        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4

        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.lm_probe is not None:
            result['LmProbe'] = self.lm_probe

        if self.mb_probe is not None:
            result['MbProbe'] = self.mb_probe

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.view_all is not None:
            result['ViewAll'] = self.view_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('IdcProbe') is not None:
            self.idc_probe = m.get('IdcProbe')

        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')

        if m.get('Ipv6') is not None:
            self.ipv_6 = m.get('Ipv6')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('LmProbe') is not None:
            self.lm_probe = m.get('LmProbe')

        if m.get('MbProbe') is not None:
            self.mb_probe = m.get('MbProbe')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ViewAll') is not None:
            self.view_all = m.get('ViewAll')

        return self

