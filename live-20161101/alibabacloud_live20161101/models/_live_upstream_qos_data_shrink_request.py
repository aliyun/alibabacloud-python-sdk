# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LiveUpstreamQosDataShrinkRequest(DaraModel):
    def __init__(
        self,
        cdn_domains_shrink: str = None,
        cdn_isps_shrink: str = None,
        cdn_provinces_shrink: str = None,
        end_time: str = None,
        kwai_sidcs_shrink: str = None,
        kwai_tsc_shrink: str = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        start_time: str = None,
        upstream_domains_shrink: str = None,
    ):
        self.cdn_domains_shrink = cdn_domains_shrink
        self.cdn_isps_shrink = cdn_isps_shrink
        self.cdn_provinces_shrink = cdn_provinces_shrink
        # This parameter is required.
        self.end_time = end_time
        self.kwai_sidcs_shrink = kwai_sidcs_shrink
        self.kwai_tsc_shrink = kwai_tsc_shrink
        self.owner_id = owner_id
        self.region = region
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time
        self.upstream_domains_shrink = upstream_domains_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_domains_shrink is not None:
            result['CdnDomains'] = self.cdn_domains_shrink

        if self.cdn_isps_shrink is not None:
            result['CdnIsps'] = self.cdn_isps_shrink

        if self.cdn_provinces_shrink is not None:
            result['CdnProvinces'] = self.cdn_provinces_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.kwai_sidcs_shrink is not None:
            result['KwaiSidcs'] = self.kwai_sidcs_shrink

        if self.kwai_tsc_shrink is not None:
            result['KwaiTsc'] = self.kwai_tsc_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.upstream_domains_shrink is not None:
            result['UpstreamDomains'] = self.upstream_domains_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnDomains') is not None:
            self.cdn_domains_shrink = m.get('CdnDomains')

        if m.get('CdnIsps') is not None:
            self.cdn_isps_shrink = m.get('CdnIsps')

        if m.get('CdnProvinces') is not None:
            self.cdn_provinces_shrink = m.get('CdnProvinces')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('KwaiSidcs') is not None:
            self.kwai_sidcs_shrink = m.get('KwaiSidcs')

        if m.get('KwaiTsc') is not None:
            self.kwai_tsc_shrink = m.get('KwaiTsc')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UpstreamDomains') is not None:
            self.upstream_domains_shrink = m.get('UpstreamDomains')

        return self

