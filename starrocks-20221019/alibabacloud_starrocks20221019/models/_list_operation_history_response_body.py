# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class ListOperationHistoryResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.ListOperationHistoryResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of records.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListOperationHistoryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListOperationHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        after_value: str = None,
        before_value: str = None,
        gmt_create: int = None,
        gmt_end: int = None,
        instance_id: str = None,
        operation_detail: str = None,
        operation_id: str = None,
        operation_status: str = None,
        operation_type: str = None,
        progress: int = None,
    ):
        # The value after the operation.
        self.after_value = after_value
        # The value before the operation.
        self.before_value = before_value
        # The start time of the operation.
        self.gmt_create = gmt_create
        # The end time of the operation.
        self.gmt_end = gmt_end
        # The instance ID.
        self.instance_id = instance_id
        # The operation details.
        self.operation_detail = operation_detail
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
        # The operation progress.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_value is not None:
            result['AfterValue'] = self.after_value

        if self.before_value is not None:
            result['BeforeValue'] = self.before_value

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_end is not None:
            result['GmtEnd'] = self.gmt_end

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operation_detail is not None:
            result['OperationDetail'] = self.operation_detail

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.progress is not None:
            result['Progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterValue') is not None:
            self.after_value = m.get('AfterValue')

        if m.get('BeforeValue') is not None:
            self.before_value = m.get('BeforeValue')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtEnd') is not None:
            self.gmt_end = m.get('GmtEnd')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperationDetail') is not None:
            self.operation_detail = m.get('OperationDetail')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        return self

