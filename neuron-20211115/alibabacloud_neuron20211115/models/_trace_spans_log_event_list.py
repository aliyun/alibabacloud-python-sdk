# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class TraceSpansLogEventList(DaraModel):
    def __init__(
        self,
        log_event_tag_entry_list: List[main_models.TagEntry] = None,
    ):
        self.log_event_tag_entry_list = log_event_tag_entry_list

    def validate(self):
        if self.log_event_tag_entry_list:
            for v1 in self.log_event_tag_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['logEventTagEntryList'] = []
        if self.log_event_tag_entry_list is not None:
            for k1 in self.log_event_tag_entry_list:
                result['logEventTagEntryList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_event_tag_entry_list = []
        if m.get('logEventTagEntryList') is not None:
            for k1 in m.get('logEventTagEntryList'):
                temp_model = main_models.TagEntry()
                self.log_event_tag_entry_list.append(temp_model.from_map(k1))

        return self

