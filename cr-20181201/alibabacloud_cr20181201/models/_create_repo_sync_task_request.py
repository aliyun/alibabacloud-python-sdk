# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoSyncTaskRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        override: bool = None,
        priority: int = None,
        repo_id: str = None,
        tag: str = None,
        target_instance_id: str = None,
        target_namespace: str = None,
        target_region_id: str = None,
        target_repo_name: str = None,
        target_tag: str = None,
        target_user_id: str = None,
    ):
        # The source instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to forcibly overwrite existing images. Valid values:
        # 
        # - `true`: Forcibly overwrites existing images.
        # 
        # - `false`: Does not forcibly overwrite existing images.
        self.override = override
        # The execution priority of the synchronization task. Synchronization tasks are executed in descending order of priority. Tasks with the same priority are executed in random order.
        # 
        # Valid values: 1 to 5.
        # 
        # Default value: 3.
        self.priority = priority
        # The ID of the image repository in the source instance.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The image tag in the source instance.
        # 
        # This parameter is required.
        self.tag = tag
        # The target instance ID.
        # 
        # This parameter is required.
        self.target_instance_id = target_instance_id
        # The namespace of the target instance.
        # 
        # This parameter is required.
        self.target_namespace = target_namespace
        # The region ID of the target instance.
        # 
        # This parameter is required.
        self.target_region_id = target_region_id
        # The name of the image repository in the target instance.
        # 
        # This parameter is required.
        self.target_repo_name = target_repo_name
        # The image tag in the target instance.
        # 
        # This parameter is required.
        self.target_tag = target_tag
        # The UID of the account to which the target instance belongs.
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

        if self.override is not None:
            result['Override'] = self.override

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.target_namespace is not None:
            result['TargetNamespace'] = self.target_namespace

        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id

        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name

        if self.target_tag is not None:
            result['TargetTag'] = self.target_tag

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Override') is not None:
            self.override = m.get('Override')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TargetNamespace') is not None:
            self.target_namespace = m.get('TargetNamespace')

        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')

        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')

        if m.get('TargetTag') is not None:
            self.target_tag = m.get('TargetTag')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

