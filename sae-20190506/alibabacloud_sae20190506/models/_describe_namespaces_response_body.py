# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeNamespacesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The information of namespaces.
        self.data = data
        # The error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The returned message. Valid values:
        # 
        # *   success: If the call is successful, **success** is returned.
        # *   An error code: If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the list of namespaces was queried. Valid values:
        # 
        # *   **true**: The list was queried.
        # *   **false**: The list failed to be queried.
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeNamespacesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeNamespacesResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        namespaces: List[main_models.DescribeNamespacesResponseBodyDataNamespaces] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The namespaces.
        self.namespaces = namespaces
        # The number of entries per page.
        self.page_size = page_size
        # The total number of namespaces.
        self.total_size = total_size

    def validate(self):
        if self.namespaces:
            for v1 in self.namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Namespaces'] = []
        if self.namespaces is not None:
            for k1 in self.namespaces:
                result['Namespaces'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k1 in m.get('Namespaces'):
                temp_model = main_models.DescribeNamespacesResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeNamespacesResponseBodyDataNamespaces(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        address_server_host: str = None,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
        secret_key: str = None,
        tenant_id: str = None,
    ):
        # The ACM-specific AccessKey ID. It can be used to manage data in an Application Configuration Management (ACM) namespace. For more information, see [Differences between Alibaba Cloud AccessKey and ACM-specific AccessKey](https://help.aliyun.com/document_detail/68941.html).
        self.access_key = access_key
        # The endpoint of the host.
        self.address_server_host = address_server_host
        # The short ID of the namespace.
        self.name_space_short_id = name_space_short_id
        # The description of the namespace.
        self.namespace_description = namespace_description
        # The ID of the namespace. You cannot query, modify, or delete the default namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The region ID.
        self.region_id = region_id
        # The ACM-specific AccessKey secret. It can be used to manage data in an ACM namespace. For more information, see [Differences between Alibaba Cloud AccessKey and ACM-specific AccessKey](https://help.aliyun.com/document_detail/68941.html).
        self.secret_key = secret_key
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.address_server_host is not None:
            result['AddressServerHost'] = self.address_server_host

        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AddressServerHost') is not None:
            self.address_server_host = m.get('AddressServerHost')

        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

