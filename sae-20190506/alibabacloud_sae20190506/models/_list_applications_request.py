# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationsRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_source: str = None,
        current_page: int = None,
        field_type: str = None,
        field_value: str = None,
        is_stateful: str = None,
        namespace_id: str = None,
        new_sae_version: str = None,
        order_by: str = None,
        page_size: int = None,
        reverse: bool = None,
        tags: str = None,
    ):
        # The application name.
        self.app_name = app_name
        # The type of the SAE application.
        # 
        # - **micro_service**
        # 
        # - **web**
        # 
        # - **job**
        self.app_source = app_source
        # The current page number.
        self.current_page = current_page
        # The field to filter applications by. Valid values:
        # 
        # - **appName**: The application name.
        # 
        # - **appIds**: The application ID.
        # 
        # - **slbIps**: The SLB IP address.
        # 
        # - **instanceIps**: The instance IP address.
        self.field_type = field_type
        # The value for the field specified by `FieldType`. This can be an application name, application ID, SLB IP address, or instance IP address.
        self.field_value = field_value
        # Filters applications by whether they are stateful. Set this parameter to `true` to return only stateful applications, or to `false` to return only stateless applications.
        self.is_stateful = is_stateful
        # The namespace ID.
        self.namespace_id = namespace_id
        # The edition of the application:
        # 
        # - `lite`: Lite
        # 
        # - `std`: Standard
        # 
        # - `pro`: Pro
        self.new_sae_version = new_sae_version
        # The field to sort the applications by. Valid values:
        # 
        # - **runnings**: Sorts the applications by the current instance count.
        # 
        # - **instances**: Sorts the applications by the target instance count.
        self.order_by = order_by
        # The number of entries to return per page. Valid values: 0 to 10000.
        self.page_size = page_size
        # The sort order. Valid values:
        # 
        # - **true**: Sorts the results in ascending order.
        # 
        # - **false**: Sorts the results in descending order.
        # 
        # 1. ****
        # 
        # 2. ****
        # 
        # 3. ****
        # 
        # 4. ****
        # 
        # 5. ****
        # 
        # 6. ****
        # 
        # 7. ****
        # 
        # 8. ****
        # 
        # 9. ****
        # 
        # 10. ****
        # 
        # 11. ****
        self.reverse = reverse
        # Filters applications by tags. The tags are specified as a JSON string that contains an array of key-value pairs.
        # 
        # - **key**: The tag key, which can be 1 to 128 characters in length.
        # 
        # - **value**: The tag value, which can be 1 to 128 characters in length.
        # 
        # This parameter is case-sensitive. An application is returned only if it matches all specified tags. On a resource, a tag key can have only one tag value.
        # 
        # The tag key and tag value cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_source is not None:
            result['AppSource'] = self.app_source

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.field_type is not None:
            result['FieldType'] = self.field_type

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.is_stateful is not None:
            result['IsStateful'] = self.is_stateful

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSource') is not None:
            self.app_source = m.get('AppSource')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('IsStateful') is not None:
            self.is_stateful = m.get('IsStateful')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

