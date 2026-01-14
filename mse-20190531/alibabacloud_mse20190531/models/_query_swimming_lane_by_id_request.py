# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySwimmingLaneByIdRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        lane_id: int = None,
        namespace: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the lane.
        # 
        # This parameter is required.
        self.lane_id = lane_id
        # The name of the Microservices Engine (MSE) namespace.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

