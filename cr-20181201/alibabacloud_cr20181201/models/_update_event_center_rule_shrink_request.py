# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEventCenterRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        event_channel: str = None,
        event_config: str = None,
        event_scope: str = None,
        event_type: str = None,
        instance_id: str = None,
        namespaces_shrink: str = None,
        repo_names_shrink: str = None,
        repo_tag_filter_pattern: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The event notification channel.
        self.event_channel = event_channel
        # The event configuration.
        self.event_config = event_config
        # The event scope. Valid values:
        # 
        # *   `INSTANCE`
        # *   `NAMESPACE`
        # *   `REPO`
        # 
        # Default value: `INSTANCE`
        self.event_scope = event_scope
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespaces to which the event notification rule applies.
        self.namespaces_shrink = namespaces_shrink
        # The names of the repositories to which the event notification rule applies.
        self.repo_names_shrink = repo_names_shrink
        # The regular expression for image tags.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        # The ID of the event notification rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the event notification rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel

        if self.event_config is not None:
            result['EventConfig'] = self.event_config

        if self.event_scope is not None:
            result['EventScope'] = self.event_scope

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespaces_shrink is not None:
            result['Namespaces'] = self.namespaces_shrink

        if self.repo_names_shrink is not None:
            result['RepoNames'] = self.repo_names_shrink

        if self.repo_tag_filter_pattern is not None:
            result['RepoTagFilterPattern'] = self.repo_tag_filter_pattern

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')

        if m.get('EventConfig') is not None:
            self.event_config = m.get('EventConfig')

        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespaces') is not None:
            self.namespaces_shrink = m.get('Namespaces')

        if m.get('RepoNames') is not None:
            self.repo_names_shrink = m.get('RepoNames')

        if m.get('RepoTagFilterPattern') is not None:
            self.repo_tag_filter_pattern = m.get('RepoTagFilterPattern')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

