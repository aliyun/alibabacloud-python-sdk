# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateK8sApplicationConfigRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cluster_id: str = None,
        cpu_limit: str = None,
        cpu_request: str = None,
        ephemeral_storage_limit: str = None,
        ephemeral_storage_request: str = None,
        mcpu_limit: str = None,
        mcpu_request: str = None,
        memory_limit: str = None,
        memory_request: str = None,
        timeout: int = None,
    ):
        # The ID of the application. You can query the application ID by calling the ListApplication operation. For more information, see [ListApplication](https://help.aliyun.com/document_detail/423162.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the cluster. You can query the cluster ID by calling the ListCluster operation. For more information, see [ListCluster](https://help.aliyun.com/document_detail/411844.html).
        self.cluster_id = cluster_id
        # The maximum number of CPU cores allowed for each application instance when the application is running. The value 0 indicates that no limit is set on CPU cores.
        self.cpu_limit = cpu_limit
        # The number of CPU cores requested for each application instance when the application is running. Unit: cores. We recommend that you set this parameter. The value 0 indicates that no limit is set on CPU cores.
        # 
        # > You must set this parameter together with the CpuLimit parameter. Make sure that the value of this parameter does not exceed that of the CpuLimit parameter.
        self.cpu_request = cpu_request
        # The maximum size of space required by ephemeral storage. Unit: GB. The value 0 indicates that no limit is set on the ephemeral storage space.
        self.ephemeral_storage_limit = ephemeral_storage_limit
        # The minimum size of space required by ephemeral storage. Unit: GB. The value 0 indicates that no limit is set on the ephemeral storage space.
        # 
        # > You must set this parameter together with the EphemeralStorageLimit parameter. Make sure that the value of this parameter does not exceed that of the EphemeralStorageLimit parameter.
        self.ephemeral_storage_request = ephemeral_storage_request
        # The maximum number of CPU cores allowed. The value 0 indicates that no limit is set on CPU cores.
        self.mcpu_limit = mcpu_limit
        # The minimum number of CPU cores required. Unit: cores. The value 0 indicates that no limit is set on CPU cores.
        # 
        # > You must set this parameter together with the CpuLimit parameter. Make sure that the value of this parameter does not exceed that of the CpuLimit parameter.
        self.mcpu_request = mcpu_request
        # The maximum size of memory allowed for each application instance when the application is running. Unit: MB. The value 0 indicates that no limit is set on the memory size.
        self.memory_limit = memory_limit
        # The size of memory requested for each application instance when the application is running. Unit: MB. We recommend that you set this parameter. If you do not want to apply for a memory quota, set this parameter to 0.
        # 
        # > You must set this parameter together with the MemoryLimit parameter. Make sure that the value of this parameter does not exceed that of the MemoryLimit parameter.
        self.memory_request = memory_request
        # The timeout period of the change process. Valid values: 1 to 1800. Default value: 600. Unit: seconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit

        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request

        if self.ephemeral_storage_limit is not None:
            result['EphemeralStorageLimit'] = self.ephemeral_storage_limit

        if self.ephemeral_storage_request is not None:
            result['EphemeralStorageRequest'] = self.ephemeral_storage_request

        if self.mcpu_limit is not None:
            result['McpuLimit'] = self.mcpu_limit

        if self.mcpu_request is not None:
            result['McpuRequest'] = self.mcpu_request

        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit

        if self.memory_request is not None:
            result['MemoryRequest'] = self.memory_request

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')

        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')

        if m.get('EphemeralStorageLimit') is not None:
            self.ephemeral_storage_limit = m.get('EphemeralStorageLimit')

        if m.get('EphemeralStorageRequest') is not None:
            self.ephemeral_storage_request = m.get('EphemeralStorageRequest')

        if m.get('McpuLimit') is not None:
            self.mcpu_limit = m.get('McpuLimit')

        if m.get('McpuRequest') is not None:
            self.mcpu_request = m.get('McpuRequest')

        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')

        if m.get('MemoryRequest') is not None:
            self.memory_request = m.get('MemoryRequest')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

