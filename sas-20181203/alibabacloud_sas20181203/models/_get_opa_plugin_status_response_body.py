# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetOpaPluginStatusResponseBody(DaraModel):
    def __init__(
        self,
        install_status: List[main_models.GetOpaPluginStatusResponseBodyInstallStatus] = None,
        request_id: str = None,
    ):
        # The installation status of the components that are required for clusters protected by proactive defense for containers.
        self.install_status = install_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.install_status:
            for v1 in self.install_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstallStatus'] = []
        if self.install_status is not None:
            for k1 in self.install_status:
                result['InstallStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.install_status = []
        if m.get('InstallStatus') is not None:
            for k1 in m.get('InstallStatus'):
                temp_model = main_models.GetOpaPluginStatusResponseBodyInstallStatus()
                self.install_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetOpaPluginStatusResponseBodyInstallStatus(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        install_status: bool = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Indicates whether the component is installed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.install_status = install_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.install_status is not None:
            result['InstallStatus'] = self.install_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstallStatus') is not None:
            self.install_status = m.get('InstallStatus')

        return self

