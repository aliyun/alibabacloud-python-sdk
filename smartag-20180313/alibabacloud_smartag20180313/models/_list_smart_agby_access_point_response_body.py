# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListSmartAGByAccessPointResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        smart_access_gateways: List[main_models.ListSmartAGByAccessPointResponseBodySmartAccessGateways] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the SAG instance.
        self.smart_access_gateways = smart_access_gateways
        # The number of SAG instances within the access point.
        self.total_count = total_count

    def validate(self):
        if self.smart_access_gateways:
            for v1 in self.smart_access_gateways:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SmartAccessGateways'] = []
        if self.smart_access_gateways is not None:
            for k1 in self.smart_access_gateways:
                result['SmartAccessGateways'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.smart_access_gateways = []
        if m.get('SmartAccessGateways') is not None:
            for k1 in m.get('SmartAccessGateways'):
                temp_model = main_models.ListSmartAGByAccessPointResponseBodySmartAccessGateways()
                self.smart_access_gateways.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSmartAGByAccessPointResponseBodySmartAccessGateways(DaraModel):
    def __init__(
        self,
        associated_ccn_id: str = None,
        hardware_version: str = None,
        routing_strategy: str = None,
        smart_agdescription: str = None,
        smart_agid: str = None,
        smart_agname: str = None,
        smart_agstatus: str = None,
    ):
        # The ID of the Cloud Connect Network (CCN) instance with which the SAG instance is associated.
        self.associated_ccn_id = associated_ccn_id
        # The model of the SAG device with which the SAG instance is associated. Valid values:
        # 
        # *   **sag-1000**.
        # *   **sag-100WM**.
        self.hardware_version = hardware_version
        # The method that the SAG instance uses to synchronize Alibaba Cloud-facing routes. Valid values:
        # 
        # *   **static**: static routing.
        # *   **dynamic**: dynamic routing.
        self.routing_strategy = routing_strategy
        # The description of the SAG instance.
        self.smart_agdescription = smart_agdescription
        # The ID of the SAG instance.
        self.smart_agid = smart_agid
        # The name of the SAG instance.
        self.smart_agname = smart_agname
        # The status of the SAG instance. Valid values:
        # 
        # *   **Active**: The SAG device is connected to Alibaba Cloud.
        # *   **offline**: The SAG device is disconnected from Alibaba Cloud.
        self.smart_agstatus = smart_agstatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_ccn_id is not None:
            result['AssociatedCcnId'] = self.associated_ccn_id

        if self.hardware_version is not None:
            result['HardwareVersion'] = self.hardware_version

        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy

        if self.smart_agdescription is not None:
            result['SmartAGDescription'] = self.smart_agdescription

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agname is not None:
            result['SmartAGName'] = self.smart_agname

        if self.smart_agstatus is not None:
            result['SmartAGStatus'] = self.smart_agstatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedCcnId') is not None:
            self.associated_ccn_id = m.get('AssociatedCcnId')

        if m.get('HardwareVersion') is not None:
            self.hardware_version = m.get('HardwareVersion')

        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')

        if m.get('SmartAGDescription') is not None:
            self.smart_agdescription = m.get('SmartAGDescription')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGName') is not None:
            self.smart_agname = m.get('SmartAGName')

        if m.get('SmartAGStatus') is not None:
            self.smart_agstatus = m.get('SmartAGStatus')

        return self

