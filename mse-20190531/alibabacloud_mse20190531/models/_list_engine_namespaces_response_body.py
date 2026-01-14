# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListEngineNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListEngineNamespacesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of returned instances.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListEngineNamespacesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEngineNamespacesResponseBodyData(DaraModel):
    def __init__(
        self,
        config_count: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        namespace_show_name: str = None,
        quota: int = None,
        service_count: str = None,
        source_type: str = None,
        type: int = None,
    ):
        # The quota value.
        self.config_count = config_count
        # The namespace.
        self.namespace = namespace
        # The description of the namespace.
        self.namespace_desc = namespace_desc
        # The name of the namespace.
        self.namespace_show_name = namespace_show_name
        # The quota.
        self.quota = quota
        # The number of active services.
        self.service_count = service_count
        # The source from which the namespace was created.
        self.source_type = source_type
        # The type of the namespace. Valid values:
        # 
        # *   `0`: global configuration
        # *   `1`: default namespace
        # *   `2`: custom namespace
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc

        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.service_count is not None:
            result['ServiceCount'] = self.service_count

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')

        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

