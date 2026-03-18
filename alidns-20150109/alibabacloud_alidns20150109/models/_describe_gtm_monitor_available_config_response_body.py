# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmMonitorAvailableConfigResponseBody(DaraModel):
    def __init__(
        self,
        isp_city_nodes: main_models.DescribeGtmMonitorAvailableConfigResponseBodyIspCityNodes = None,
        request_id: str = None,
    ):
        self.isp_city_nodes = isp_city_nodes
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.isp_city_nodes:
            self.isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isp_city_nodes is not None:
            result['IspCityNodes'] = self.isp_city_nodes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspCityNodes') is not None:
            temp_model = main_models.DescribeGtmMonitorAvailableConfigResponseBodyIspCityNodes()
            self.isp_city_nodes = temp_model.from_map(m.get('IspCityNodes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGtmMonitorAvailableConfigResponseBodyIspCityNodes(DaraModel):
    def __init__(
        self,
        isp_city_node: List[main_models.DescribeGtmMonitorAvailableConfigResponseBodyIspCityNodesIspCityNode] = None,
    ):
        self.isp_city_node = isp_city_node

    def validate(self):
        if self.isp_city_node:
            for v1 in self.isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k1 in self.isp_city_node:
                result['IspCityNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k1 in m.get('IspCityNode'):
                temp_model = main_models.DescribeGtmMonitorAvailableConfigResponseBodyIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeGtmMonitorAvailableConfigResponseBodyIspCityNodesIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        default_selected: bool = None,
        group_name: str = None,
        group_type: str = None,
        isp_code: str = None,
        isp_name: str = None,
        mainland: bool = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.default_selected = default_selected
        self.group_name = group_name
        self.group_type = group_type
        self.isp_code = isp_code
        self.isp_name = isp_name
        self.mainland = mainland

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.isp_code is not None:
            result['IspCode'] = self.isp_code

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.mainland is not None:
            result['Mainland'] = self.mainland

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('Mainland') is not None:
            self.mainland = m.get('Mainland')

        return self

