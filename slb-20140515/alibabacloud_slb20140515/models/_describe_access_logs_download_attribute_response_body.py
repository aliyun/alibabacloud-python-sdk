# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessLogsDownloadAttributeResponseBody(DaraModel):
    def __init__(
        self,
        logs_download_attributes: main_models.DescribeAccessLogsDownloadAttributeResponseBodyLogsDownloadAttributes = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configuration of the access log.
        self.logs_download_attributes = logs_download_attributes
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.logs_download_attributes:
            self.logs_download_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logs_download_attributes is not None:
            result['LogsDownloadAttributes'] = self.logs_download_attributes.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogsDownloadAttributes') is not None:
            temp_model = main_models.DescribeAccessLogsDownloadAttributeResponseBodyLogsDownloadAttributes()
            self.logs_download_attributes = temp_model.from_map(m.get('LogsDownloadAttributes'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccessLogsDownloadAttributeResponseBodyLogsDownloadAttributes(DaraModel):
    def __init__(
        self,
        logs_download_attribute: List[main_models.DescribeAccessLogsDownloadAttributeResponseBodyLogsDownloadAttributesLogsDownloadAttribute] = None,
    ):
        self.logs_download_attribute = logs_download_attribute

    def validate(self):
        if self.logs_download_attribute:
            for v1 in self.logs_download_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogsDownloadAttribute'] = []
        if self.logs_download_attribute is not None:
            for k1 in self.logs_download_attribute:
                result['LogsDownloadAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs_download_attribute = []
        if m.get('LogsDownloadAttribute') is not None:
            for k1 in m.get('LogsDownloadAttribute'):
                temp_model = main_models.DescribeAccessLogsDownloadAttributeResponseBodyLogsDownloadAttributesLogsDownloadAttribute()
                self.logs_download_attribute.append(temp_model.from_map(k1))

        return self

class DescribeAccessLogsDownloadAttributeResponseBodyLogsDownloadAttributesLogsDownloadAttribute(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        log_project: str = None,
        log_store: str = None,
        log_type: str = None,
        region: str = None,
    ):
        # The CLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The name of the Log Service project.
        self.log_project = log_project
        # The name of the Logstore.
        self.log_store = log_store
        # The type of access log. Only **layer7** is returned, which indicates Layer 7 access logs.
        self.log_type = log_type
        # The region ID of the CLB instance.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.log_project is not None:
            result['LogProject'] = self.log_project

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

