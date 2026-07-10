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
        programming_language: str = None,
        reverse: bool = None,
        tags: str = None,
    ):
        # The application name.
        self.app_name = app_name
        # The Serverless App Engine (SAE) application type.
        # 
        # - **micro_service.**
        # - **web.**
        # - **job.**
        self.app_source = app_source
        # The current page number.
        self.current_page = current_page
        # The dimension by which to filter applications. Valid values:
        # 
        # - **appName**: application name.
        # - **appIds**: application ID.
        # - **slbIps**: SLB IP address.
        # - **instanceIps**: instance IP address.
        self.field_type = field_type
        # The application name, application ID, SLB IP address, or instance IP address of the target application.
        self.field_value = field_value
        # Specifies whether the application is stateful.
        self.is_stateful = is_stateful
        # The namespace ID.
        self.namespace_id = namespace_id
        # The application version. Valid values:
        # 
        # - lite: Lite Edition
        # - std: Standard Edition
        # - pro: Professional Edition
        self.new_sae_version = new_sae_version
        # The field by which to sort applications. Valid values:
        # 
        # - **runnings**: sorts by the current number target instances.
        # - **instances**: sorts by the target number target instances.
        self.order_by = order_by
        # The number of entries per page in a paging query. Valid values: [0,10000].
        self.page_size = page_size
        self.programming_language = programming_language
        # Specifies whether to sort application instances by running status. If instances have the same status, they are sorted by instance ID. Valid values:
        #   - **true**: sorts in ascending order. Instances are arranged based on the startup sequence. For example, to reach the running state, an instance must go through steps such as starting the container, pulling the image, and initializing the instance.
        #   - **false**: sorts in descending order.
        # 
        # The ascending order of instances is as follows:
        # 
        # 1. **Error**: an error occurred during instance startup.
        # 2. **CrashLoopBackOff**: the container failed to start, encountered an error during startup, and encountered an error again after restart.
        # 3. **ErrImagePull**: an error occurred while pulling the container image for the instance.
        # 4. **ImagePullBackOff**: the container image cannot be obtained.
        # 5. **Pending**: the instance is waiting to be scheduled.
        # 6. **Unknown**: an unknown exception occurred.
        # 7. **Terminating**: the instance is being terminated.
        # 8. **NotFound**: the instance cannot be found.
        # 9. **PodInitializing**: the instance is being initialized.
        # 10. **Init:0/1**: the instance is initializing.
        # 11. **Running**: the instance is running.
        self.reverse = reverse
        # The tag key-value pairs. Valid values:
        # - **key**: the tag key. The length must be in the range of [1,128].
        # - **value**: the tag value. The length must be in the range of [1,128].
        # 
        # Tags are case-sensitive. If you specify multiple tags, all specified tags are created and attached to the resource. Each tag key on the same resource can have only one tag value. If you add a tag key that already exists, the corresponding tag value is updated to the new value.
        # 
        # Tags cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language

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

        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

