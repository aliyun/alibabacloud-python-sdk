# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNormalizationSchemasRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_category_id: str = None,
        normalization_field_source: str = None,
        normalization_schema_type: str = None,
        normalization_security_domain_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The pagination token for the next query. Leave this parameter empty for the first query or if no more results exist. If more results exist, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The ID of the normalization rule category.
        self.normalization_category_id = normalization_category_id
        # The field source filter. Valid values: normalized / native.
        self.normalization_field_source = normalization_field_source
        # The normalization schema type. Valid values:
        # - log: log.
        # - entity: entity.
        self.normalization_schema_type = normalization_schema_type
        # The security domain ID.
        self.normalization_security_domain_id = normalization_security_domain_id
        # The region where the threat analysis data management center is located. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: the asset is in the Chinese mainland.
        # - ap-southeast-1: the asset is outside the Chinese mainland.
        self.region_id = region_id
        # The user ID that the administrator switches to when viewing as another member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        if self.normalization_field_source is not None:
            result['NormalizationFieldSource'] = self.normalization_field_source

        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type

        if self.normalization_security_domain_id is not None:
            result['NormalizationSecurityDomainId'] = self.normalization_security_domain_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

        if m.get('NormalizationFieldSource') is not None:
            self.normalization_field_source = m.get('NormalizationFieldSource')

        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')

        if m.get('NormalizationSecurityDomainId') is not None:
            self.normalization_security_domain_id = m.get('NormalizationSecurityDomainId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

