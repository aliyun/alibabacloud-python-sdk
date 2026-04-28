# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyModelApiRequest(DaraModel):
    def __init__(
        self,
        gw_cluster_id: str = None,
        model_api_id: str = None,
        model_category: str = None,
        path_prefix: str = None,
        protocol: str = None,
        record_input: str = None,
        record_output: str = None,
        region_id: str = None,
        route_rules: str = None,
    ):
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # This parameter is required.
        self.model_api_id = model_api_id
        # This parameter is required.
        self.model_category = model_category
        # This parameter is required.
        self.path_prefix = path_prefix
        # This parameter is required.
        self.protocol = protocol
        self.record_input = record_input
        self.record_output = record_output
        self.region_id = region_id
        # This parameter is required.
        self.route_rules = route_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.model_api_id is not None:
            result['ModelApiId'] = self.model_api_id

        if self.model_category is not None:
            result['ModelCategory'] = self.model_category

        if self.path_prefix is not None:
            result['PathPrefix'] = self.path_prefix

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.record_input is not None:
            result['RecordInput'] = self.record_input

        if self.record_output is not None:
            result['RecordOutput'] = self.record_output

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_rules is not None:
            result['RouteRules'] = self.route_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ModelApiId') is not None:
            self.model_api_id = m.get('ModelApiId')

        if m.get('ModelCategory') is not None:
            self.model_category = m.get('ModelCategory')

        if m.get('PathPrefix') is not None:
            self.path_prefix = m.get('PathPrefix')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RecordInput') is not None:
            self.record_input = m.get('RecordInput')

        if m.get('RecordOutput') is not None:
            self.record_output = m.get('RecordOutput')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteRules') is not None:
            self.route_rules = m.get('RouteRules')

        return self

