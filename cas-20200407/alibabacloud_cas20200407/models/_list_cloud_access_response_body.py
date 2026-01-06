# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListCloudAccessResponseBody(DaraModel):
    def __init__(
        self,
        cloud_access_list: List[main_models.ListCloudAccessResponseBodyCloudAccessList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The query results.
        self.cloud_access_list = cloud_access_list
        # The default value is the current page. If CurrentPage is not specified, this parameter is not returned.
        self.current_page = current_page
        # The request ID.
        self.request_id = request_id
        # The number of entries per page. If ShowSize is not specified, this parameter is not returned.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cloud_access_list:
            for v1 in self.cloud_access_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAccessList'] = []
        if self.cloud_access_list is not None:
            for k1 in self.cloud_access_list:
                result['CloudAccessList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_access_list = []
        if m.get('CloudAccessList') is not None:
            for k1 in m.get('CloudAccessList'):
                temp_model = main_models.ListCloudAccessResponseBodyCloudAccessList()
                self.cloud_access_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAccessResponseBodyCloudAccessList(DaraModel):
    def __init__(
        self,
        access_id: int = None,
        cloud_name: str = None,
        secret_id: str = None,
        service_status: str = None,
    ):
        # The ID of the primary key.
        self.access_id = access_id
        # The cloud service provider.
        self.cloud_name = cloud_name
        # The AccessKey ID that is used to access cloud resources.
        self.secret_id = secret_id
        # The service status. The value normal indicates that the service runs as expected.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        return self

