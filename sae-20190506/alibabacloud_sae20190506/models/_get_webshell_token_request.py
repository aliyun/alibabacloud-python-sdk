# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWebshellTokenRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        container_name: str = None,
        pod_name: str = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the init container.
        # 
        # Note:
        # 
        # *   If you specify this parameter, Cloud Assistant runs the command in the specified container of the instances.
        # 
        # *   If this parameter is specified, the command can run only on Linux instances on which Cloud Assistant Agent 2.2.3.344 or later is installed.
        # 
        #     *   For information about how to query the version of Cloud Assistant Agent, see [Install Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        #     *   For information about how to upgrade Cloud Assistant Agent, see [Upgrade or disable upgrades for Cloud Assistant Agent](https://help.aliyun.com/document_detail/134383.html).
        # 
        # *   If this parameter is specified, the `Username` parameter that is specified in a request to call this operation and the `WorkingDir` parameter that is specified in a request to call the [CreateCommand](https://help.aliyun.com/document_detail/64844.html) operation do not take effect. You can run the command only in the default working directory of the container by using the default user of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # 
        # *   If this parameter is specified, only shell scripts can be run in Linux containers. You cannot add a command in the format similar to `#!/usr/bin/python` at the beginning of a script to specify a script interpreter. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_name = container_name
        # The name of the pod.
        # 
        # This parameter is required.
        self.pod_name = pod_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        return self

