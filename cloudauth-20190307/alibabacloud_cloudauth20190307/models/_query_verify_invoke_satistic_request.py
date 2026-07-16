# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVerifyInvokeSatisticRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: int = None,
        page_size: int = None,
        product_program_list: str = None,
        product_type: str = None,
        scene_id_list: str = None,
        start_date: int = None,
        statistics_type: str = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The end time of the query.
        self.end_date = end_date
        # The number of entries per page.
        self.page_size = page_size
        # The list of product codes to query. For more information, refer to the productCode under the corresponding ProductType.
        self.product_program_list = product_program_list
        # The product type. Valid values:
        # - **FINANCE_VERIFY**: financial-grade ID Verification
        # - **SMART_VERIFY**: enhanced ID Verification (discontinued)
        # - **FACE_VERIFY**: ID Verification (discontinued).
        self.product_type = product_type
        # The list of common scenarios.
        self.scene_id_list = scene_id_list
        # The start time of the query.
        self.start_date = start_date
        # The statistical dimension. Valid values:
        # - **day**: daily
        # - **month**: monthly.
        self.statistics_type = statistics_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_program_list is not None:
            result['ProductProgramList'] = self.product_program_list

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.scene_id_list is not None:
            result['SceneIdList'] = self.scene_id_list

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductProgramList') is not None:
            self.product_program_list = m.get('ProductProgramList')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SceneIdList') is not None:
            self.scene_id_list = m.get('SceneIdList')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')

        return self

