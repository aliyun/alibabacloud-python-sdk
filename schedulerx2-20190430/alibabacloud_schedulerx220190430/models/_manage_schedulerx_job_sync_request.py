# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ManageSchedulerxJobSyncRequest(DaraModel):
    def __init__(
        self,
        job_id_list: List[int] = None,
        namespace_source: str = None,
        original_group_id: str = None,
        original_namespace: str = None,
        region_id: str = None,
        target_group_id: str = None,
        target_namespace: str = None,
    ):
        # The list of task IDs.
        # 
        # This parameter is required.
        self.job_id_list = job_id_list
        # The source of the namespace. Required only for specific third-party cases.
        self.namespace_source = namespace_source
        # The source application group to which the task belongs.
        # 
        # This parameter is required.
        self.original_group_id = original_group_id
        # The source namespace where the task resides.
        # 
        # This parameter is required.
        self.original_namespace = original_namespace
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the destination application group to which the task will be synchronized.
        # 
        # This parameter is required.
        self.target_group_id = target_group_id
        # The destination namespace to which the task will be synchronized.
        # 
        # This parameter is required.
        self.target_namespace = target_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.original_group_id is not None:
            result['OriginalGroupId'] = self.original_group_id

        if self.original_namespace is not None:
            result['OriginalNamespace'] = self.original_namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_group_id is not None:
            result['TargetGroupId'] = self.target_group_id

        if self.target_namespace is not None:
            result['TargetNamespace'] = self.target_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('OriginalGroupId') is not None:
            self.original_group_id = m.get('OriginalGroupId')

        if m.get('OriginalNamespace') is not None:
            self.original_namespace = m.get('OriginalNamespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetGroupId') is not None:
            self.target_group_id = m.get('TargetGroupId')

        if m.get('TargetNamespace') is not None:
            self.target_namespace = m.get('TargetNamespace')

        return self

