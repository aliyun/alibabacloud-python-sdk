# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustomDomainSampleRateRequest(DaraModel):
    def __init__(
        self,
        base_config_id: str = None,
        domain_names: str = None,
        sample_rate: float = None,
        sink_id: int = None,
    ):
        self.base_config_id = base_config_id
        self.domain_names = domain_names
        self.sample_rate = sample_rate
        self.sink_id = sink_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_config_id is not None:
            result['BaseConfigID'] = self.base_config_id

        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.sink_id is not None:
            result['SinkID'] = self.sink_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseConfigID') is not None:
            self.base_config_id = m.get('BaseConfigID')

        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('SinkID') is not None:
            self.sink_id = m.get('SinkID')

        return self

