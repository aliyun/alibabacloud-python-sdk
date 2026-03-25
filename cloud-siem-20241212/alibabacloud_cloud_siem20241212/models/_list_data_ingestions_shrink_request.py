# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataIngestionsShrinkRequest(DaraModel):
    def __init__(
        self,
        data_ingestion_ids_shrink: str = None,
        data_ingestion_status: str = None,
        data_ingestion_template_ids_shrink: str = None,
        lang: str = None,
        normalization_schema_ids_shrink: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_ids_shrink = data_ingestion_ids_shrink
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_ids_shrink = data_ingestion_template_ids_shrink
        self.lang = lang
        self.normalization_schema_ids_shrink = normalization_schema_ids_shrink
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_ids_shrink is not None:
            result['DataIngestionIds'] = self.data_ingestion_ids_shrink

        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status

        if self.data_ingestion_template_ids_shrink is not None:
            result['DataIngestionTemplateIds'] = self.data_ingestion_template_ids_shrink

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_schema_ids_shrink is not None:
            result['NormalizationSchemaIds'] = self.normalization_schema_ids_shrink

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
            self.data_ingestion_ids_shrink = m.get('DataIngestionIds')

        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')

        if m.get('DataIngestionTemplateIds') is not None:
            self.data_ingestion_template_ids_shrink = m.get('DataIngestionTemplateIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationSchemaIds') is not None:
            self.normalization_schema_ids_shrink = m.get('NormalizationSchemaIds')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

