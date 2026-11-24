# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelApiRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        force_model: str = None,
        gw_cluster_id: str = None,
        model_category: str = None,
        model_mappings: str = None,
        model_routing: str = None,
        name: str = None,
        path_prefix: str = None,
        protocol: str = None,
        record_input: str = None,
        record_output: str = None,
        region_id: str = None,
        route_rules: str = None,
    ):
        # The gateway retry configuration.
        self.config = config
        # The forced model.
        self.force_model = force_model
        # The ID of the gateway instance. You can obtain this ID from the GwClusterId value returned by the CreateGateway operation.
        # 
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # The category. Valid values:
        # * **text**
        # * **embedding**
        # * **rerank**
        self.model_category = model_category
        # The model name mappings, specified as a JSON array string. Each element is in the format of {"Source":"client model name","Target":"upstream model name"}. The Source parameter is matched in a case-insensitive manner and must be unique. The Target parameter retains its original case when forwarded. Both parameters cannot be empty and cannot contain leading or trailing spaces.
        self.model_mappings = model_mappings
        # The intelligent routing candidate list, specified as a JSON object string. Currently, it only contains AllowedModels, which is a non-empty array of unique model names. The order of the array determines the candidate order. Do not pass the Enabled, cost, or quality tier parameters. Saving candidates does not enable the feature. You must first call the EnableModelRouting operation to obtain the gateway entitlements.
        self.model_routing = model_routing
        # The name of the model API.
        self.name = name
        # The API path prefix.
        self.path_prefix = path_prefix
        # The protocol. Valid values:
        # 
        # * **openai**
        # * **anthropic**
        # * **bailian**
        # * **vllm**
        self.protocol = protocol
        # The number of input points.
        self.record_input = record_input
        # The number of output points.
        self.record_output = record_output
        # The region ID.
        self.region_id = region_id
        # The list of routing rules, specified as a JSON array string.
        self.route_rules = route_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.force_model is not None:
            result['ForceModel'] = self.force_model

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.model_category is not None:
            result['ModelCategory'] = self.model_category

        if self.model_mappings is not None:
            result['ModelMappings'] = self.model_mappings

        if self.model_routing is not None:
            result['ModelRouting'] = self.model_routing

        if self.name is not None:
            result['Name'] = self.name

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
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ForceModel') is not None:
            self.force_model = m.get('ForceModel')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ModelCategory') is not None:
            self.model_category = m.get('ModelCategory')

        if m.get('ModelMappings') is not None:
            self.model_mappings = m.get('ModelMappings')

        if m.get('ModelRouting') is not None:
            self.model_routing = m.get('ModelRouting')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

