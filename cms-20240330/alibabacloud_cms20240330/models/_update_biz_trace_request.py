# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBizTraceRequest(DaraModel):
    def __init__(
        self,
        advanced_config: str = None,
        biz_trace_name: str = None,
        rule_config: str = None,
        workspace: str = None,
    ):
        self.advanced_config = advanced_config
        self.biz_trace_name = biz_trace_name
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

        if self.biz_trace_name is not None:
            result['bizTraceName'] = self.biz_trace_name

        if self.rule_config is not None:
            result['ruleConfig'] = self.rule_config

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedConfig') is not None:
            self.advanced_config = m.get('advancedConfig')

        if m.get('bizTraceName') is not None:
            self.biz_trace_name = m.get('bizTraceName')

        if m.get('ruleConfig') is not None:
            self.rule_config = m.get('ruleConfig')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

