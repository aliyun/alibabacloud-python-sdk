# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeModelServicesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeModelServicesResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeModelServicesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeModelServicesResponseBodyItems(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        gmt_created: str = None,
        input_cost_points_per_million: str = None,
        model_category: str = None,
        model_service_id: str = None,
        name: str = None,
        output_cost_points_per_million: str = None,
        protocol: str = None,
        request_cost_points: str = None,
        status: str = None,
        vendor: str = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.gmt_created = gmt_created
        self.input_cost_points_per_million = input_cost_points_per_million
        self.model_category = model_category
        self.model_service_id = model_service_id
        self.name = name
        self.output_cost_points_per_million = output_cost_points_per_million
        self.protocol = protocol
        self.request_cost_points = request_cost_points
        self.status = status
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.input_cost_points_per_million is not None:
            result['InputCostPointsPerMillion'] = self.input_cost_points_per_million

        if self.model_category is not None:
            result['ModelCategory'] = self.model_category

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output_cost_points_per_million is not None:
            result['OutputCostPointsPerMillion'] = self.output_cost_points_per_million

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.request_cost_points is not None:
            result['RequestCostPoints'] = self.request_cost_points

        if self.status is not None:
            result['Status'] = self.status

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('InputCostPointsPerMillion') is not None:
            self.input_cost_points_per_million = m.get('InputCostPointsPerMillion')

        if m.get('ModelCategory') is not None:
            self.model_category = m.get('ModelCategory')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputCostPointsPerMillion') is not None:
            self.output_cost_points_per_million = m.get('OutputCostPointsPerMillion')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RequestCostPoints') is not None:
            self.request_cost_points = m.get('RequestCostPoints')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

