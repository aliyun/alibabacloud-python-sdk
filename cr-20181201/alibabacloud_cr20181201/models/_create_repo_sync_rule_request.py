# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoSyncRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        link_id: str = None,
        namespace_name: str = None,
        namespace_name_filter: str = None,
        priority: int = None,
        repo_name: str = None,
        repo_name_filter: str = None,
        sync_rule_name: str = None,
        sync_scope: str = None,
        sync_trigger: str = None,
        tag_filter: str = None,
        target_instance_id: str = None,
        target_namespace_name: str = None,
        target_region_id: str = None,
        target_repo_name: str = None,
        target_user_id: str = None,
    ):
        # The ID of the source instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the custom synchronization link.
        self.link_id = link_id
        # The namespace name of the source instance.
        self.namespace_name = namespace_name
        # The instance-level namespace regex filter.
        # > This parameter takes effect only when SyncScope is set to `INSTANCE`.
        self.namespace_name_filter = namespace_name_filter
        # The execution priority of the synchronization task. Synchronization tasks are executed in descending order of priority. Tasks with the same priority are executed in random order.
        # 
        # Valid values: 1 to 5.
        # 
        # Default value: 3.
        self.priority = priority
        # The repository name of the source instance.
        self.repo_name = repo_name
        # The repository filter rule.
        # > This parameter takes effect only when SyncScope is set to `INSTANCE` or `NAMESPACE`.
        self.repo_name_filter = repo_name_filter
        # The name of the synchronization rule.
        # 
        # This parameter is required.
        self.sync_rule_name = sync_rule_name
        # The synchronization type. Valid values:
        # 
        # - `REPO`: Synchronizes by image repository.
        # 
        # - `NAMESPACE`: Synchronizes by namespace.
        # 
        # - `INSTANCE`: Synchronizes by namespace regex and repository regex.
        # 
        # This parameter is required.
        self.sync_scope = sync_scope
        # The trigger for the synchronization action. Valid values:
        # 
        # - `INITIATIVE`: Manual trigger.
        #  
        # - `PASSIVE`: Automatic trigger.
        self.sync_trigger = sync_trigger
        # The tag filter rule.
        # 
        # This parameter is required.
        self.tag_filter = tag_filter
        # The ID of the target instance.
        # 
        # This parameter is required.
        self.target_instance_id = target_instance_id
        # The namespace name of the target instance.
        self.target_namespace_name = target_namespace_name
        # The region ID of the target instance.
        # 
        # This parameter is required.
        self.target_region_id = target_region_id
        # The image repository name of the target instance.
        self.target_repo_name = target_repo_name
        # The UID of the account to which the target instance belongs.
        # 
        # > This parameter is required for cross-account image synchronization.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.namespace_name_filter is not None:
            result['NamespaceNameFilter'] = self.namespace_name_filter

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_name_filter is not None:
            result['RepoNameFilter'] = self.repo_name_filter

        if self.sync_rule_name is not None:
            result['SyncRuleName'] = self.sync_rule_name

        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope

        if self.sync_trigger is not None:
            result['SyncTrigger'] = self.sync_trigger

        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.target_namespace_name is not None:
            result['TargetNamespaceName'] = self.target_namespace_name

        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id

        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NamespaceNameFilter') is not None:
            self.namespace_name_filter = m.get('NamespaceNameFilter')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNameFilter') is not None:
            self.repo_name_filter = m.get('RepoNameFilter')

        if m.get('SyncRuleName') is not None:
            self.sync_rule_name = m.get('SyncRuleName')

        if m.get('SyncScope') is not None:
            self.sync_scope = m.get('SyncScope')

        if m.get('SyncTrigger') is not None:
            self.sync_trigger = m.get('SyncTrigger')

        if m.get('TagFilter') is not None:
            self.tag_filter = m.get('TagFilter')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TargetNamespaceName') is not None:
            self.target_namespace_name = m.get('TargetNamespaceName')

        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')

        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

