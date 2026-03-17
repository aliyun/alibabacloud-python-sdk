# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeBindableSmartAccessGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        smart_access_gateways: main_models.DescribeBindableSmartAccessGatewaysResponseBodySmartAccessGateways = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.smart_access_gateways = smart_access_gateways
        # The total number of SAG instances.
        self.total_count = total_count

    def validate(self):
        if self.smart_access_gateways:
            self.smart_access_gateways.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.smart_access_gateways is not None:
            result['SmartAccessGateways'] = self.smart_access_gateways.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmartAccessGateways') is not None:
            temp_model = main_models.DescribeBindableSmartAccessGatewaysResponseBodySmartAccessGateways()
            self.smart_access_gateways = temp_model.from_map(m.get('SmartAccessGateways'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBindableSmartAccessGatewaysResponseBodySmartAccessGateways(DaraModel):
    def __init__(
        self,
        smart_access_gateway: List[main_models.DescribeBindableSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGateway] = None,
    ):
        self.smart_access_gateway = smart_access_gateway

    def validate(self):
        if self.smart_access_gateway:
            for v1 in self.smart_access_gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SmartAccessGateway'] = []
        if self.smart_access_gateway is not None:
            for k1 in self.smart_access_gateway:
                result['SmartAccessGateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.smart_access_gateway = []
        if m.get('SmartAccessGateway') is not None:
            for k1 in m.get('SmartAccessGateway'):
                temp_model = main_models.DescribeBindableSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGateway()
                self.smart_access_gateway.append(temp_model.from_map(k1))

        return self

class DescribeBindableSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGateway(DaraModel):
    def __init__(
        self,
        name: str = None,
        smart_agid: str = None,
        smart_aguid: int = None,
    ):
        self.name = name
        self.smart_agid = smart_agid
        self.smart_aguid = smart_aguid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_aguid is not None:
            result['SmartAGUid'] = self.smart_aguid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGUid') is not None:
            self.smart_aguid = m.get('SmartAGUid')

        return self

