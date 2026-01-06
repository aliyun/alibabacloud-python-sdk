# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetAssistantCapabilityResponseBody(DaraModel):
    def __init__(
        self,
        assistant_description: str = None,
        can_handle: bool = None,
        capability_assessment: main_models.GetAssistantCapabilityResponseBodyCapabilityAssessment = None,
        request_id: str = None,
    ):
        self.assistant_description = assistant_description
        self.can_handle = can_handle
        self.capability_assessment = capability_assessment
        self.request_id = request_id

    def validate(self):
        if self.capability_assessment:
            self.capability_assessment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant_description is not None:
            result['assistantDescription'] = self.assistant_description

        if self.can_handle is not None:
            result['canHandle'] = self.can_handle

        if self.capability_assessment is not None:
            result['capabilityAssessment'] = self.capability_assessment.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistantDescription') is not None:
            self.assistant_description = m.get('assistantDescription')

        if m.get('canHandle') is not None:
            self.can_handle = m.get('canHandle')

        if m.get('capabilityAssessment') is not None:
            temp_model = main_models.GetAssistantCapabilityResponseBodyCapabilityAssessment()
            self.capability_assessment = temp_model.from_map(m.get('capabilityAssessment'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAssistantCapabilityResponseBodyCapabilityAssessment(DaraModel):
    def __init__(
        self,
        brief_capability: str = None,
        capability_list: List[main_models.GetAssistantCapabilityResponseBodyCapabilityAssessmentCapabilityList] = None,
    ):
        self.brief_capability = brief_capability
        self.capability_list = capability_list

    def validate(self):
        if self.capability_list:
            for v1 in self.capability_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brief_capability is not None:
            result['briefCapability'] = self.brief_capability

        result['capabilityList'] = []
        if self.capability_list is not None:
            for k1 in self.capability_list:
                result['capabilityList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('briefCapability') is not None:
            self.brief_capability = m.get('briefCapability')

        self.capability_list = []
        if m.get('capabilityList') is not None:
            for k1 in m.get('capabilityList'):
                temp_model = main_models.GetAssistantCapabilityResponseBodyCapabilityAssessmentCapabilityList()
                self.capability_list.append(temp_model.from_map(k1))

        return self

class GetAssistantCapabilityResponseBodyCapabilityAssessmentCapabilityList(DaraModel):
    def __init__(
        self,
        capability_overview: str = None,
        description: str = None,
        name: str = None,
    ):
        self.capability_overview = capability_overview
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capability_overview is not None:
            result['capabilityOverview'] = self.capability_overview

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilityOverview') is not None:
            self.capability_overview = m.get('capabilityOverview')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

