# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        current_page: int = None,
        field_type: str = None,
        field_value: str = None,
        namespace_id: str = None,
        order_by: str = None,
        page_size: int = None,
        reverse: bool = None,
        tags: str = None,
        workload: str = None,
    ):
        # The name of the job template.
        self.app_name = app_name
        # The number of the page to return. The parameter value is a positive integer that is greater than or equal to 1.
        self.current_page = current_page
        # The dimension by which applications are filtered. Valid values:
        # 
        # *   **appName**: Applications are filtered by job template name.
        # *   **appIds**: Applications are filtered by job template ID.
        self.field_type = field_type
        # Enter the name and ID of the job template.
        self.field_value = field_value
        # The namespace ID.
        self.namespace_id = namespace_id
        # Specifies how applications are sorted. Valid values:
        # 
        # *   **running**: The applications are sorted based on the number of running instances.
        # *   **instances**: The applications are sorted based on the number of destination instances.
        self.order_by = order_by
        # The number of entries to return on each page. Valid value: 0 to 200.
        self.page_size = page_size
        # Specifies whether to sort the field names that are passed by **OrderBy** in ascending order. Valid values:
        # 
        # *   **true**: in ascending order
        # *   **false**: in descending order
        self.reverse = reverse
        # The tags that are displayed in a JSON string. Valid values:
        # 
        # *   **key**: the tag key
        # *   **value**: the tag value
        self.tags = tags
        # Set the value to `job`.
        self.workload = workload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.field_type is not None:
            result['FieldType'] = self.field_type

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.workload is not None:
            result['Workload'] = self.workload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Workload') is not None:
            self.workload = m.get('Workload')

        return self

