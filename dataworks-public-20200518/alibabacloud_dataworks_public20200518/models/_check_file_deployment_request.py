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
        # This parameter is deprecated.
        self.check_detail_url = check_detail_url
        # The ID of the instance to which the file checker belongs. You can obtain the ID from the CheckerInstanceId parameter in the check event logs returned by DataWorks.
        # 
        # This parameter is required.
        self.checker_instance_id = checker_instance_id
        # The check status of the file that you want to deploy. Valid values:
        # 
        # *   OK: The file passes the check.
        # *   WARN: The file passes the check, but an alert is reported.
        # *   FAIL: The file fails the check.
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

