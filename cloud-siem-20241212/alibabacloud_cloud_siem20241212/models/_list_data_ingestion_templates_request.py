# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataIngestionTemplatesRequest(DaraModel):
    def __init__(
        self,
        data_ingestion_template_status: str = None,
        data_source_template_ids: str = None,
        lang: str = None,
        page_number: str = None,
        page_size: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The status of the data ingestion template. Valid values:
        # - pending
        # - running
        # - success
        # - failed
        self.data_ingestion_template_status = data_ingestion_template_status
        # The list of data source template IDs.
        self.data_source_template_ids = data_source_template_ids
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # 
        # Note: This parameter is required. If you do not specify this parameter, the service returns a 400 error: "The specified Lang can not be empty." Explicitly pass in a language code.
        self.lang = lang
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The product ID.
        self.product_id = product_id
        # The region where the data management center of threat detection and response resides. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside the Chinese mainland.
        self.region_id = region_id
        # The user ID used by an administrator to assume the view of another member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_template_status is not None:
            result['DataIngestionTemplateStatus'] = self.data_ingestion_template_status

        if self.data_source_template_ids is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionTemplateStatus') is not None:
            self.data_ingestion_template_status = m.get('DataIngestionTemplateStatus')

        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids = m.get('DataSourceTemplateIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

