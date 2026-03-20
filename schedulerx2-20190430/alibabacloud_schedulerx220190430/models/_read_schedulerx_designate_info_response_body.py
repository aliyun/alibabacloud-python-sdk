# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class ReadSchedulerxDesignateInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ReadSchedulerxDesignateInfoResponseBodyAccessDeniedDetail = None,
        code: int = None,
        data: main_models.ReadSchedulerxDesignateInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The access denial details.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        self.code = code
        # *
        self.data = data
        # The error message returned only if an error occurs.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.ReadSchedulerxDesignateInfoResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ReadSchedulerxDesignateInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadSchedulerxDesignateInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        designate_detail_vos: List[main_models.ReadSchedulerxDesignateInfoResponseBodyDataDesignateDetailVos] = None,
        designate_type: int = None,
        transferable: bool = None,
    ):
        # *
        self.designate_detail_vos = designate_detail_vos
        # The information type of the specified workers.
        # 
        # *   1: the IP address of the specified workers.
        # *   2: the tags of the specified workers.
        # 
        # >  The default value of the DesignateType parameter is 1.
        self.designate_type = designate_type
        # Indicates whether to enable failover for the workers. If you set this parameter to true, the job is scheduled to other workers when the specified workers go offline.
        # 
        # *   true: enables failover for the workers.
        # *   false: disables failover for the workers.
        # 
        # >  The default value of the Transferable parameter is false.
        self.transferable = transferable

    def validate(self):
        if self.designate_detail_vos:
            for v1 in self.designate_detail_vos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DesignateDetailVos'] = []
        if self.designate_detail_vos is not None:
            for k1 in self.designate_detail_vos:
                result['DesignateDetailVos'].append(k1.to_map() if k1 else None)

        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type

        if self.transferable is not None:
            result['Transferable'] = self.transferable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.designate_detail_vos = []
        if m.get('DesignateDetailVos') is not None:
            for k1 in m.get('DesignateDetailVos'):
                temp_model = main_models.ReadSchedulerxDesignateInfoResponseBodyDataDesignateDetailVos()
                self.designate_detail_vos.append(temp_model.from_map(k1))

        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')

        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')

        return self

