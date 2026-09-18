# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectsRequest(DaraModel):
    def __init__(
        self,
        list_system_catalog: bool = None,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        quota_name: str = None,
        quota_nick_name: str = None,
        region: str = None,
        sale_tags: str = None,
        sort_by: str = None,
        sort_order: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # Specifies whether to list the built-in **SYSTEM_CATALOG** project. This project provides information such as project metadata and usage history. For more information, see <props="intl">[Information Schema](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tenant-level-information-schema).
        self.list_system_catalog = list_system_catalog
        # The token that specifies the starting point of the query. The results are returned in alphabetical order, starting from the entry that immediately follows the marker.
        self.marker = marker
        # The maximum number of entries to return on each page. Default value: 10.
        self.max_item = max_item
        # The prefix of the resource names to query. For example, if you specify `a` for this parameter, only resources whose names start with "a" are returned.
        self.prefix = prefix
        # The quota name. The system automatically generates this name. To obtain the quota name, log in to the [MaxCompute console](https://maxcompute.console.aliyun.com) and select **Workspace** > **Quota** **Management** from the navigation pane on the left.
        self.quota_name = quota_name
        # The quota nickname. To obtain the quota nickname, log in to the [MaxCompute console](https://maxcompute.console.aliyun.com) and select **Workspace** > **Quota** **Management** from the navigation pane on the left.
        self.quota_nick_name = quota_nick_name
        # The region ID.
        self.region = region
        # The instance ID and billing method of the default compute quota.
        self.sale_tags = sale_tags
        # The sort field. The only supported value is `createdTime`.
        self.sort_by = sort_by
        # The sort order. This parameter takes effect only when `sortBy` is specified. Valid values are `ASC` and `DESC`. The values are case-insensitive.
        self.sort_order = sort_order
        # The tenant ID. To obtain the ID, log in to the [MaxCompute console](https://maxcompute.console.aliyun.com) and select **Tenant Management** > **Tenant Properties** from the navigation pane on the left.
        self.tenant_id = tenant_id
        # The project type. Valid values:
        # 
        # - **managed**: a managed project.
        # 
        # - **external**: an external project.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_system_catalog is not None:
            result['listSystemCatalog'] = self.list_system_catalog

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.quota_name is not None:
            result['quotaName'] = self.quota_name

        if self.quota_nick_name is not None:
            result['quotaNickName'] = self.quota_nick_name

        if self.region is not None:
            result['region'] = self.region

        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('listSystemCatalog') is not None:
            self.list_system_catalog = m.get('listSystemCatalog')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')

        if m.get('quotaNickName') is not None:
            self.quota_nick_name = m.get('quotaNickName')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

