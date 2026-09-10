# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataCheckTemplateListShrinkRequest(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        group_by: str = None,
        id_list_shrink: str = None,
        is_admin: bool = None,
        is_builtin: int = None,
        need_total_count: bool = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
    ):
        # The validation rule type. Valid values:
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        # - 3: custom comparison.
        # - 4: full-text comparison.
        # - 5: null rate comparison.
        self.check_type = check_type
        # The field used for grouping (GROUP BY condition). Configure this parameter as needed.
        self.group_by = group_by
        # The list of validation template UUIDs. The source code of CheckTemplatePagedQry indicates that this parameter has no actual effect and does not need to be exposed externally. It is retained only for backward compatibility with legacy calls. Passing this parameter does not affect query results.
        self.id_list_shrink = id_list_shrink
        # **[Deprecated]** This parameter is deprecated and does not need to be passed. The source code of CheckTemplatePagedQry marks this parameter with @Deprecated.
        self.is_admin = is_admin
        # Specifies whether the template is built-in. Valid values:
        # - 0: No. The template is a custom template.
        # - 1: Yes. The template is a built-in template.
        self.is_builtin = is_builtin
        # Specifies whether to return the total record count in the paginated results.
        self.need_total_count = need_total_count
        # The field used for sorting. Configure this parameter as needed.
        self.order_by = order_by
        # The sort direction. Valid values:
        # - ASC: ascending order.
        # - DESC: descending order.
        self.order_direction = order_direction
        # The page number. Pages start from 1.
        self.page_index = page_index
        # The page size, which specifies the number of records returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The name of the validation template.
        self.template_name = template_name
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.id_list_shrink is not None:
            result['idList'] = self.id_list_shrink

        if self.is_admin is not None:
            result['isAdmin'] = self.is_admin

        if self.is_builtin is not None:
            result['isBuiltin'] = self.is_builtin

        if self.need_total_count is not None:
            result['needTotalCount'] = self.need_total_count

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('idList') is not None:
            self.id_list_shrink = m.get('idList')

        if m.get('isAdmin') is not None:
            self.is_admin = m.get('isAdmin')

        if m.get('isBuiltin') is not None:
            self.is_builtin = m.get('isBuiltin')

        if m.get('needTotalCount') is not None:
            self.need_total_count = m.get('needTotalCount')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

