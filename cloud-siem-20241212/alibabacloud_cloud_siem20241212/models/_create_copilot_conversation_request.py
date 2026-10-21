# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCopilotConversationRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        model: str = None,
        plan_mode: str = None,
        project_id: str = None,
        region_id: str = None,
        thinking_mode: str = None,
        title: str = None,
        trace_id: str = None,
    ):
        # The language of the response messages. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The model identifier.
        self.model = model
        # The planning configuration.
        self.plan_mode = plan_mode
        # The security project ID.
        self.project_id = project_id
        # The region where the data management center for threat analysis is located. Select the management center region based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland.
        # - ap-southeast-1: Assets are located outside China.
        self.region_id = region_id
        # The thinking mode configuration.
        self.thinking_mode = thinking_mode
        # The session title.
        self.title = title
        # The trace ID of the created span object.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.model is not None:
            result['Model'] = self.model

        if self.plan_mode is not None:
            result['PlanMode'] = self.plan_mode

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.thinking_mode is not None:
            result['ThinkingMode'] = self.thinking_mode

        if self.title is not None:
            result['Title'] = self.title

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('PlanMode') is not None:
            self.plan_mode = m.get('PlanMode')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ThinkingMode') is not None:
            self.thinking_mode = m.get('ThinkingMode')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

