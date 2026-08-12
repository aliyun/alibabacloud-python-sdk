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
        # Details about access denied errors.
        self.access_denied_detail = access_denied_detail
        # Returned data.
        self.data = data
        # Error code.
        self.err_code = err_code
        # Error message.
        self.err_message = err_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success
        # Total number of records.
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
        # Value after the operation.
        self.after_value = after_value
        # Value before the operation.
        self.before_value = before_value
        # Start time of the operation.
        self.gmt_create = gmt_create
        # End time of the operation.
        self.gmt_end = gmt_end
        # Instance ID.
        self.instance_id = instance_id
        # Operation details.
        self.operation_detail = operation_detail
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
        # Operation progress.
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

