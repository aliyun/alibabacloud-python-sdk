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
        self.city = city
        self.idc_probe = idc_probe
        self.ipv_4 = ipv_4
        self.ipv_6 = ipv_6
        self.isp = isp
        self.lm_probe = lm_probe
        self.mb_probe = mb_probe
        self.region_id = region_id
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

