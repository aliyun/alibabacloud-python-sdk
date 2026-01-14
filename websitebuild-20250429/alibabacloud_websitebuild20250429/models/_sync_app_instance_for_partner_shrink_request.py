# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncAppInstanceForPartnerShrinkRequest(DaraModel):
    def __init__(
        self,
        app_instance_shrink: str = None,
        event_type: str = None,
        operator: str = None,
        source_biz_id: str = None,
        source_type: str = None,
    ):
        self.app_instance_shrink = app_instance_shrink
        self.event_type = event_type
        self.operator = operator
        self.source_biz_id = source_biz_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_shrink is not None:
            result['AppInstance'] = self.app_instance_shrink

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            self.app_instance_shrink = m.get('AppInstance')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

