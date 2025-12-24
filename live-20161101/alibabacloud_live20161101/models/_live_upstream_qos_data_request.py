# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class LiveUpstreamQosDataRequest(DaraModel):
    def __init__(
        self,
        cdn_domains: List[str] = None,
        cdn_isps: List[str] = None,
        cdn_provinces: List[str] = None,
        end_time: str = None,
        kwai_sidcs: List[str] = None,
        kwai_tsc: List[int] = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        start_time: str = None,
        upstream_domains: List[str] = None,
    ):
        self.cdn_domains = cdn_domains
        self.cdn_isps = cdn_isps
        self.cdn_provinces = cdn_provinces
        # This parameter is required.
        self.end_time = end_time
        self.kwai_sidcs = kwai_sidcs
        self.kwai_tsc = kwai_tsc
        self.owner_id = owner_id
        self.region = region
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time
        self.upstream_domains = upstream_domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_domains is not None:
            result['CdnDomains'] = self.cdn_domains

        if self.cdn_isps is not None:
            result['CdnIsps'] = self.cdn_isps

        if self.cdn_provinces is not None:
            result['CdnProvinces'] = self.cdn_provinces

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.kwai_sidcs is not None:
            result['KwaiSidcs'] = self.kwai_sidcs

        if self.kwai_tsc is not None:
            result['KwaiTsc'] = self.kwai_tsc

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.upstream_domains is not None:
            result['UpstreamDomains'] = self.upstream_domains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnDomains') is not None:
            self.cdn_domains = m.get('CdnDomains')

        if m.get('CdnIsps') is not None:
            self.cdn_isps = m.get('CdnIsps')

        if m.get('CdnProvinces') is not None:
            self.cdn_provinces = m.get('CdnProvinces')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('KwaiSidcs') is not None:
            self.kwai_sidcs = m.get('KwaiSidcs')

        if m.get('KwaiTsc') is not None:
            self.kwai_tsc = m.get('KwaiTsc')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UpstreamDomains') is not None:
            self.upstream_domains = m.get('UpstreamDomains')

        return self

