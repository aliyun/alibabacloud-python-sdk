# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceDiagnosisSummaryResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBInstanceDiagnosisSummaryResponseBodyItems] = None,
        master_status_info: main_models.DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo = None,
        page_number: str = None,
        request_id: str = None,
        segment_status_info: main_models.DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo = None,
        total_count: str = None,
    ):
        # The group ID.
        self.items = items
        # The state information about the coordinator node.
        self.master_status_info = master_status_info
        # The page number.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # The state information about compute nodes.
        self.segment_status_info = segment_status_info
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.master_status_info:
            self.master_status_info.validate()
        if self.segment_status_info:
            self.segment_status_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.master_status_info is not None:
            result['MasterStatusInfo'] = self.master_status_info.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.segment_status_info is not None:
            result['SegmentStatusInfo'] = self.segment_status_info.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBInstanceDiagnosisSummaryResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MasterStatusInfo') is not None:
            temp_model = main_models.DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo()
            self.master_status_info = temp_model.from_map(m.get('MasterStatusInfo'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SegmentStatusInfo') is not None:
            temp_model = main_models.DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo()
            self.segment_status_info = temp_model.from_map(m.get('SegmentStatusInfo'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo(DaraModel):
    def __init__(
        self,
        exception_node_num: int = None,
        normal_node_num: int = None,
        not_preferred_node_num: int = None,
        not_syncing_node_num: int = None,
        preferred_node_num: int = None,
        synced_node_num: int = None,
    ):
        # The number of abnormal nodes.
        self.exception_node_num = exception_node_num
        # The number of normal nodes.
        self.normal_node_num = normal_node_num
        # The number of nodes whose roles are reversed.
        self.not_preferred_node_num = not_preferred_node_num
        # The number of unsynchronized nodes.
        self.not_syncing_node_num = not_syncing_node_num
        # The number of nodes whose roles are normal.
        self.preferred_node_num = preferred_node_num
        # The number of synchronized nodes.
        self.synced_node_num = synced_node_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_node_num is not None:
            result['ExceptionNodeNum'] = self.exception_node_num

        if self.normal_node_num is not None:
            result['NormalNodeNum'] = self.normal_node_num

        if self.not_preferred_node_num is not None:
            result['NotPreferredNodeNum'] = self.not_preferred_node_num

        if self.not_syncing_node_num is not None:
            result['NotSyncingNodeNum'] = self.not_syncing_node_num

        if self.preferred_node_num is not None:
            result['PreferredNodeNum'] = self.preferred_node_num

        if self.synced_node_num is not None:
            result['SyncedNodeNum'] = self.synced_node_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionNodeNum') is not None:
            self.exception_node_num = m.get('ExceptionNodeNum')

        if m.get('NormalNodeNum') is not None:
            self.normal_node_num = m.get('NormalNodeNum')

        if m.get('NotPreferredNodeNum') is not None:
            self.not_preferred_node_num = m.get('NotPreferredNodeNum')

        if m.get('NotSyncingNodeNum') is not None:
            self.not_syncing_node_num = m.get('NotSyncingNodeNum')

        if m.get('PreferredNodeNum') is not None:
            self.preferred_node_num = m.get('PreferredNodeNum')

        if m.get('SyncedNodeNum') is not None:
            self.synced_node_num = m.get('SyncedNodeNum')

        return self

class DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo(DaraModel):
    def __init__(
        self,
        exception_node_num: int = None,
        normal_node_num: int = None,
        not_preferred_node_num: int = None,
        not_syncing_node_num: int = None,
        preferred_node_num: int = None,
        synced_node_num: int = None,
    ):
        # The number of abnormal nodes.
        self.exception_node_num = exception_node_num
        # The number of normal nodes.
        self.normal_node_num = normal_node_num
        # The number of nodes whose roles are reversed.
        self.not_preferred_node_num = not_preferred_node_num
        # The number of unsynchronized nodes.
        self.not_syncing_node_num = not_syncing_node_num
        # The number of nodes whose roles are normal.
        self.preferred_node_num = preferred_node_num
        # The number of synchronized nodes.
        self.synced_node_num = synced_node_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_node_num is not None:
            result['ExceptionNodeNum'] = self.exception_node_num

        if self.normal_node_num is not None:
            result['NormalNodeNum'] = self.normal_node_num

        if self.not_preferred_node_num is not None:
            result['NotPreferredNodeNum'] = self.not_preferred_node_num

        if self.not_syncing_node_num is not None:
            result['NotSyncingNodeNum'] = self.not_syncing_node_num

        if self.preferred_node_num is not None:
            result['PreferredNodeNum'] = self.preferred_node_num

        if self.synced_node_num is not None:
            result['SyncedNodeNum'] = self.synced_node_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionNodeNum') is not None:
            self.exception_node_num = m.get('ExceptionNodeNum')

        if m.get('NormalNodeNum') is not None:
            self.normal_node_num = m.get('NormalNodeNum')

        if m.get('NotPreferredNodeNum') is not None:
            self.not_preferred_node_num = m.get('NotPreferredNodeNum')

        if m.get('NotSyncingNodeNum') is not None:
            self.not_syncing_node_num = m.get('NotSyncingNodeNum')

        if m.get('PreferredNodeNum') is not None:
            self.preferred_node_num = m.get('PreferredNodeNum')

        if m.get('SyncedNodeNum') is not None:
            self.synced_node_num = m.get('SyncedNodeNum')

        return self

class DescribeDBInstanceDiagnosisSummaryResponseBodyItems(DaraModel):
    def __init__(
        self,
        hostname: str = None,
        node_address: str = None,
        node_cid: str = None,
        node_id: str = None,
        node_name: str = None,
        node_port: str = None,
        node_preferred_role: str = None,
        node_replication_mode: str = None,
        node_role: str = None,
        node_status: str = None,
        node_type: str = None,
    ):
        # The name of the node.
        self.hostname = hostname
        # The IP address of the node.
        self.node_address = node_address
        # The node group ID.
        self.node_cid = node_cid
        # The node ID.
        self.node_id = node_id
        # The name of the host where the node resides.
        self.node_name = node_name
        # The port number of the node.
        self.node_port = node_port
        # The initial role of the node. Valid values:
        # 
        # *   **primary**: primary node.
        # *   **mirror**: secondary node.
        # 
        # If the value of this parameter is the same as that of **NodeRole**, no primary/secondary switchover occurs. If the value of this parameter is different from that of **NodeRole**, a primary/secondary switchover occurs.
        self.node_preferred_role = node_preferred_role
        # The data synchronization state of the node. Valid values:
        # 
        # *   **Synced**: The node data is synchronized.
        # *   **Not Syncing**: The node data is not synchronized.
        # *   **No sync required**: Data synchronization is not required. This value may be returned only for the coordinator node.
        self.node_replication_mode = node_replication_mode
        # The current role of the node. Valid values:
        # 
        # *   **primary**: primary node.
        # *   **mirror**: secondary node.
        self.node_role = node_role
        # The running state of the node. Valid values:
        # 
        # *   **UP**: The node is running.
        # *   **DOWN**: The node is faulty.
        self.node_status = node_status
        # The type of the node. Valid values:
        # 
        # *   **master**: primary coordinator node.
        # *   **slave**: standby coordinator node.
        # *   **segment**: compute node.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.node_address is not None:
            result['NodeAddress'] = self.node_address

        if self.node_cid is not None:
            result['NodeCID'] = self.node_cid

        if self.node_id is not None:
            result['NodeID'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_port is not None:
            result['NodePort'] = self.node_port

        if self.node_preferred_role is not None:
            result['NodePreferredRole'] = self.node_preferred_role

        if self.node_replication_mode is not None:
            result['NodeReplicationMode'] = self.node_replication_mode

        if self.node_role is not None:
            result['NodeRole'] = self.node_role

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('NodeAddress') is not None:
            self.node_address = m.get('NodeAddress')

        if m.get('NodeCID') is not None:
            self.node_cid = m.get('NodeCID')

        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')

        if m.get('NodePreferredRole') is not None:
            self.node_preferred_role = m.get('NodePreferredRole')

        if m.get('NodeReplicationMode') is not None:
            self.node_replication_mode = m.get('NodeReplicationMode')

        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

