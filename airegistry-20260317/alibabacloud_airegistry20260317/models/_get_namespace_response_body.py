# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class GetNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetNamespaceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetNamespaceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNamespaceResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        prompt_count: int = None,
        scan_policy: str = None,
        skill_count: int = None,
        source: str = None,
        source_index: int = None,
        tags: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.name = name
        self.namespace_id = namespace_id
        self.prompt_count = prompt_count
        self.scan_policy = scan_policy
        self.skill_count = skill_count
        self.source = source
        self.source_index = source_index
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.prompt_count is not None:
            result['PromptCount'] = self.prompt_count

        if self.scan_policy is not None:
            result['ScanPolicy'] = self.scan_policy

        if self.skill_count is not None:
            result['SkillCount'] = self.skill_count

        if self.source is not None:
            result['Source'] = self.source

        if self.source_index is not None:
            result['SourceIndex'] = self.source_index

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PromptCount') is not None:
            self.prompt_count = m.get('PromptCount')

        if m.get('ScanPolicy') is not None:
            self.scan_policy = m.get('ScanPolicy')

        if m.get('SkillCount') is not None:
            self.skill_count = m.get('SkillCount')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIndex') is not None:
            self.source_index = m.get('SourceIndex')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