class ReadSchedulerxDesignateInfoResponseBodyDataDesignateDetailVos(DaraModel):
    def __init__(
        self,
        busy: str = None,
        checked: bool = None,
        key: str = None,
        metrics: main_models.ReadSchedulerxDesignateInfoResponseBodyDataDesignateDetailVosMetrics = None,
        offline: bool = None,
        size: int = None,
        starter: str = None,
        version: str = None,
    ):
        # The status of the workers. Valid values:
        # 
        # *   FREE: idle.
        # *   LOAD5_BUSY: The average of the latest five values of CPU workload is too high.
        # *   HEAP5_BUSY: The average of the latest five values of heap memory usage is too high.
        # *   DISK_BUSY: The disk usage is too high.
        self.busy = busy
        # Indicates whether the workers are specified.
        # 
        # *   true: The workers are specified.
        # *   false: The workers are not specified.
        self.checked = checked
        # The information returned based on the value of the DesignateType parameter.
        # 
        # *   If you set the DesignateType parameter to 2, the tags of the workers are returned.
        # *   If you set the DesignateType parameter to 1, the IP addresses of the workers are returned.
        self.key = key
        # The metric values.
        self.metrics = metrics
        # Indicates whether the workers are offline.
        self.offline = offline
        # The number of workers.
        self.size = size
        # The startup method of the workers.
        self.starter = starter
        # The version of the workers.
        self.version = version

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.busy is not None:
            result['Busy'] = self.busy

        if self.checked is not None:
            result['Checked'] = self.checked

        if self.key is not None:
            result['Key'] = self.key

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.offline is not None:
            result['Offline'] = self.offline

        if self.size is not None:
            result['Size'] = self.size

        if self.starter is not None:
            result['Starter'] = self.starter

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Busy') is not None:
            self.busy = m.get('Busy')

        if m.get('Checked') is not None:
            self.checked = m.get('Checked')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Metrics') is not None:
            temp_model = main_models.ReadSchedulerxDesignateInfoResponseBodyDataDesignateDetailVosMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('Offline') is not None:
            self.offline = m.get('Offline')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Starter') is not None:
            self.starter = m.get('Starter')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ReadSchedulerxDesignateInfoResponseBodyDataDesignateDetailVosMetrics(DaraModel):
    def __init__(
        self,
        cpu_load_1: float = None,
        cpu_load_5: float = None,
        cpu_processors: int = None,
        disk_max: int = None,
        disk_usage: float = None,
        disk_used: int = None,
        exec_count: int = None,
        heap_1usage: float = None,
        heap_1used: float = None,
        heap_5usage: float = None,
        heap_max: int = None,
        share_pool_available_size: int = None,
        share_pool_queue_size: int = None,
    ):
        # The most recent value of CPU workload.
        self.cpu_load_1 = cpu_load_1
        # The average of the latest five values of CPU workload.
        self.cpu_load_5 = cpu_load_5
        # The number of available CPU processors.
        self.cpu_processors = cpu_processors
        # The total disk capacity in MB.
        self.disk_max = disk_max
        # The disk usage.
        self.disk_usage = disk_usage
        # The used disk space in MB.
        self.disk_used = disk_used
        # The number of job executions.
        self.exec_count = exec_count
        # The most recent value of heap memory usage.
        self.heap_1usage = heap_1usage
        # The most recent value of used heap memory in MB.
        self.heap_1used = heap_1used
        # The average of the latest five values of heap memory usage.
        self.heap_5usage = heap_5usage
        # The maximum heap memory in MB.
        self.heap_max = heap_max
        # The number of available resources in the shared pool.
        self.share_pool_available_size = share_pool_available_size
        # The queue size in the shared pool.
        self.share_pool_queue_size = share_pool_queue_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_load_1 is not None:
            result['CpuLoad1'] = self.cpu_load_1

        if self.cpu_load_5 is not None:
            result['CpuLoad5'] = self.cpu_load_5

        if self.cpu_processors is not None:
            result['CpuProcessors'] = self.cpu_processors

        if self.disk_max is not None:
            result['DiskMax'] = self.disk_max

        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage

        if self.disk_used is not None:
            result['DiskUsed'] = self.disk_used

        if self.exec_count is not None:
            result['ExecCount'] = self.exec_count

        if self.heap_1usage is not None:
            result['Heap1Usage'] = self.heap_1usage

        if self.heap_1used is not None:
            result['Heap1Used'] = self.heap_1used

        if self.heap_5usage is not None:
            result['Heap5Usage'] = self.heap_5usage

        if self.heap_max is not None:
            result['HeapMax'] = self.heap_max

        if self.share_pool_available_size is not None:
            result['SharePoolAvailableSize'] = self.share_pool_available_size

        if self.share_pool_queue_size is not None:
            result['SharePoolQueueSize'] = self.share_pool_queue_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuLoad1') is not None:
            self.cpu_load_1 = m.get('CpuLoad1')

        if m.get('CpuLoad5') is not None:
            self.cpu_load_5 = m.get('CpuLoad5')

        if m.get('CpuProcessors') is not None:
            self.cpu_processors = m.get('CpuProcessors')

        if m.get('DiskMax') is not None:
            self.disk_max = m.get('DiskMax')

        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')

        if m.get('DiskUsed') is not None:
            self.disk_used = m.get('DiskUsed')

        if m.get('ExecCount') is not None:
            self.exec_count = m.get('ExecCount')

        if m.get('Heap1Usage') is not None:
            self.heap_1usage = m.get('Heap1Usage')

        if m.get('Heap1Used') is not None:
            self.heap_1used = m.get('Heap1Used')

        if m.get('Heap5Usage') is not None:
            self.heap_5usage = m.get('Heap5Usage')

        if m.get('HeapMax') is not None:
            self.heap_max = m.get('HeapMax')

        if m.get('SharePoolAvailableSize') is not None:
            self.share_pool_available_size = m.get('SharePoolAvailableSize')

        if m.get('SharePoolQueueSize') is not None:
            self.share_pool_queue_size = m.get('SharePoolQueueSize')

        return self

class ReadSchedulerxDesignateInfoResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The authentication operation.
        self.auth_action = auth_action
        # The principal name.
        self.auth_principal_display_name = auth_principal_display_name
        # The principal account.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The principal type.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The permission denial type.
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

