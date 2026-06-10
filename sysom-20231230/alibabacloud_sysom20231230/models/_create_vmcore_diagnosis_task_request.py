# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVmcoreDiagnosisTaskRequest(DaraModel):
    def __init__(
        self,
        debuginfo_common_url: str = None,
        debuginfo_url: str = None,
        dmesg_url: str = None,
        task_type: str = None,
        vmcore_url: str = None,
    ):
        # Download link for the debuginfo-common file. This parameter is optional when the diagnosis type is vmcore.  
        # 
        # For CentOS or Alinux kernel diagnosis, the corresponding debuginfo-common file is automatically downloaded, so you do not need to provide this parameter. For kernels of other distributions, you must manually provide the download link for the debuginfo-common file that matches the kernel version.
        self.debuginfo_common_url = debuginfo_common_url
        # The download link of the debuginfo file corresponding to the vmcore file. This parameter is optional when the diagnosis type is vmcore.
        # 
        # For CentOS or Alinux kernel diagnosis, the corresponding debuginfo file is automatically downloaded, so you do not need to provide this parameter. For kernels from other distributions, you must manually provide the download link for the debuginfo file that matches the kernel version.
        self.debuginfo_url = debuginfo_url
        # Download link for the dmesg log file. This parameter is required when the diagnosis type is dmesg.
        self.dmesg_url = dmesg_url
        # Task Type  
        # 
        # vmcore: vmcore file diagnosis task  
        # 
        # dmesg: dmesg log diagnosis task
        # 
        # This parameter is required.
        self.task_type = task_type
        # The download link of the vmcore file. This parameter is required when the diagnosis type is vmcore.
        self.vmcore_url = vmcore_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debuginfo_common_url is not None:
            result['debuginfoCommonUrl'] = self.debuginfo_common_url

        if self.debuginfo_url is not None:
            result['debuginfoUrl'] = self.debuginfo_url

        if self.dmesg_url is not None:
            result['dmesgUrl'] = self.dmesg_url

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.vmcore_url is not None:
            result['vmcoreUrl'] = self.vmcore_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('debuginfoCommonUrl') is not None:
            self.debuginfo_common_url = m.get('debuginfoCommonUrl')

        if m.get('debuginfoUrl') is not None:
            self.debuginfo_url = m.get('debuginfoUrl')

        if m.get('dmesgUrl') is not None:
            self.dmesg_url = m.get('dmesgUrl')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('vmcoreUrl') is not None:
            self.vmcore_url = m.get('vmcoreUrl')

        return self

