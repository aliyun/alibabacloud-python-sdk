# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetArtifactSubscriptionRuleResponseBody(DaraModel):
    def __init__(
        self,
        accelerate: bool = None,
        code: str = None,
        create_time: int = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        namespace_name: str = None,
        override: bool = None,
        platform: List[str] = None,
        repo_name: str = None,
        request_id: str = None,
        rule_id: str = None,
        source_domain: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        tag_count: int = None,
        tag_list: List[str] = None,
        tag_regexp: str = None,
    ):
        # Specifies whether to enable link acceleration. The subscription acceleration feature is in public preview and can improve image subscription speed through scheduling policies and network link optimization.
        self.accelerate = accelerate
        # The return code.
        self.code = code
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the API call was successful. Valid values:
        # 
        # - `true`: The API call was successful.
        # 
        # - `false`: The API call failed.
        self.is_success = is_success
        # The modification time. The value is a UNIX timestamp in milliseconds.
        self.modified_time = modified_time
        # The ACR namespace.
        self.namespace_name = namespace_name
        # Specifies whether to overwrite images.
        self.override = override
        # The operating system and architecture. If the source repository contains multi-architecture images, only images with the specified operating system and architecture are subscribed to the destination repository of the Enterprise instance.
        self.platform = platform
        # The ACR repository.
        self.repo_name = repo_name
        # The request ID.
        self.request_id = request_id
        # The rule ID.
        self.rule_id = rule_id
        # The domain name of the source image repository for the subscription rule.
        self.source_domain = source_domain
        # The source namespace.
        self.source_namespace_name = source_namespace_name
        # The artifact source.
        self.source_provider = source_provider
        # The source repository.
        self.source_repo_name = source_repo_name
        # The number of subscribed images.
        self.tag_count = tag_count
        # The list of subscribed tags.
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

        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.override is not None:
            result['Override'] = self.override

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.source_domain is not None:
            result['SourceDomain'] = self.source_domain

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

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('Override') is not None:
            self.override = m.get('Override')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('SourceDomain') is not None:
            self.source_domain = m.get('SourceDomain')

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

