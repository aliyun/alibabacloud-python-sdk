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
        # The SAE application type. Valid values:
        # 
        # - **micro_service**
        # - **web**
        # - **job**
        self.app_source = app_source
        # The current page number.
        self.current_page = current_page
        # Set the filtering criteria for applications. The value options are as follows:
        # 
        # - appName: Application name.
        # - appIds: Application IDs.
        # - slbIps: SLB IP addresses.
        # - instanceIps: Instance IP addresses.
        self.field_type = field_type
        # The name, ID, SLB IP, or instance IP of the target application.
        self.field_value = field_value
        self.is_stateful = is_stateful
        # The namespace ID.
        self.namespace_id = namespace_id
        self.new_sae_version = new_sae_version
        # Specifies how applications are sorted. Valid values:
        # 
        # *   **running**: The applications are sorted based on the number of running instances.
        # *   **instances**: The applications are sorted based on the number of destination instances.
        self.order_by = order_by
        # The number of records in each page. Value range: [0,10000]
        self.page_size = page_size
        # Sort by the running status of application instances. If the statuses are the same, sort by instance ID. The value options are as follows:
        # 
        # - true: Sort in ascending order. Instances are arranged according to the startup process, for example: to ultimately reach the running state, an instance must first go through steps such as starting containers, pulling images, and initializing the instance.
        # - false: Sort in descending order.
        self.reverse = reverse
        # The tag in the format of a key-value pair.
        # *   **key**: the tag key. It cannot exceed 128 characters in length.
        # *   **value**: the tag value. It cannot exceed 128 characters in length.
        # 
        # Tag keys and tag values are case-sensitive. If you specify multiple tags, the system adds all the tags to the specified resources. Each tag key on a resource can have only one tag value. If you create a tag that has the same key as an existing tag, the value of the existing tag is overwritten.
        # 
        # Tag keys and tag values cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

