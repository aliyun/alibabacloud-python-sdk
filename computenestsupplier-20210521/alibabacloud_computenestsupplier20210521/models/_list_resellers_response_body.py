# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListResellersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        supplier_information: List[main_models.ListResellersResponseBodySupplierInformation] = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # distributor informations
        self.supplier_information = supplier_information
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.supplier_information:
            for v1 in self.supplier_information:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SupplierInformation'] = []
        if self.supplier_information is not None:
            for k1 in self.supplier_information:
                result['SupplierInformation'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.supplier_information = []
        if m.get('SupplierInformation') is not None:
            for k1 in m.get('SupplierInformation'):
                temp_model = main_models.ListResellersResponseBodySupplierInformation()
                self.supplier_information.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResellersResponseBodySupplierInformation(DaraModel):
    def __init__(
        self,
        supplier_desc: str = None,
        supplier_logo: str = None,
        supplier_name: str = None,
        supplier_uid: int = None,
        supplier_url: str = None,
    ):
        # The description of distributor.
        self.supplier_desc = supplier_desc
        # The Logo of distributor
        self.supplier_logo = supplier_logo
        # The name of the distributor
        self.supplier_name = supplier_name
        # The Alibaba Cloud account ID of the distributor.
        self.supplier_uid = supplier_uid
        # The URL of the distributor.
        self.supplier_url = supplier_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc

        if self.supplier_logo is not None:
            result['SupplierLogo'] = self.supplier_logo

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')

        if m.get('SupplierLogo') is not None:
            self.supplier_logo = m.get('SupplierLogo')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        return self

