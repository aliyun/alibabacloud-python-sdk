# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoTriggerRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        trigger_name: str = None,
        trigger_tag: str = None,
        trigger_type: str = None,
        trigger_url: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The name of the trigger.
        # 
        # This parameter is required.
        self.trigger_name = trigger_name
        # The image tag based on which the trigger is set.
        # 
        # > 
        # 
        # *   If `TriggerType` is set to `ALL`, `TriggerTag` can be set to a string or an array, for example, `*`.
        # 
        # *   If `TriggerType` is set to `TAG_LIST`, `TriggerTag` must be set to an array, for example, `[1]`.
        # *   If `TriggerType` is set to `TAG_REG_EXP`, `TriggerTag` must be set to a string, for example, `*`.
        self.trigger_tag = trigger_tag
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LIST`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        # 
        # This parameter is required.
        self.trigger_type = trigger_type
        # The URL of the trigger.
        # 
        # This parameter is required.
        self.trigger_url = trigger_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name

        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')

        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')

        return self

