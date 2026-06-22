# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImageRiskRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        current_page: int = None,
        image_name: str = None,
        namespace: str = None,
        page_size: int = None,
    ):
        # The application name.
        self.app_name = app_name
        # The ID of the container cluster to query.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The page number of the current page in a paging query.
        self.current_page = current_page
        # The image name.
        self.image_name = image_name
        # The image namespace.
        self.namespace = namespace
        # The maximum number of entries per page in a paging query. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

