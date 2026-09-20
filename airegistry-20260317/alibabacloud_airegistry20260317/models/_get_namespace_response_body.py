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
        # The namespace information.
        self.data = data
        # The request ID.
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
        ip_whitelist: str = None,
        name: str = None,
        namespace_id: str = None,
        prompt_count: int = None,
        public_access_enabled: bool = None,
        public_domain: str = None,
        scan_policy: str = None,
        skill_count: int = None,
        source: str = None,
        source_index: int = None,
        tags: str = None,
    ):
        # The time when the namespace was created.
        self.created_time = created_time
        # The description of the namespace.
        self.description = description
        self.ip_whitelist = ip_whitelist
        # The namespace name.
        self.name = name
        # The namespace ID.
        self.namespace_id = namespace_id
        # The number of prompts in the namespace.
        self.prompt_count = prompt_count
        self.public_access_enabled = public_access_enabled
        self.public_domain = public_domain
        # The scan policy.
        # 
        # The policy contains two configuration items:
        # - minBlockRiskLevel: the risk level for blocking.
        #   - high: blocks high-risk items.
        #   - medium: blocks medium- and high-risk items.
        #   - low: blocks all risk levels including high, medium, and low.
        # - maxSkipRatio: the maximum skip ratio. If the scan skip ratio exceeds this value, the scan is considered as failed.
        self.scan_policy = scan_policy
        # The number of skills in the namespace.
        self.skill_count = skill_count
        # The source of the namespace.
        self.source = source
        # The source ordinal number of the namespace.
        self.source_index = source_index
        # The tags of the namespace.
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

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.prompt_count is not None:
            result['PromptCount'] = self.prompt_count

        if self.public_access_enabled is not None:
            result['PublicAccessEnabled'] = self.public_access_enabled

        if self.public_domain is not None:
            result['PublicDomain'] = self.public_domain

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

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PromptCount') is not None:
            self.prompt_count = m.get('PromptCount')

        if m.get('PublicAccessEnabled') is not None:
            self.public_access_enabled = m.get('PublicAccessEnabled')

        if m.get('PublicDomain') is not None:
            self.public_domain = m.get('PublicDomain')

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

