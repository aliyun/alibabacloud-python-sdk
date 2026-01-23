# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBelongAssetMappingRequest(DaraModel):
    def __init__(
        self,
        asset_mapping_query: main_models.GetBelongAssetMappingRequestAssetMappingQuery = None,
        op_tenant_id: int = None,
    ):
        self.asset_mapping_query = asset_mapping_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.asset_mapping_query:
            self.asset_mapping_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_mapping_query is not None:
            result['AssetMappingQuery'] = self.asset_mapping_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetMappingQuery') is not None:
            temp_model = main_models.GetBelongAssetMappingRequestAssetMappingQuery()
            self.asset_mapping_query = temp_model.from_map(m.get('AssetMappingQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetBelongAssetMappingRequestAssetMappingQuery(DaraModel):
    def __init__(
        self,
        belong_guid: str = None,
        relation_type: str = None,
    ):
        # This parameter is required.
        self.belong_guid = belong_guid
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_guid is not None:
            result['BelongGuid'] = self.belong_guid

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongGuid') is not None:
            self.belong_guid = m.get('BelongGuid')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        return self

