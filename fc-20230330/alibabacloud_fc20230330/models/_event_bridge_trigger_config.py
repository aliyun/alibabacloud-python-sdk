# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class EventBridgeTriggerConfig(DaraModel):
    def __init__(
        self,
        async_invocation_type: bool = None,
        event_rule_filter_pattern: str = None,
        event_sink_config: main_models.EventSinkConfig = None,
        event_source_config: main_models.EventSourceConfig = None,
        run_options: main_models.RunOptions = None,
        trigger_enable: bool = None,
    ):
        self.async_invocation_type = async_invocation_type
        self.event_rule_filter_pattern = event_rule_filter_pattern
        self.event_sink_config = event_sink_config
        self.event_source_config = event_source_config
        self.run_options = run_options
        self.trigger_enable = trigger_enable

    def validate(self):
        if self.event_sink_config:
            self.event_sink_config.validate()
        if self.event_source_config:
            self.event_source_config.validate()
        if self.run_options:
            self.run_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_invocation_type is not None:
            result['asyncInvocationType'] = self.async_invocation_type

        if self.event_rule_filter_pattern is not None:
            result['eventRuleFilterPattern'] = self.event_rule_filter_pattern

        if self.event_sink_config is not None:
            result['eventSinkConfig'] = self.event_sink_config.to_map()

        if self.event_source_config is not None:
            result['eventSourceConfig'] = self.event_source_config.to_map()

        if self.run_options is not None:
            result['runOptions'] = self.run_options.to_map()

        if self.trigger_enable is not None:
            result['triggerEnable'] = self.trigger_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncInvocationType') is not None:
            self.async_invocation_type = m.get('asyncInvocationType')

        if m.get('eventRuleFilterPattern') is not None:
            self.event_rule_filter_pattern = m.get('eventRuleFilterPattern')

        if m.get('eventSinkConfig') is not None:
            temp_model = main_models.EventSinkConfig()
            self.event_sink_config = temp_model.from_map(m.get('eventSinkConfig'))

        if m.get('eventSourceConfig') is not None:
            temp_model = main_models.EventSourceConfig()
            self.event_source_config = temp_model.from_map(m.get('eventSourceConfig'))

        if m.get('runOptions') is not None:
            temp_model = main_models.RunOptions()
            self.run_options = temp_model.from_map(m.get('runOptions'))

        if m.get('triggerEnable') is not None:
            self.trigger_enable = m.get('triggerEnable')

        return self

