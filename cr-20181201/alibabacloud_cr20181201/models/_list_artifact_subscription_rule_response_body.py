# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListArtifactSubscriptionRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[main_models.ListArtifactSubscriptionRuleResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried artifact subscription rules.
        self.rules = rules
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for v1 in self.rules:
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

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListArtifactSubscriptionRuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListArtifactSubscriptionRuleResponseBodyRules(DaraModel):
    def __init__(
        self,
        accelerate: bool = None,
        create_time: int = None,
        instance_id: str = None,
        modified_time: int = None,
        namespace_name: str = None,
        override: bool = None,
        platform: List[str] = None,
        repo_name: str = None,
        rule_id: str = None,
        source_domain: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        tag_count: int = None,
        tag_regexp: str = None,
    ):
        # Indicates whether an acceleration link is enabled for image subscription. The subscription acceleration feature is in public preview. The feature is optimized based on scheduling policies and network links to accelerate image subscription.
        self.accelerate = accelerate
        # The time when the subscription rule was created.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The time when the subscription rule was modified.
        self.modified_time = modified_time
        # The name of the source namespace.
        self.namespace_name = namespace_name
        # Indicates whether the original image is overwritten.
        self.override = override
        # The operating system and architecture. If the source repository contains a multi-arch image, only the images with the specified operating system and architecture are subscribed to the destination repository of the Enterprise Edition instance.
        self.platform = platform
        # The name of the source repository.
        self.repo_name = repo_name
        # The rule ID.
        self.rule_id = rule_id
        self.source_domain = source_domain
        # The source namespace.
        self.source_namespace_name = source_namespace_name
        # The source of the artifact.
        # 
        # Valid values:
        # 
        # *   DOCKER_HUB: Docker Hub
        # *   GCR: GCR
        # *   QUAY: Quay.io
        self.source_provider = source_provider
        # The source repository.
        self.source_repo_name = source_repo_name
        # The number of subscribed images.
        self.tag_count = tag_count
        # The image tag in the subscription source repository. Regular expressions are supported.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerate') is not None:
            self.accelerate = m.get('Accelerate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')

        return self

