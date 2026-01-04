# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListBusinessAccessPointsResponseBody(DaraModel):
    def __init__(
        self,
        business_access_points: List[main_models.ListBusinessAccessPointsResponseBodyBusinessAccessPoints] = None,
        request_id: str = None,
    ):
        # The list of access points.
        self.business_access_points = business_access_points
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.business_access_points:
            for v1 in self.business_access_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BusinessAccessPoints'] = []
        if self.business_access_points is not None:
            for k1 in self.business_access_points:
                result['BusinessAccessPoints'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.business_access_points = []
        if m.get('BusinessAccessPoints') is not None:
            for k1 in m.get('BusinessAccessPoints'):
                temp_model = main_models.ListBusinessAccessPointsResponseBodyBusinessAccessPoints()
                self.business_access_points.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBusinessAccessPointsResponseBodyBusinessAccessPoints(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        access_point_name: str = None,
        cloud_box_instance_ids: str = None,
        latitude: float = None,
        longitude: float = None,
        optical_module_models: List[main_models.ListBusinessAccessPointsResponseBodyBusinessAccessPointsOpticalModuleModels] = None,
        support_line_operator: str = None,
        support_port_types: str = None,
    ):
        # The ID of the access point.
        self.access_point_id = access_point_id
        # The name of the access point.
        self.access_point_name = access_point_name
        # The ID of the cloud box.
        # 
        # >  You can query this parameter if the Express Connect circuits and access points are of the cloud box type.
        self.cloud_box_instance_ids = cloud_box_instance_ids
        # The latitude of the access point.
        self.latitude = latitude
        # The longitude of the access point.
        self.longitude = longitude
        self.optical_module_models = optical_module_models
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CT**: China Telecom.
        # *   **CU**: China Unicom.
        # *   **CM**: China Mobile.
        # *   **CO**: other connectivity providers in the Chinese mainland.
        # *   **Equinix**: Equinix.
        # *   **Other**: other connectivity providers outside the Chinese mainland.
        self.support_line_operator = support_line_operator
        # The port type supported by the access point. Valid values:
        # 
        # *   **100Base-T**: 100 Mbit/s copper Ethernet port
        # *   **1000Base-T**: 1,000 Mbit/s copper Ethernet port
        # *   **1000Base-LX**: 1,000 Mbit/s single-mode optical port (10 km)
        # *   **10GBase-T**: 10,000 Mbit/s copper Ethernet port
        # *   **10GBase-LR**: 10,000 Mbit/s single-mode optical port (10 km)
        # *   **40GBase-LR**: 40,000 Mbit/s single-mode optical port
        # *   **100GBase-LR**: 100,000 Mbit/s single-mode optical port
        # 
        # >  To use ports 40GBase-LR and 100GBase-LR, you must first contact your account manager.
        self.support_port_types = support_port_types

    def validate(self):
        if self.optical_module_models:
            for v1 in self.optical_module_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name

        if self.cloud_box_instance_ids is not None:
            result['CloudBoxInstanceIds'] = self.cloud_box_instance_ids

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        result['OpticalModuleModels'] = []
        if self.optical_module_models is not None:
            for k1 in self.optical_module_models:
                result['OpticalModuleModels'].append(k1.to_map() if k1 else None)

        if self.support_line_operator is not None:
            result['SupportLineOperator'] = self.support_line_operator

        if self.support_port_types is not None:
            result['SupportPortTypes'] = self.support_port_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')

        if m.get('CloudBoxInstanceIds') is not None:
            self.cloud_box_instance_ids = m.get('CloudBoxInstanceIds')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        self.optical_module_models = []
        if m.get('OpticalModuleModels') is not None:
            for k1 in m.get('OpticalModuleModels'):
                temp_model = main_models.ListBusinessAccessPointsResponseBodyBusinessAccessPointsOpticalModuleModels()
                self.optical_module_models.append(temp_model.from_map(k1))

        if m.get('SupportLineOperator') is not None:
            self.support_line_operator = m.get('SupportLineOperator')

        if m.get('SupportPortTypes') is not None:
            self.support_port_types = m.get('SupportPortTypes')

        return self

class ListBusinessAccessPointsResponseBodyBusinessAccessPointsOpticalModuleModels(DaraModel):
    def __init__(
        self,
        optical_module_model: str = None,
        port_type: str = None,
    ):
        self.optical_module_model = optical_module_model
        self.port_type = port_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.optical_module_model is not None:
            result['OpticalModuleModel'] = self.optical_module_model

        if self.port_type is not None:
            result['PortType'] = self.port_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpticalModuleModel') is not None:
            self.optical_module_model = m.get('OpticalModuleModel')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        return self

