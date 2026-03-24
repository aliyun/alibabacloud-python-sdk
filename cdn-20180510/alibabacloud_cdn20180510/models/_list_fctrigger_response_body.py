# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class ListFCTriggerResponseBody(DaraModel):
    def __init__(
        self,
        fctriggers: List[main_models.ListFCTriggerResponseBodyFCTriggers] = None,
        request_id: str = None,
    ):
        # The Function Compute triggers that are set for Alibaba Cloud CDN events.
        self.fctriggers = fctriggers
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fctriggers:
            for v1 in self.fctriggers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FCTriggers'] = []
        if self.fctriggers is not None:
            for k1 in self.fctriggers:
                result['FCTriggers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fctriggers = []
        if m.get('FCTriggers') is not None:
            for k1 in m.get('FCTriggers'):
                temp_model = main_models.ListFCTriggerResponseBodyFCTriggers()
                self.fctriggers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFCTriggerResponseBodyFCTriggers(DaraModel):
    def __init__(
        self,
        event_meta_name: str = None,
        event_meta_version: str = None,
        notes: str = None,
        role_arn: str = None,
        source_arn: str = None,
        trigger_arn: str = None,
    ):
        # The name of the event.
        self.event_meta_name = event_meta_name
        # The version of the event.
        self.event_meta_version = event_meta_version
        # The remarks.
        self.notes = notes
        # The Resource Access Management (RAM) role.
        self.role_arn = role_arn
        # The resources and filters for event listening.
        self.source_arn = source_arn
        # The trigger that corresponds to the Function Compute service.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name

        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version

        if self.notes is not None:
            result['Notes'] = self.notes

        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn

        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn

        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')

        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')

        if m.get('Notes') is not None:
            self.notes = m.get('Notes')

        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')

        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')

        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')

        return self

