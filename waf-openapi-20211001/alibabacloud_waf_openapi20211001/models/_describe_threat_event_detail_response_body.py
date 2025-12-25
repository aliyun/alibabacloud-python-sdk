# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeThreatEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        threat_event_detail: main_models.DescribeThreatEventDetailResponseBodyThreatEventDetail = None,
    ):
        self.request_id = request_id
        self.threat_event_detail = threat_event_detail

    def validate(self):
        if self.threat_event_detail:
            self.threat_event_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.threat_event_detail is not None:
            result['ThreatEventDetail'] = self.threat_event_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ThreatEventDetail') is not None:
            temp_model = main_models.DescribeThreatEventDetailResponseBodyThreatEventDetail()
            self.threat_event_detail = temp_model.from_map(m.get('ThreatEventDetail'))

        return self

class DescribeThreatEventDetailResponseBodyThreatEventDetail(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        event_block: str = None,
        event_cnt: str = None,
        event_condition: str = None,
        event_intelligence: str = None,
        event_level: str = None,
        event_src: str = None,
        event_src_country: str = None,
        event_src_region: str = None,
        event_suggest: str = None,
        event_tag: str = None,
        is_persistent: int = None,
    ):
        self.end_time = end_time
        self.event_block = event_block
        self.event_cnt = event_cnt
        self.event_condition = event_condition
        self.event_intelligence = event_intelligence
        self.event_level = event_level
        self.event_src = event_src
        self.event_src_country = event_src_country
        self.event_src_region = event_src_region
        self.event_suggest = event_suggest
        self.event_tag = event_tag
        self.is_persistent = is_persistent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_block is not None:
            result['EventBlock'] = self.event_block

        if self.event_cnt is not None:
            result['EventCnt'] = self.event_cnt

        if self.event_condition is not None:
            result['EventCondition'] = self.event_condition

        if self.event_intelligence is not None:
            result['EventIntelligence'] = self.event_intelligence

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_src is not None:
            result['EventSrc'] = self.event_src

        if self.event_src_country is not None:
            result['EventSrcCountry'] = self.event_src_country

        if self.event_src_region is not None:
            result['EventSrcRegion'] = self.event_src_region

        if self.event_suggest is not None:
            result['EventSuggest'] = self.event_suggest

        if self.event_tag is not None:
            result['EventTag'] = self.event_tag

        if self.is_persistent is not None:
            result['IsPersistent'] = self.is_persistent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventBlock') is not None:
            self.event_block = m.get('EventBlock')

        if m.get('EventCnt') is not None:
            self.event_cnt = m.get('EventCnt')

        if m.get('EventCondition') is not None:
            self.event_condition = m.get('EventCondition')

        if m.get('EventIntelligence') is not None:
            self.event_intelligence = m.get('EventIntelligence')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventSrc') is not None:
            self.event_src = m.get('EventSrc')

        if m.get('EventSrcCountry') is not None:
            self.event_src_country = m.get('EventSrcCountry')

        if m.get('EventSrcRegion') is not None:
            self.event_src_region = m.get('EventSrcRegion')

        if m.get('EventSuggest') is not None:
            self.event_suggest = m.get('EventSuggest')

        if m.get('EventTag') is not None:
            self.event_tag = m.get('EventTag')

        if m.get('IsPersistent') is not None:
            self.is_persistent = m.get('IsPersistent')

        return self

