# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListAnsServicesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAnsServicesResponseBodyData] = None,
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
        # The HTTP status code returned.
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
        # The total number of instances returned.
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
                temp_model = main_models.ListAnsServicesResponseBodyData()
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

class ListAnsServicesResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_count: int = None,
        group_name: str = None,
        healthy_instance_count: int = None,
        ip_count: int = None,
        name: str = None,
        source: str = None,
    ):
        # The total number of clusters.
        self.cluster_count = cluster_count
        # The name of the contact group.
        self.group_name = group_name
        # The total number of instances with healthy heartbeats.
        self.healthy_instance_count = healthy_instance_count
        # The total number of instances that are used for the current service.
        self.ip_count = ip_count
        # The name of the service.
        self.name = name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.healthy_instance_count is not None:
            result['HealthyInstanceCount'] = self.healthy_instance_count

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HealthyInstanceCount') is not None:
            self.healthy_instance_count = m.get('HealthyInstanceCount')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

