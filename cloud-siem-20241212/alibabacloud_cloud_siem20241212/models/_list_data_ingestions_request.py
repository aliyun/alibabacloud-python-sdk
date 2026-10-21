# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDataIngestionsRequest(DaraModel):
    def __init__(
        self,
        data_ingestion_ids: List[str] = None,
        data_ingestion_status: str = None,
        data_ingestion_template_ids: List[str] = None,
        lang: str = None,
        normalization_schema_ids: List[str] = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The list of data ingestion policy IDs.
        self.data_ingestion_ids = data_ingestion_ids
        # The accessed state of data ingestion. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.data_ingestion_status = data_ingestion_status
        # The list of data ingestion template IDs.
        self.data_ingestion_template_ids = data_ingestion_template_ids
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The list of normalization schema IDs.
        self.normalization_schema_ids = normalization_schema_ids
        # The product ID.
        self.product_id = product_id
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The user ID of the member to which the administrator switches the view.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_ids is not None:
            result['DataIngestionIds'] = self.data_ingestion_ids

        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status

        if self.data_ingestion_template_ids is not None:
            result['DataIngestionTemplateIds'] = self.data_ingestion_template_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_schema_ids is not None:
            result['NormalizationSchemaIds'] = self.normalization_schema_ids

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionIds') is not None:
            self.data_ingestion_ids = m.get('DataIngestionIds')

        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')

        if m.get('DataIngestionTemplateIds') is not None:
            self.data_ingestion_template_ids = m.get('DataIngestionTemplateIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationSchemaIds') is not None:
            self.normalization_schema_ids = m.get('NormalizationSchemaIds')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

