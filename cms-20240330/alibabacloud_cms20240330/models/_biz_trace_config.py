# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BizTraceConfig(DaraModel):
    def __init__(
        self,
        advanced_config: str = None,
        biz_trace_code: str = None,
        biz_trace_id: str = None,
        biz_trace_name: str = None,
        create_time: str = None,
        region_id: str = None,
        rule_config: str = None,
        workspace: str = None,
    ):
        self.advanced_config = advanced_config
        self.biz_trace_code = biz_trace_code
        self.biz_trace_id = biz_trace_id
        self.biz_trace_name = biz_trace_name
        self.create_time = create_time
        self.region_id = region_id
        self.rule_config = rule_config
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_config is not None:
            result['advancedConfig'] = self.advanced_config

        if self.biz_trace_code is not None:
            result['bizTraceCode'] = self.biz_trace_code

        if self.biz_trace_id is not None:
            result['bizTraceId'] = self.biz_trace_id

        if self.biz_trace_name is not None:
            result['bizTraceName'] = self.biz_trace_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.rule_config is not None:
            result['ruleConfig'] = self.rule_config

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedConfig') is not None:
            self.advanced_config = m.get('advancedConfig')

        if m.get('bizTraceCode') is not None:
            self.biz_trace_code = m.get('bizTraceCode')

        if m.get('bizTraceId') is not None:
            self.biz_trace_id = m.get('bizTraceId')

        if m.get('bizTraceName') is not None:
            self.biz_trace_name = m.get('bizTraceName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('ruleConfig') is not None:
            self.rule_config = m.get('ruleConfig')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

