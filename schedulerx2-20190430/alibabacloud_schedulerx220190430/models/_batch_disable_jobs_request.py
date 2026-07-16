# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchDisableJobsRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        job_id_list: List[int] = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        # The ID of the application group. You can find this ID on the **Application Management** page in the console.
        self.group_id = group_id
        # The IDs of the jobs to disable.
        # 
        # This parameter is required.
        self.job_id_list = job_id_list
        # The ID of the namespace that contains the jobs. You can find this ID on the **Namespaces** page in the console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # This parameter is used only by specific third-party services.
        self.namespace_source = namespace_source
        # The ID of the region where the jobs are located.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

