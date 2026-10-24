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
        # The end time of the operation. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The operation ID.
        self.operation_id = operation_id
        # The operation status. Valid values:
        # - COMPLETED: Completed.
        # - TERMINATED: Terminated.
        # - HUMAN_PROCESSING: Pending manual processing.
        self.operation_status = operation_status
        # The operation type. Valid values:
        # - trial_to_official: Upgrades the trial edition to the standard edition.
        # - upgrade_version: Upgrades the version.
        # - update_configuration: Updates the configuration.
        # - update_public_network_status: Updates the public network status.
        # - create_cluster: Creates a cluster.
        # - delete_cluster: Deletes a cluster.
        # - disable_cluster: Stops a cluster.
        # - enable_cluster: Recovers a cluster.
        # - restart_cluster: Restarts a cluster.
        # - migrate_cluster: Migrates a cluster.
        # - renew_cluster: Renews a cluster.
        # - modify_charge_type: Changes the billing method.
        # - UPGRADE: Upgrades a cluster.
        # - DOWNGRADE: Downgrades a cluster.
        # - create_node_group: Creates a node group.
        # - delete_node_group: Deletes a node group.
        # - disable_node_group: Stops a node group.
        # - enable_node_group: Recovers a node group.
        # - sre_operation: Performs O&M on a cluster.
        # - resource_change: Changes resources.
        # - disable_postpaid_resource: Disables pay-as-you-go resources.
        # - enable_postpaid_resource: Recovers pay-as-you-go resources.
        # - restart_node_group: Restarts a compute group.
        # - enable_ha_cluster: Enables high availability (HA) to keep the cluster active.
        # - restart_node: Restarts a node.
        # - backup: Backs up data.
        # - delete_backup: Deletes a data backup.
        # - cancel_backup_task: Cancels a data backup task.
        # - modify_timezone: Modifies the system time zone.
        # - restore: Recovers data.
        # - switch_az: Switches the primary and secondary zones.
        # - rollback_upgrade_version: Rolls back a version upgrade.
        # - scale_out_fe: Scales out FE nodes.
        # - scale_in_fe: Scales in FE nodes.
        # - upgrade_fe_cu: Upgrades the FE CU specifications.
        # - downgrade_fe_cu: Decrease the quota of FE CU specifications.
        # - increase_fe_disk_size: Increases the FE disk size.
        # - decrease_fe_disk_size: Decreases the FE disk size.
        # - increase_fe_disk_number: Increases the number of FE disks.
        # - decrease_fe_disk_number: Decreases the number of FE disks.
        # - upgrade_fe_disk_performance_level: Upgrades the FE disk performance level (PL).
        # - downgrade_fe_disk_performance_level: Decrease the quota of the FE disk performance level (PL).
        # - create_agent: Creates an agent.
        # - upgrade_agent_cu: Upgrades the agent CU specifications.
        # - scale_out_be: Scales out BE nodes.
        # - scale_in_be: Scales in BE nodes.
        # - upgrade_be_cu: Upgrades the BE CU specifications.
        # - downgrade_be_cu: Decrease the quota of BE CU specifications.
        # - increase_be_disk_size: Increases the BE disk size.
        # - decrease_be_disk_size: Decreases the BE disk size.
        # - increase_be_disk_number: Increases the number of BE disks.
        # - decrease_be_disk_number: Decreases the number of BE disks.
        # - upgrade_be_disk_performance_level: Upgrades the BE disk performance level (PL).
        # - downgrade_be_disk_performance_level: Decrease the quota of the BE disk performance level (PL).
        # - upgrade_be_spec_type: Upgrades the BE specification type.
        # - downgrade_be_spec_type: Decrease the quota of the BE specification type.
        # - scale_out_cn: Scales out CN nodes.
        # - scale_in_cn: Scales in CN nodes.
        # - upgrade_cn_cu: Upgrades the CN CU specifications.
        # - downgrade_cn_cu: Decrease the quota of CN CU specifications.
        # - increase_cn_disk_size: Increases the CN disk size.
        # - decrease_cn_disk_size: Decreases the CN disk size.
        # - increase_cn_disk_number: Increases the number of CN disks.
        # - decrease_cn_disk_number: Decreases the number of CN disks.
        # - upgrade_cn_disk_performance: Upgrades the CN disk performance level (PL).
        # - downgrade_cn_disk_performance: Decrease the quota of the CN disk performance level (PL).
        # - upgrade_cn_spec_type: Upgrades the CN specification type.
        # - downgrade_cn_spec_type: Decrease the quota of the CN specification type.
        # - elastic_scale_out_cn: Elastically scales out CN nodes.
        # - elastic_scale_in_cn: Elastically scales in CN nodes.
        self.operation_type = operation_type
        # The page number of the current page. Default value: 1.
        self.page_number = page_number
        # The number of entries per page for paging in a paged query. Default value: 10.
        self.page_size = page_size
        # The start time of the operation. The value is a UNIX timestamp in milliseconds.
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

