# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        job_name: str = None,
        namespace: str = None,
        namespace_source: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        status: str = None,
    ):
        # The application ID. You can obtain the ID on the **Application Management** page in the console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The node name.
        self.job_name = job_name
        # The namespace. You can obtain the namespace on the **Namespace** page in the console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # Required only for special third-party users.
        self.namespace_source = namespace_source
        # The page number.
        self.page_num = page_num
        # The number of records per page.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The node status.
        # 
        # - **0**: disabled
        # 
        # - **1**: enabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

