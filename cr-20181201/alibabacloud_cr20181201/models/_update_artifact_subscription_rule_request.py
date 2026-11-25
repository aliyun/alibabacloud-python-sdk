# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateArtifactSubscriptionRuleRequest(DaraModel):
    def __init__(
        self,
        accelerate: str = None,
        instance_id: str = None,
        namespace_name: str = None,
        override: str = None,
        platform: List[str] = None,
        repo_name: str = None,
        rule_id: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        tag_count: int = None,
        tag_list: List[str] = None,
        tag_regexp: str = None,
    ):
        # Specifies whether to enable the acceleration link. The subscription acceleration feature is in public preview. It improves the image subscription speed based on scheduling policies and network link optimization.
        self.accelerate = accelerate
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ACR namespace.
        self.namespace_name = namespace_name
        # Specifies whether to overwrite images.
        self.override = override
        # The operating system and architecture. If the source repository contains multi-architecture images, only images with the specified operating system and architecture are subscribed to the destination repository of the Enterprise instance.
        self.platform = platform
        # The ACR repository.
        self.repo_name = repo_name
        # The rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The source namespace.
        self.source_namespace_name = source_namespace_name
        # The artifact source.
        self.source_provider = source_provider
        # The source repository.
        self.source_repo_name = source_repo_name
        # The number of images to subscribe to.
        self.tag_count = tag_count
        # - The image tags to subscribe to when matching by tag list. A maximum of 10 tags are supported.
        # - This parameter is valid only when the rule is created by using tag list matching. It cannot be specified together with TagRegexp or TagCount.
        # - If this parameter is not specified or an empty list is specified, the original tag list is retained and cannot be cleared. The matching method cannot be modified. To modify the matching method, delete the rule and create a new one.
        self.tag_list = tag_list
        # The image versions in the source repository to subscribe to. Regular expressions are supported.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate is not None:
            result['Accelerate'] = self.accelerate

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.override is not None:
            result['Override'] = self.override

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name

        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider

        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name

        if self.tag_count is not None:
            result['TagCount'] = self.tag_count

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerate') is not None:
            self.accelerate = m.get('Accelerate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('Override') is not None:
            self.override = m.get('Override')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')

        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')

        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')

        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')

        return self

