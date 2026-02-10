# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOpaClusterImageListRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_page: int = None,
        image_name: str = None,
        page_size: int = None,
    ):
        # The ID of the cluster to which the container belongs.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The name of the image.
        self.image_name = image_name
        # The number of entries per page. Default value: **20**.
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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

