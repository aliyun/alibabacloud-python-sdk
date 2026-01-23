# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRepoSyncRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        target_instance_id: str = None,
        target_region_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the image repository.
        self.repo_name = repo_name
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id
        # The region ID of the destination instance.
        self.target_region_id = target_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')

        return self

