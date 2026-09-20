# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckFileDeploymentRequest(DaraModel):
    def __init__(
        self,
        check_detail_url: str = None,
        checker_instance_id: str = None,
        status: str = None,
    ):
        # Deprecated.
        self.check_detail_url = check_detail_url
        # The instance ID to which the file checker belongs. You can obtain this value from the CheckerInstanceId field in the file publish check event.
        # 
        # This parameter is required.
        self.checker_instance_id = checker_instance_id
        # The check status of the file pending deployment. Valid values:
        # 
        # - OK: The file passed the check.
        # - WARN: The file passed the check but has warnings.
        # - FAIL: The file failed the check.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_detail_url is not None:
            result['CheckDetailUrl'] = self.check_detail_url

        if self.checker_instance_id is not None:
            result['CheckerInstanceId'] = self.checker_instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckDetailUrl') is not None:
            self.check_detail_url = m.get('CheckDetailUrl')

        if m.get('CheckerInstanceId') is not None:
            self.checker_instance_id = m.get('CheckerInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

