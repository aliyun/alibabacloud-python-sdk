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
        # The page number. The value starts from 1.
        self.current_page = current_page
        # The dimension by which to filter job templates. Valid values:
        # 
        # - **appName**: The name of the job template.
        # 
        # - **appIds**: The ID of the job template.
        self.field_type = field_type
        # The name or ID of the target job template. This value corresponds to the dimension specified by **FieldType**.
        self.field_value = field_value
        # The namespace ID.
        self.namespace_id = namespace_id
        # The sorting method for the job templates. Valid values:
        # 
        # - **running**: Sorts by the number of running instances.
        # 
        # - **instances**: Sorts by the number of destination instances.
        self.order_by = order_by
        # The number of entries per page. Valid values: 0 to 200.
        self.page_size = page_size
        # Specifies whether to sort the results in ascending or descending order based on the field specified by the **OrderBy** parameter. Valid values:
        # 
        # - **true**: ascending order.
        # 
        # - **false**: descending order.
        self.reverse = reverse
        # A list of tags. This is a JSON string. The value consists of the following parts:
        # 
        # - **key**: The tag key.
        # 
        # - **value**: The tag value.
        self.tags = tags
        # The workload. Set the value to `job`.
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

