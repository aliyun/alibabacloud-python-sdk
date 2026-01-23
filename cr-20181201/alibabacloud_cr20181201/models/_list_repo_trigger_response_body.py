# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoTriggerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        triggers: List[main_models.ListRepoTriggerResponseBodyTriggers] = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The triggers of the repository.
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for v1 in self.triggers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['Triggers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.triggers = []
        if m.get('Triggers') is not None:
            for k1 in m.get('Triggers'):
                temp_model = main_models.ListRepoTriggerResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class ListRepoTriggerResponseBodyTriggers(DaraModel):
    def __init__(
        self,
        repo_event: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_tag: str = None,
        trigger_type: str = None,
        trigger_url: str = None,
    ):
        # The type of the event that activates the trigger. Valid values:
        # 
        # *   `BUILD_SUCCESS`: The trigger is activated when an image building task is successful.
        # *   `BUILD_Fail`: The trigger is activated when an image building task fails.
        self.repo_event = repo_event
        # The ID of the trigger.
        self.trigger_id = trigger_id
        # The name of the trigger.
        self.trigger_name = trigger_name
        # The image tag based on which the trigger is set.
        self.trigger_tag = trigger_tag
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LISTTAG`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        self.trigger_type = trigger_type
        # The URL of the trigger.
        self.trigger_url = trigger_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.repo_event is not None:
            result['RepoEvent'] = self.repo_event

        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id

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
        if m.get('RepoEvent') is not None:
            self.repo_event = m.get('RepoEvent')

        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')

        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')

        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')

        return self

