# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeModelApisResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeModelApisResponseBodyItems] = None,
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
                temp_model = main_models.DescribeModelApisResponseBodyItems()
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

class DescribeModelApisResponseBodyItems(DaraModel):
    def __init__(
        self,
        category: str = None,
        gmt_created: str = None,
        model_api_id: str = None,
        name: str = None,
        path_prefix: str = None,
        protocol: str = None,
        record_input: str = None,
        record_output: str = None,
        route_rules: str = None,
        status: str = None,
    ):
        self.category = category
        self.gmt_created = gmt_created
        self.model_api_id = model_api_id
        self.name = name
        self.path_prefix = path_prefix
        self.protocol = protocol
        self.record_input = record_input
        self.record_output = record_output
        self.route_rules = route_rules
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.model_api_id is not None:
            result['ModelApiId'] = self.model_api_id

        if self.name is not None:
            result['Name'] = self.name

        if self.path_prefix is not None:
            result['PathPrefix'] = self.path_prefix

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.record_input is not None:
            result['RecordInput'] = self.record_input

        if self.record_output is not None:
            result['RecordOutput'] = self.record_output

        if self.route_rules is not None:
            result['RouteRules'] = self.route_rules

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('ModelApiId') is not None:
            self.model_api_id = m.get('ModelApiId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathPrefix') is not None:
            self.path_prefix = m.get('PathPrefix')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RecordInput') is not None:
            self.record_input = m.get('RecordInput')

        if m.get('RecordOutput') is not None:
            self.record_output = m.get('RecordOutput')

        if m.get('RouteRules') is not None:
            self.route_rules = m.get('RouteRules')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

