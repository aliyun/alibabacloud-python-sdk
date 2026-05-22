# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LaunchServiceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_launch_result_type: str = None,
        version: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The mode of the service online. Valid Type
        # 
        # - PublishNewVersion: Launch new version
        # - PublishOfflineVersion:  The offline version is online again.
        # - UpdateLatestVersion: Update the latest version online
        self.service_launch_result_type = service_launch_result_type
        # The service version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_launch_result_type is not None:
            result['ServiceLaunchResultType'] = self.service_launch_result_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceLaunchResultType') is not None:
            self.service_launch_result_type = m.get('ServiceLaunchResultType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

