# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkInstanceRelationListResponseBody(DaraModel):
    def __init__(
        self,
        network_instance_list: List[main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the network instances.
        self.network_instance_list = network_instance_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.network_instance_list:
            for v1 in self.network_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInstanceList'] = []
        if self.network_instance_list is not None:
            for k1 in self.network_instance_list:
                result['NetworkInstanceList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_instance_list = []
        if m.get('NetworkInstanceList') is not None:
            for k1 in m.get('NetworkInstanceList'):
                temp_model = main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceList()
                self.network_instance_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceList(DaraModel):
    def __init__(
        self,
        associated_cen: List[main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListAssociatedCen] = None,
        connect_type: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        network_instance_type: str = None,
        peer_network_instance_list: List[main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListPeerNetworkInstanceList] = None,
        region_no: str = None,
    ):
        # The associated CEN instance.
        self.associated_cen = associated_cen
        # The connection type.
        self.connect_type = connect_type
        # The ID of the network instance.
        self.network_instance_id = network_instance_id
        # The name of the network instance.
        self.network_instance_name = network_instance_name
        # The type of the network instance.
        self.network_instance_type = network_instance_type
        # The list of peer network instances.
        self.peer_network_instance_list = peer_network_instance_list
        # The region ID.
        self.region_no = region_no

    def validate(self):
        if self.associated_cen:
            for v1 in self.associated_cen:
                 if v1:
                    v1.validate()
        if self.peer_network_instance_list:
            for v1 in self.peer_network_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedCen'] = []
        if self.associated_cen is not None:
            for k1 in self.associated_cen:
                result['AssociatedCen'].append(k1.to_map() if k1 else None)

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name

        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type

        result['PeerNetworkInstanceList'] = []
        if self.peer_network_instance_list is not None:
            for k1 in self.peer_network_instance_list:
                result['PeerNetworkInstanceList'].append(k1.to_map() if k1 else None)

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_cen = []
        if m.get('AssociatedCen') is not None:
            for k1 in m.get('AssociatedCen'):
                temp_model = main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListAssociatedCen()
                self.associated_cen.append(temp_model.from_map(k1))

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')

        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')

        self.peer_network_instance_list = []
        if m.get('PeerNetworkInstanceList') is not None:
            for k1 in m.get('PeerNetworkInstanceList'):
                temp_model = main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListPeerNetworkInstanceList()
                self.peer_network_instance_list.append(temp_model.from_map(k1))

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

class DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListPeerNetworkInstanceList(DaraModel):
    def __init__(
        self,
        associated_cen: List[main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListPeerNetworkInstanceListAssociatedCen] = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        network_instance_type: str = None,
        region_no: str = None,
    ):
        # The associated CEN instance.
        self.associated_cen = associated_cen
        # The ID of the network instance.
        self.network_instance_id = network_instance_id
        # The name of the network instance.
        self.network_instance_name = network_instance_name
        # The type of the network instance.
        self.network_instance_type = network_instance_type
        # The region.
        self.region_no = region_no

    def validate(self):
        if self.associated_cen:
            for v1 in self.associated_cen:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedCen'] = []
        if self.associated_cen is not None:
            for k1 in self.associated_cen:
                result['AssociatedCen'].append(k1.to_map() if k1 else None)

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name

        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_cen = []
        if m.get('AssociatedCen') is not None:
            for k1 in m.get('AssociatedCen'):
                temp_model = main_models.DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListPeerNetworkInstanceListAssociatedCen()
                self.associated_cen.append(temp_model.from_map(k1))

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')

        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

class DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListPeerNetworkInstanceListAssociatedCen(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        attachment_name: str = None,
        cen_id: str = None,
        cen_name: str = None,
        transit_router_type: str = None,
    ):
        # The ID of the network instance connection.
        self.attachment_id = attachment_id
        # The name of the network instance connection.
        self.attachment_name = attachment_name
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The name of the CEN instance.
        self.cen_name = cen_name
        # The version of the transit router. Valid values:
        # 
        # - **Basic**: Basic Edition transit router.
        # 
        # - **Enterprise**: Enterprise Edition transit router.
        self.transit_router_type = transit_router_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_name is not None:
            result['CenName'] = self.cen_name

        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')

        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')

        return self

class DescribeNetworkInstanceRelationListResponseBodyNetworkInstanceListAssociatedCen(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        attachment_name: str = None,
        cen_id: str = None,
        cen_name: str = None,
        transit_router_type: str = None,
    ):
        # The ID of the network instance connection.
        self.attachment_id = attachment_id
        # The name of the network instance connection.
        self.attachment_name = attachment_name
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The name of the CEN instance.
        self.cen_name = cen_name
        # The type of the transit router. Valid values:
        # 
        # - **Basic**: Basic Edition transit router.
        # 
        # - **Enterprise**: Enterprise Edition transit router.
        self.transit_router_type = transit_router_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_name is not None:
            result['CenName'] = self.cen_name

        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')

        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')

        return self

