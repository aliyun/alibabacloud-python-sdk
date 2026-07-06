# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoSyncRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sync_rules: List[main_models.ListRepoSyncRuleResponseBodySyncRules] = None,
        total_count: int = None,
    ):
        # The response code.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of synchronization rules.
        self.sync_rules = sync_rules
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.sync_rules:
            for v1 in self.sync_rules:
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

        result['SyncRules'] = []
        if self.sync_rules is not None:
            for k1 in self.sync_rules:
                result['SyncRules'].append(k1.to_map() if k1 else None)

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

        self.sync_rules = []
        if m.get('SyncRules') is not None:
            for k1 in m.get('SyncRules'):
                temp_model = main_models.ListRepoSyncRuleResponseBodySyncRules()
                self.sync_rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRepoSyncRuleResponseBodySyncRules(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        cross_user: bool = None,
        link_id: str = None,
        local_instance_id: str = None,
        local_namespace_name: str = None,
        local_region_id: str = None,
        local_repo_name: str = None,
        modified_time: int = None,
        repo_name_filter: str = None,
        sync_direction: str = None,
        sync_rule_id: str = None,
        sync_rule_name: str = None,
        sync_scope: str = None,
        sync_trigger: str = None,
        tag_filter: str = None,
        target_instance_id: str = None,
        target_namespace_name: str = None,
        target_region_id: str = None,
        target_repo_name: str = None,
    ):
        # The time when the synchronization rule was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # Indicates whether images are synchronized across different Alibaba Cloud accounts. Valid values:
        # 
        # - `true`
        # 
        # - `false`
        # 
        # Default value: `false`.
        self.cross_user = cross_user
        self.link_id = link_id
        # The ID of the source instance.
        self.local_instance_id = local_instance_id
        # The name of the namespace in the source instance.
        self.local_namespace_name = local_namespace_name
        # The region ID of the source instance.
        self.local_region_id = local_region_id
        # The name of the repository in the source instance.
        self.local_repo_name = local_repo_name
        # The time when the synchronization rule was last modified. This value is a UNIX timestamp. Unit: milliseconds.
        self.modified_time = modified_time
        # The regular expression that is used to filter repositories.
        # 
        # > This parameter is valid only when `SyncScope` is set to `NAMESPACE`.
        self.repo_name_filter = repo_name_filter
        # The synchronization direction. Valid values:
        # 
        # - `FROM`: from the source instance to the target instance.
        # 
        # - `TO`: from the target instance to the source instance.
        self.sync_direction = sync_direction
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id
        # The name of the synchronization rule.
        self.sync_rule_name = sync_rule_name
        # The synchronization scope. Valid values:
        # 
        # - `NAMESPACE`: Synchronizes resources by namespace.
        # 
        # - `REPO`: Synchronizes resources by repository.
        self.sync_scope = sync_scope
        # The trigger policy. Valid values:
        # 
        # - `INITIATIVE`: The synchronization is actively triggered.
        # 
        # - `PASSIVE`: The synchronization is passively triggered.
        self.sync_trigger = sync_trigger
        # The regular expression that is used to filter tags.
        self.tag_filter = tag_filter
        # The ID of the target instance.
        self.target_instance_id = target_instance_id
        # The name of the namespace in the target instance.
        self.target_namespace_name = target_namespace_name
        # The region ID of the target instance.
        self.target_region_id = target_region_id
        # The name of the repository in the target instance.
        self.target_repo_name = target_repo_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.local_instance_id is not None:
            result['LocalInstanceId'] = self.local_instance_id

        if self.local_namespace_name is not None:
            result['LocalNamespaceName'] = self.local_namespace_name

        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id

        if self.local_repo_name is not None:
            result['LocalRepoName'] = self.local_repo_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.repo_name_filter is not None:
            result['RepoNameFilter'] = self.repo_name_filter

        if self.sync_direction is not None:
            result['SyncDirection'] = self.sync_direction

        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('LocalInstanceId') is not None:
            self.local_instance_id = m.get('LocalInstanceId')

        if m.get('LocalNamespaceName') is not None:
            self.local_namespace_name = m.get('LocalNamespaceName')

        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')

        if m.get('LocalRepoName') is not None:
            self.local_repo_name = m.get('LocalRepoName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RepoNameFilter') is not None:
            self.repo_name_filter = m.get('RepoNameFilter')

        if m.get('SyncDirection') is not None:
            self.sync_direction = m.get('SyncDirection')

        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')

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

        return self

