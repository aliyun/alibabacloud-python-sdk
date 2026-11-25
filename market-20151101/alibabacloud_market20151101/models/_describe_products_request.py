# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeProductsRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeProductsRequestFilter] = None,
        page_number: int = None,
        page_size: int = None,
        search_term: str = None,
    ):
        # The list of filter conditions.
        self.filter = filter
        # The current page number.
        self.page_number = page_number
        # The number of products to display per page.
        self.page_size = page_size
        # The search keyword.
        self.search_term = search_term

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_term is not None:
            result['SearchTerm'] = self.search_term

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeProductsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchTerm') is not None:
            self.search_term = m.get('SearchTerm')

        return self

class DescribeProductsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The category of the search tag. Valid values:
        # 
        # * sort: the sorting method
        # * categoryId: the category ID
        # * productType: the product type
        # * aliyunUid: the Alibaba Cloud account ID of the service provider that owns the product.
        self.key = key
        # The value of the search label:
        # 
        # 
        # - sort
        #   - user_count-desc: number of transactions in the last 180 days
        #   - created_on-desc: creation time
        #   - price-desc: price
        #   - score-desc: rating
        # 
        # - categoryId 
        #   - Software Marketplace  53366009
        #     + Runtime Environment  53448001
        #     - Management & Monitoring  53690006
        #     - Website Building System  53616009
        #     - Application Development  55530001
        #     - Database  56024006
        #     - Server Software  56014009
        #     - Network Feature Software  56368007
        #     - Operating System  57742013
        #   - Service Marketplace  52734001
        #     - Data Migration  52738004
        #     - Environment Configuration  52746001
        #     - Troubleshooting  52740002
        #     - Security O&M  52732002
        #     - Custom Development  56082003
        #     - Training & Certification  57252001
        #     - Dedicated Line Access  57392001
        #     - Enterprise Services  56838014
        #     - Security Services  57004003
        #   - Website Building Marketplace  52738001
        #     - Enterprise Display  52738005
        #     - E-commerce  52750001
        #     - Mobile Website  52752001
        #     - Design  52732003
        #     - Information Portal  52744002
        #     - After-sales Service  52744003
        #     - Community Forum  55586021
        #     - Mobile Marketing  55514022
        #     - Template Website  56598032
        #     - Website Hosting  57342011
        #   - Cloud Security Marketplace  56764045
        #     + Host Security  56832023
        #     + Application Security  56846020
        #     + Data Security  56824015
        #     + Security Management  56830014
        #     + Network Security  56820014
        #   - Enterprise Applications  56832009
        #     - Office Management  56778013
        #     - Financial Management  56764034
        #     - HR Management  56780006
        #     - Sales Management  56842010
        #     - Advertising & Marketing  56842011
        #     - Foreign Trade  56790007
        #     - Cloud Communications  57602001
        #     - Supply Chain Management  57604001
        #     - Data Services  57606001
        #   - Solutions  56848023
        #     - E-commerce  56848024
        #     - Finance  56820017
        #     - Logistics  56776025
        #     - Government  56842031
        #     - Multimedia  56784018
        #     - IoT  56794026
        #     - Big Data  56792022
        #   - API Marketplace  56956004
        #     - E-commerce  56928004
        #     - Finance & Investment  57000002
        #     - Transportation & Geography  57002002
        #     - Enterprise Management  56928005
        #     - Public Affairs  57002003
        #     - Meteorology & Water Resources  57096001
        #     - Artificial Intelligence  57124001
        #     - Lifestyle Services  57126001
        #   - IoT Marketplace  201194001
        #     - Integrated Systems  201196001
        #     - Smart Hardware  201198001
        #     - Modules  201200001
        #     - Sensors  201192002
        #     - Chips  201202001
        #     - IoT Applications  201196002
        #     - IoT Services  201196003
        #   - Data Intelligence  201204005
        #     - Data Analytics & Visualization  201190008
        #     - Public Opinion Analysis  201198004
        #     - E-commerce & Marketing  201202006
        #     - Artificial Intelligence  201204006
        #     - Meteorology & Transportation  201214006
        #     - Finance & Accounting  201208013
        # - productType:
        #   - APP: application
        #   - SERVICE: service
        #   - MIRROR: image
        #   - DOWNLOAD: download
        #   - API_SERVICE: API.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

