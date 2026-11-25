# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        codes: str = None,
        except_codes: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The commodity codes. Separate multiple codes with commas (,).
        self.codes = codes
        # The commodity codes to exclude. This parameter cannot be specified together with the Codes parameter. Separate multiple codes with commas (,).
        self.except_codes = except_codes
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The page number.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The commodity type. Valid values:
        # - APP: application
        # - SERVICE: service
        # - MIRROR: image
        # - DOWNLOAD: download
        # - API_SERVICE: API
        # - ROS: resource orchestration
        # - DOCKER: container
        # - IOT: IoT.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codes is not None:
            result['Codes'] = self.codes

        if self.except_codes is not None:
            result['ExceptCodes'] = self.except_codes

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')

        if m.get('ExceptCodes') is not None:
            self.except_codes = m.get('ExceptCodes')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

