# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataIngestionTemplateRequest(DaraModel):
    def __init__(
        self,
        data_ingestion_status: str = None,
        data_ingestion_template_id: str = None,
        data_ingestion_template_name: str = None,
        lang: str = None,
        normalization_rule_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_id = data_ingestion_template_id
        self.data_ingestion_template_name = data_ingestion_template_name
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status

        if self.data_ingestion_template_id is not None:
            result['DataIngestionTemplateId'] = self.data_ingestion_template_id

        if self.data_ingestion_template_name is not None:
            result['DataIngestionTemplateName'] = self.data_ingestion_template_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')

        if m.get('DataIngestionTemplateId') is not None:
            self.data_ingestion_template_id = m.get('DataIngestionTemplateId')

        if m.get('DataIngestionTemplateName') is not None:
            self.data_ingestion_template_name = m.get('DataIngestionTemplateName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

