# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDomainQpsWithCacheResponseBody(DaraModel):
    def __init__(
        self,
        blocks: List[str] = None,
        cache_hits: List[str] = None,
        cc_block_qps: List[str] = None,
        cc_js_qps: List[str] = None,
        interval: int = None,
        ip_block_qps: List[str] = None,
        precise_blocks: List[str] = None,
        precise_js_qps: List[str] = None,
        region_blocks: List[str] = None,
        request_id: str = None,
        start_time: int = None,
        totals: List[str] = None,
    ):
        self.blocks = blocks
        self.cache_hits = cache_hits
        self.cc_block_qps = cc_block_qps
        self.cc_js_qps = cc_js_qps
        self.interval = interval
        self.ip_block_qps = ip_block_qps
        self.precise_blocks = precise_blocks
        self.precise_js_qps = precise_js_qps
        self.region_blocks = region_blocks
        self.request_id = request_id
        self.start_time = start_time
        self.totals = totals

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blocks is not None:
            result['Blocks'] = self.blocks

        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits

        if self.cc_block_qps is not None:
            result['CcBlockQps'] = self.cc_block_qps

        if self.cc_js_qps is not None:
            result['CcJsQps'] = self.cc_js_qps

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.ip_block_qps is not None:
            result['IpBlockQps'] = self.ip_block_qps

        if self.precise_blocks is not None:
            result['PreciseBlocks'] = self.precise_blocks

        if self.precise_js_qps is not None:
            result['PreciseJsQps'] = self.precise_js_qps

        if self.region_blocks is not None:
            result['RegionBlocks'] = self.region_blocks

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.totals is not None:
            result['Totals'] = self.totals

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blocks') is not None:
            self.blocks = m.get('Blocks')

        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')

        if m.get('CcBlockQps') is not None:
            self.cc_block_qps = m.get('CcBlockQps')

        if m.get('CcJsQps') is not None:
            self.cc_js_qps = m.get('CcJsQps')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IpBlockQps') is not None:
            self.ip_block_qps = m.get('IpBlockQps')

        if m.get('PreciseBlocks') is not None:
            self.precise_blocks = m.get('PreciseBlocks')

        if m.get('PreciseJsQps') is not None:
            self.precise_js_qps = m.get('PreciseJsQps')

        if m.get('RegionBlocks') is not None:
            self.region_blocks = m.get('RegionBlocks')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Totals') is not None:
            self.totals = m.get('Totals')

        return self

