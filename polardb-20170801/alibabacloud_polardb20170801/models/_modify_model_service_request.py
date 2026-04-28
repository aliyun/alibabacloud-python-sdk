# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyModelServiceRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        gw_cluster_id: str = None,
        input_cost_points_per_million: str = None,
        model_category: str = None,
        model_service_id: str = None,
        name: str = None,
        output_cost_points_per_million: str = None,
        protocol: str = None,
        region_id: str = None,
        request_cost_points: str = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.input_cost_points_per_million = input_cost_points_per_million
        # This parameter is required.
        self.model_category = model_category
        # This parameter is required.
        self.model_service_id = model_service_id
        # This parameter is required.
        self.name = name
        self.output_cost_points_per_million = output_cost_points_per_million
        # This parameter is required.
        self.protocol = protocol
        self.region_id = region_id
        self.request_cost_points = request_cost_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.input_cost_points_per_million is not None:
            result['InputCostPointsPerMillion'] = self.input_cost_points_per_million

        if self.model_category is not None:
            result['ModelCategory'] = self.model_category

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output_cost_points_per_million is not None:
            result['OutputCostPointsPerMillion'] = self.output_cost_points_per_million

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_cost_points is not None:
            result['RequestCostPoints'] = self.request_cost_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('InputCostPointsPerMillion') is not None:
            self.input_cost_points_per_million = m.get('InputCostPointsPerMillion')

        if m.get('ModelCategory') is not None:
            self.model_category = m.get('ModelCategory')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputCostPointsPerMillion') is not None:
            self.output_cost_points_per_million = m.get('OutputCostPointsPerMillion')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestCostPoints') is not None:
            self.request_cost_points = m.get('RequestCostPoints')

        return self

