# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperationHistoryRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        operation_id: str = None,
        operation_status: str = None,
        operation_type: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # End time of the operation.
        self.end_time = end_time
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Operation ID.
        self.operation_id = operation_id
        # Operation status:
        # 
        # - COMPLETED: completed
        # 
        # - TERMINATED: terminated
        # 
        # - HUMAN_PROCESSING: pending manual processing
        self.operation_status = operation_status
        # Operation type. Valid values:
        # 
        # - trial_to_official: upgrade from Trial Edition to Standard Edition
        # 
        # - upgrade_version: upgrade version
        # 
        # - update_configuration: update configuration
        # 
        # - update_public_network_status: update public network status
        # 
        # - create_cluster: create cluster
        # 
        # - delete_cluster: delete cluster
        # 
        # - disable_cluster: stop cluster
        # 
        # - enable_cluster: resume cluster
        # 
        # - restart_cluster: restart cluster
        # 
        # - migrate_cluster: migrate cluster
        # 
        # - renew_cluster: renew cluster
        # 
        # - modify_charge_type: change billing method
        # 
        # - UPGRADE: upgrade cluster
        # 
        # - DOWNGRADE: downgrade cluster
        # 
        # - create_node_group: create node group
        # 
        # - delete_node_group: delete node group
        # 
        # - disable_node_group: stop node group
        # 
        # - enable_node_group: resume node group
        # 
        # - sre_operation: O\\&M cluster
        # 
        # - resource_change: resource change
        # 
        # - disable_postpaid_resource: disable pay-as-you-go resources
        # 
        # - enable_postpaid_resource: enable pay-as-you-go resources
        # 
        # - restart_node_group: restart compute group
        # 
        # - enable_ha_cluster: enable high availability (HA) for cluster
        # 
        # - restart_node: restart node
        # 
        # - backup: data backup
        # 
        # - delete_backup: delete data backup
        # 
        # - cancel_backup_task: cancel data backup
        # 
        # - modify_timezone: modify system time zone
        # 
        # - restore: data restoration
        # 
        # - switch_az: switch primary and secondary zones
        # 
        # - rollback_upgrade_version: roll back version upgrade
        # 
        # - scale_out_fe: scale out FE
        # 
        # - scale_in_fe: scale in FE
        # 
        # - upgrade_fe_cu: upgrade FE CU specification
        # 
        # - downgrade_fe_cu: downgrade FE CU specification
        # 
        # - increase_fe_disk_size: increase FE disk size
        # 
        # - decrease_fe_disk_size: decrease FE disk size
        # 
        # - increase_fe_disk_number: increase FE disk count
        # 
        # - decrease_fe_disk_number: decrease FE disk count
        # 
        # - upgrade_fe_disk_performance_level: upgrade FE disk performance level
        # 
        # - downgrade_fe_disk_performance_level: downgrade FE disk performance level
        # 
        # - create_agent: create Agent
        # 
        # - upgrade_agent_cu: upgrade Agent CU specification
        # 
        # - scale_out_be: scale out BE
        # 
        # - scale_in_be: scale in BE
        # 
        # - upgrade_be_cu: upgrade BE CU specification
        # 
        # - downgrade_be_cu: downgrade BE CU specification
        # 
        # - increase_be_disk_size: increase BE disk size
        # 
        # - decrease_be_disk_size: decrease BE disk size
        # 
        # - increase_be_disk_number: increase BE disk count
        # 
        # - decrease_be_disk_number: decrease BE disk count
        # 
        # - upgrade_be_disk_performance_level: upgrade BE disk performance level
        # 
        # - downgrade_be_disk_performance_level: downgrade BE disk performance level
        # 
        # - upgrade_be_spec_type: upgrade BE specification type
        # 
        # - downgrade_be_spec_type: downgrade BE specification type
        # 
        # - scale_out_cn: scale out CN
        # 
        # - scale_in_cn: scale in CN
        # 
        # - upgrade_cn_cu: upgrade CN CU specification
        # 
        # - downgrade_cn_cu: downgrade CN CU specification
        # 
        # - increase_cn_disk_size: increase CN disk size
        # 
        # - decrease_cn_disk_size: decrease CN disk size
        # 
        # - increase_cn_disk_number: increase CN disk count
        # 
        # - decrease_cn_disk_number: decrease CN disk count
        # 
        # - upgrade_cn_disk_performance: upgrade CN disk performance level
        # 
        # - downgrade_cn_disk_performance: downgrade CN disk performance level
        # 
        # - upgrade_cn_spec_type: upgrade CN specification type
        # 
        # - downgrade_cn_spec_type: downgrade CN specification type
        # 
        # - elastic_scale_out_cn: elastically scale out CN
        # 
        # - elastic_scale_in_cn: elastically scale in CN
        self.operation_type = operation_type
        # Page number of the current page. Default value: 1.
        self.page_number = page_number
        # Number of entries per page for paged queries. Default value: 10.
        self.page_size = page_size
        # Start time of the operation.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

