# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_filter_shrink: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The job filter information.
        self.job_filter_shrink = job_filter_shrink
        # The page number of the page to return.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1
        self.page_number = page_number
        # The number of entries per page.
        # 
        # *   Maximum value: 50.
        # *   Default value: 10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_filter_shrink is not None:
            result['JobFilter'] = self.job_filter_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobFilter') is not None:
            self.job_filter_shrink = m.get('JobFilter')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

